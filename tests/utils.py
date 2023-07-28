"""Some useful utilities for tests."""

from flask import url_for
from flask.testing import FlaskClient
from werkzeug.test import TestResponse

EMAIL = "example@example.com"
PASSWORD = "test-test"

BAD_REQUEST = "Input payload validation failed"
UNAUTHORIZED = "Unauthorized"
FORBIDDEN = "You are not an administrator"
WWW_AUTH_NO_TOKEN = 'Bearer realm="registered_users@mydomain.com"'


def register_user(test_client: FlaskClient, email: str = EMAIL, password: str = PASSWORD) -> TestResponse:
    """Make an API call to register a user.

    This will create a new user in the test database,
    which can be used for further testing.

    :param FlaskClient test_client: Testing flask client.
    :param str, optional email: User email, defaults to EMAIL
    :param str, optional password: User password, defaults to PASSWORD

    :return: App response
    :rtype: TestResponse
    """
    return test_client.post(
        url_for("api.register"),
        data=f"email={email}&password={password}",
        content_type="application/x-www-form-urlencoded",
    )


def login_user(test_client: FlaskClient, email: str = EMAIL, password: str = PASSWORD) -> TestResponse:
    """Make an API call to log in a user.

    :param FlaskClient test_client: Testing Flask client
    :param str, optional email: User email, defaults to EMAIL
    :param str, optional password: User password, defaults to PASSWORD

    :return: App response.
    :rtype: TestResponse
    """
    return test_client.post(
        url_for("api.login"),
        data=f"email={email}&password={password}",
        content_type="application/x-www-form-urlencoded",
    )


def get_user(test_client: FlaskClient, access_token: str) -> TestResponse:
    """Make an API call to get a user using access_token.

    :param FlaskClient test_client: Testing Flask client.
    :param str access_token: Current user access token.

    :return: App response.
    :rtype: TestResponse
    """
    return test_client.get(url_for("api.get_user"), headers={"Authorization": f"Bearer {access_token}"})


def logout_user(test_client: FlaskClient, access_token: str) -> TestResponse:
    """Make an API call to log out current user.

    :param FlaskClient test_client: Testing Flask client.
    :param str access_token: Current user access token.

    :return: App response.
    :rtype: TestResponse
    """
    return test_client.post(url_for("api.logout"), headers={"Authorization": f"Bearer {access_token}"})
