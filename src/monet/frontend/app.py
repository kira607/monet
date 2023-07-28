# flake8: noqa

from flask import Blueprint, render_template
from werkzeug import Response

from .controller import RootController

frontend_app = Blueprint(
    "frontend",
    __name__,
    static_folder="static",
    template_folder="templates",
    static_url_path="/static/",
)
controller = RootController()


@frontend_app.route("/")
def root() -> Response | str:
    """Get main page."""
    return render_template("pages/budget_main.html")


# @frontend_app.route("/", methods=["GET"])
# def root() -> Response | str:
#     """Get an app root."""
#     if current_user.is_authenticated():
#         return redirect(url_for("frontend.profile"))
#     return redirect(url_for("frontend.login"))


@frontend_app.route("/register", methods=["GET"])
def register() -> str:
    """Get registration page."""
    return render_template("pages/register.html")


@frontend_app.route("/login", methods=["GET"])
def login() -> str:
    """Get login page."""
    return render_template("pages/login.html")


@frontend_app.route("/profile", methods=["GET"])
def profile() -> str:
    """Get a profile page."""
    return render_template("pages/profile.html", user=None)
