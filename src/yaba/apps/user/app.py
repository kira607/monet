import json
import os

import requests

from flask import Blueprint, redirect, request, url_for, flash, Response
from flask import render_template, current_app
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from oauthlib.oauth2 import WebApplicationClient
from werkzeug.security import generate_password_hash

from yaba.orm import db
from yaba.orm.models import User

from .controller import AuthController

user_app = Blueprint(
    'user',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/user',
    static_url_path='static',
)
controller = AuthController()
login_manager = LoginManager()

login_manager.login_view = 'user.login'
login_manager.login_message = 'Please login to access this page'
login_manager.login_message_category = 'success'

GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', None)
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', None)
GOOGLE_DISCOVERY_URL = 'https://accounts.google.com/.well-known/openid-configuration'

oauth_client = WebApplicationClient(GOOGLE_CLIENT_ID)


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


@login_manager.user_loader
def load_user(user_id) -> User:
    return User.query.filter_by(id=user_id).first()


@user_app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']

        if len(username) <= 4:
            flash('Name must be at least 4 characters'); return redirect(url_for('user.register'))
        if User.query.filter_by(username=username).first():
            flash('User with given username already exists'); return redirect(url_for('user.register'))
        if len(request.form['email']) <= 4:
            flash('Wrong email'); return redirect(url_for('user.register'))
        if User.query.filter_by(email=email).first():
            flash('User with given email already exists'); return redirect(url_for('user.register'))
        if len(password1) < 8:
            flash('Password must be at least 8 characters'); return redirect(url_for('user.register'))
        if password1 != password2:
            flash('Passwords do not match'); return redirect(url_for('user.register'))

        try:
            new_user = User()
            new_user.username = username
            new_user.name = name
            new_user.lastname = lastname
            new_user.email = email
            new_user.password = generate_password_hash(password1)
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            flash(f'Error while registering user (DB query failed): {e}'); return redirect(url_for('user.register'))

        flash("Registration successful!", "success")
        return redirect(url_for('user.login'))

    return render_template('register.html')


@user_app.route('/login', methods=['GET', 'POST'])
def login() -> Response | str:
    if current_user.is_authenticated:
        return redirect(url_for('user.profile'))

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        remember = bool(request.form.get('remember'))

        user = User.query.filter_by(username=username).first()
        if not user:
            flash('Wrong username')
            return redirect(url_for('user.login'))

        if not user.check_password(password):
            flash('Wrong password')
            return redirect(url_for('user.login'))

        login_user(user, remember=remember)
        return redirect(request.args.get('next') or url_for('user.profile'))

    return render_template('login.html')


@user_app.route('/glogin')
def google_login():
    current_app.logger.info("Initiating google login")
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    current_app.logger.info(google_provider_cfg)
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    current_app.logger.info(authorization_endpoint)

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = oauth_client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    current_app.logger.info(request_uri)
    return redirect(request_uri)


@user_app.route('/glogin/callback')
def google_login_callback():
    current_app.logger.info('processing google login callback')
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = oauth_client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    oauth_client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = oauth_client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    current_app.logger.info(userinfo_response.json())
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400
    
    # Create a user in your db with the information provided
    # by Google
    user = User(
        name=users_name,
        email=users_email,
        # profile_pic=picture
    )

    # Doesn't exist? Add it to the database.
    if not User.get(unique_id):
        User.create(unique_id, users_name, users_email, picture)

    # Begin user session by logging the user in
    login_user(user)

    # Send user back to homepage
    return redirect(url_for("index"))

@user_app.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@user_app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out', 'success')
    return redirect(url_for('user.login'))
