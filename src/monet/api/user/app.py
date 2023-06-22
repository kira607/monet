# mypy: disable-error-code="assignment"

import bcrypt
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from werkzeug import Response

from monet.logger import logger
from monet.orm import db
from monet.orm.models import User, UserEvent, UserEventType

from .controller import UserController
from .forms import UserLoginForm, UserRegistrationForm

user_app = Blueprint(
    "user",
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/user",
    static_url_path="static",
)
controller = UserController()
login_manager = LoginManager()

login_manager.login_view = "user.login"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "success"


@login_manager.user_loader
def load_user(user_id: int) -> User:
    """Load a user model by id."""
    return User.query.filter_by(id=user_id).first()


@user_app.route("/", methods=["GET"])
def root() -> Response | str:
    """Get an app root."""
    if current_user.is_authenticated():
        return redirect(url_for("user.profile"))
    return redirect(url_for("user.login"))


@user_app.route("/register", methods=["GET", "POST"])
def register() -> Response | str:
    """Register a new user."""
    form = UserRegistrationForm(request.form)

    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            form.email.errors.append("User with given email already exists")
            return render_template("register.html", form=form)

        try:
            new_user = User()
            new_user.name = form.name.data
            new_user.email = form.email.data
            new_user.password = bcrypt.hashpw(
                form.password.data.encode("utf-8"), bcrypt.gensalt()
            )

            reg_event = UserEvent()
            reg_event.event_type = UserEventType.REGISTER
            reg_event.ip = request.remote_addr

            db.session.add(new_user)
            db.session.commit()

            reg_event.user_id = new_user.id

            db.session.add(reg_event)
            db.session.commit()
        except Exception as e:
            flash(f"Error while registering user (DB query failed): {e}", "danger")
            return render_template("register.html", form=form)

        flash("Registration successful!", "success")
        return redirect(url_for("user.login"))

    for field in form:
        if field.errors:
            for error in field.errors:
                logger.info(f"Error in field {field.name}: {error}")

    return render_template("register.html", form=form)


@user_app.route("/login", methods=["GET", "POST"])
def login() -> Response | str:
    """Get a login page or login a user."""
    logger.info("User login called...")

    form = UserLoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash("Wrong username", "danger")
            return render_template("login.html", form=form)

        if not bcrypt.checkpw(
            form.password.data.encode("utf-8"), user.password.encode("utf-8")
        ):
            flash("Wrong password", "danger")
            return render_template("login.html", form=form)

        login_user(user, remember=form.remember.data)

        try:
            reg_event = UserEvent()
            reg_event.event_type = UserEventType.LOGIN
            reg_event.ip = request.remote_addr
            reg_event.user_id = user.id
            db.session.add(reg_event)
            db.session.commit()
        except Exception as e:
            flash(f"Error while registering user (DB query failed): {e}", "danger")
            return redirect(url_for("user.register", form=form))

        return redirect(request.args.get("next") or url_for("budget.main"))

    return render_template("login.html", form=form)


@user_app.route("/profile", methods=["GET"])
@login_required
def profile() -> str:
    """Get a profile page."""
    return render_template("profile.html", user=current_user)


@user_app.route("/logout")
@login_required
def logout() -> Response:
    """Logout current user."""
    try:
        log_out_event = UserEvent()
        log_out_event.event_type = UserEventType.LOG_OUT
        log_out_event.ip = request.remote_addr
        log_out_event.user_id = current_user.id
        db.session.add(log_out_event)
        db.session.commit()
    except Exception as e:
        flash(f"Error while logging out user (DB query failed): {e}", "danger")
    logout_user()
    flash("You have logged out", "success")
    return redirect(url_for("user.login"))
