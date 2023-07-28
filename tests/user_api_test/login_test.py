"""Unit tests for api.login API endpoint."""
from http import HTTPStatus

from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy

from monet.orm.models.user import User
from monet.orm.models.user_event import UserEvent, UserEventType
from tests.utils import EMAIL, login_user, register_user

SUCCESS = "successfully logged in"
UNAUTHORIZED = "Invalid email or password"


def test_login(client: FlaskClient, db: SQLAlchemy) -> None:
    """Test successful login API request.

    Checks:
      - Response has a valid structure.
      - The database has been updated after request.
    """
    register_user(client)
    response = login_user(client)
    assert response.status_code == HTTPStatus.OK
    assert "status" in response.json and response.json["status"] == "success"
    assert "message" in response.json and response.json["message"] == SUCCESS
    assert "access_token" in response.json
    user = User.query.filter(User.email == EMAIL).first()
    assert UserEvent.query.filter(UserEvent.user_id == user.id, UserEvent.event_type == UserEventType.LOGIN).first()


def test_login_email_does_not_exist(client: FlaskClient, db: SQLAlchemy) -> None:
    """Test login API request when email does not exit.

    Checks:
      - Response has a valid structure.
    """
    response = login_user(client)
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert "message" in response.json and response.json["message"] == UNAUTHORIZED
    assert "access_token" not in response.json
