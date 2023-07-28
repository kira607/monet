"""A Flak-JWT-Extended extention initialization."""

from flask.typing import ResponseReturnValue
from flask_jwt_extended import JWTManager
from flask_jwt_extended.default_callbacks import (
    default_expired_token_callback,
    default_revoked_token_callback,
    default_unauthorized_callback,
)

from monet.orm import db
from monet.orm.models import BlocklistToken, User

jwt = JWTManager()


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(user: User) -> int:
    """Get the identity of the user."""
    return user.id


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header: dict, jwt_data: dict) -> User:
    """Get the user using jwt data."""
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


@jwt.expired_token_loader
def expired_token_callback(jwt_header: dict, jwt_payload: dict) -> ResponseReturnValue:
    """Get a response when a token has expired."""
    response, code = default_expired_token_callback(jwt_header, jwt_payload)  # type: ignore
    response.headers["WWW-Authenticate"] = (  # type: ignore
        'Bearer realm="registered_users@mydomain.com", '
        'error="invalid_token", '
        'error_description="Token has expired"'
    )
    return response, code  # type: ignore


@jwt.unauthorized_loader
def unauthorized_callback(message: str) -> ResponseReturnValue:
    """Get a response when a token is not present."""
    response, code = default_unauthorized_callback(message)  # type: ignore
    response.headers["WWW-Authenticate"] = 'Bearer realm="registered_users@mydomain.com"'  # type: ignore
    return response, code  # type: ignore


# Callback function to check if a JWT exists in the database blocklist
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header: dict, jwt_payload: dict) -> bool:
    """Check if token has been revoked.

    :param dict jwt_header: JWT header
    :param dict jwt_payload: JWT payload

    :return: Whether token has been revoked or not.
    :rtype: bool
    """
    jti = jwt_payload["jti"]
    token = db.session.query(BlocklistToken.id).filter_by(jti=jti).scalar()

    return token is not None


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header: dict, jwt_payload: dict) -> ResponseReturnValue:
    """Get a response when a revoked token is encountered."""
    response, code = default_revoked_token_callback(jwt_header, jwt_payload)  # type: ignore
    response.headers["WWW-Authenticate"] = (  # type: ignore
        'Bearer realm="registered_users@mydomain.com", '
        'error="invalid_token", '
        'error_description="Token has been revoked"'
    )
    return response, code  # type: ignore
