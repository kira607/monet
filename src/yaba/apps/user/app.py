from flask import Blueprint, redirect, request, url_for, flash, Response
from flask import render_template
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
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
