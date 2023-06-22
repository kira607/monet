from flask import Blueprint, render_template
from flask_login import current_user, login_required
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
    """Get authentication main page."""
    return render_template("pages/budget_main.html")


@frontend_app.route("/profile", methods=["GET"])
@login_required
def profile() -> str:
    """Get a profile page."""
    return render_template("pages/profile.html", user=current_user)
