"""Unit tests for api.register API endpoint."""
from http import HTTPStatus

from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy

from monet.orm.models import User
from monet.orm.models.user_event import UserEventType
from tests.utils import EMAIL, register_user

SUCCESS = "successfully registered"


def test_user_register(client: FlaskClient, db: SQLAlchemy) -> None:
    """Test successful registration API request.

    Checks:
      - Response has a valid structure
      - The database has been updated after request.
    """
    response = register_user(client)
    assert response.status_code == HTTPStatus.CREATED
    assert "status" in response.json and response.json["status"] == "success"
    assert "message" in response.json and response.json["message"] == SUCCESS
    assert "token_type" in response.json and response.json["token_type"] == "bearer"
    assert "expires_in" in response.json and response.json["expires_in"] == 5
    assert "access_token" in response.json
    user = User.query.filter(User.email == EMAIL).first()
    assert user
    login_event = user.events[0]
    assert login_event and login_event.event_type == UserEventType.REGISTER
