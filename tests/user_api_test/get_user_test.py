"""Unit tests for api.get_user API endpoint."""
import time
from http import HTTPStatus

from flask import url_for
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy

from tests.utils import EMAIL, WWW_AUTH_NO_TOKEN, get_user, login_user, register_user

TOKEN_EXPIRED = "Token has expired"
WWW_AUTH_EXPIRED_TOKEN = f"{WWW_AUTH_NO_TOKEN}, " 'error="invalid_token", ' f'error_description="{TOKEN_EXPIRED}"'


def test_get_user(client: FlaskClient, db: SQLAlchemy) -> None:
    """Test successful get user API request.

    Checks:
      - Response has a valid structure.
    """
    register_user(client)
    response = login_user(client)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    response = get_user(client, access_token)
    assert response.status_code == HTTPStatus.OK
    assert "email" in response.json and response.json["email"] == EMAIL
    assert response.json.get("id") is not None


def test_get_user_no_token(client: FlaskClient, db: SQLAlchemy) -> None:
    """Test get user API request whith no token provided.

    Checks:
      - Response has a valid structure.
    """
    response = client.get(url_for("api.get_user"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert "message" in response.json and response.json["message"] == "Missing Authorization Header"
    assert "WWW-Authenticate" in response.headers
    assert response.headers["WWW-Authenticate"] == WWW_AUTH_NO_TOKEN


def test_get_user_no_header(client: FlaskClient, db: SQLAlchemy) -> None:
    """Test get user API request with no header provided.

    Checks:
    - Response has a valid structure.
    """
    register_user(client)
    login_user(client)
    response = client.get(url_for("api.get_user"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert "message" in response.json and response.json["message"] == "Missing Authorization Header"
    assert "WWW-Authenticate" in response.headers
    assert response.headers["WWW-Authenticate"] == WWW_AUTH_NO_TOKEN


def test_auth_user_expired_token(client: FlaskClient, db: SQLAlchemy) -> None:
    """Test get user API request when token has expired.

    Checks:
      - Response has a valid structure.
    """
    register_user(client)
    response = login_user(client)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    time.sleep(6)  # TODO: come up with something to not have this time.sleep()
    response = get_user(client, access_token)
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert "message" in response.json and response.json["message"] == TOKEN_EXPIRED
    assert "WWW-Authenticate" in response.headers
    assert response.headers["WWW-Authenticate"] == WWW_AUTH_EXPIRED_TOKEN
