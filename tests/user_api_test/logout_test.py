"""Unit tests for api.logout API endpoint."""
from http import HTTPStatus

from flask.testing import FlaskClient
from flask_jwt_extended import decode_token
from flask_sqlalchemy import SQLAlchemy

from monet.orm.models import BlocklistToken
from tests.utils import WWW_AUTH_NO_TOKEN, login_user, logout_user, register_user

SUCCESS = "successfully logged out"
TOKEN_BLOCKLISTED = "Token has been revoked"
WWW_AUTH_BLACKLISTED_TOKEN = (
    f"{WWW_AUTH_NO_TOKEN}, " 'error="invalid_token", ' f'error_description="{TOKEN_BLOCKLISTED}"'
)


def test_logout(client: FlaskClient, db: SQLAlchemy) -> None:
    """Test successful logout API request.

    Checks:
      - Response has a valid structure.
      - User token has beed added to blocklist in the database.
    """
    register_user(client)
    response = login_user(client)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    jti = decode_token(access_token)["jti"]
    blacklist = BlocklistToken.query.all()
    assert len(blacklist) == 0

    response = logout_user(client, access_token)
    assert response.status_code == HTTPStatus.OK
    assert "status" in response.json and response.json["status"] == "success"
    assert "message" in response.json and response.json["message"] == SUCCESS
    blacklist = BlocklistToken.query.all()
    assert len(blacklist) == 1
    assert jti == blacklist[0].jti


def test_logout_token_blocklisted(client: FlaskClient, db: SQLAlchemy) -> None:
    """Test unauthorized logout API request.

    Checks:
      - Response has a valid structure.
    """
    register_user(client)
    response = login_user(client)
    assert "access_token" in response.json
    access_token = response.json["access_token"]

    response = logout_user(client, access_token)
    assert response.status_code == HTTPStatus.OK

    response = logout_user(client, access_token)
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert "message" in response.json and response.json["message"] == TOKEN_BLOCKLISTED
    assert "WWW-Authenticate" in response.headers
    assert response.headers["WWW-Authenticate"] == WWW_AUTH_BLACKLISTED_TOKEN
