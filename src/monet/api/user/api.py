from http import HTTPStatus

import bcrypt
from flask import Response, current_app, jsonify, make_response, request
from flask.typing import ResponseReturnValue
from flask_jwt_extended import create_access_token, current_user, get_jwt, jwt_required
from flask_restx import Namespace, Resource, abort

from monet.logger import logger
from monet.orm import db
from monet.orm.models import BlocklistToken, User, UserEvent, UserEventType
from monet.utils.datetime_utils import Timespan

from .models import user_model
from .request_parsers import auth_request_parser

user_api = Namespace(
    name="user",
    description="An api for user interaction: register, login, get info, etc.",
    validate=True,
)

user_api.add_model(user_model.name, user_model)


def create_authentication_successful_response(token: str, status_code: HTTPStatus, message: str) -> Response:
    """Create a successful response after user has authenticated.

    :param str token: A new JWT token to put in a response.
    :param HTTPStatus status_code: Response status code.
    :param str message: Response message

    :return: A successful authentication response
    :rtype: :class:`flask.Response`.
    """
    response = jsonify(
        status="success",
        message=message,
        access_token=token,
        token_type="bearer",
        expires_in=Timespan.from_timedelta(current_app.config["JWT_ACCESS_TOKEN_EXPIRES"]).total_seconds,
    )
    response.status_code = status_code
    response.headers["Cache-Control"] = "no-store"
    response.headers["Pragma"] = "no-cache"
    return response


@user_api.route("/register", endpoint="register")
class RegisterUser(Resource):
    """Handles HTTP requests to URL: /api/v1/user/register."""

    @user_api.expect(auth_request_parser)
    @user_api.response(int(HTTPStatus.CREATED), "New user was successfully created.")
    @user_api.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
    @user_api.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @user_api.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self) -> Response:
        """Register a new user and return an access token."""
        request_data = auth_request_parser.parse_args()
        email = request_data.get("email")
        password = request_data.get("password")

        if User.query.filter_by(email=email).first():
            abort(HTTPStatus.CONFLICT, f"{email} is already registered", status="fail")

        new_user = User()
        new_user.email = email
        new_user.password = bcrypt.hashpw(  # type: ignore
            password.encode("utf-8"),
            bcrypt.gensalt(),
        )

        reg_event = UserEvent()
        reg_event.event_type = UserEventType.REGISTER
        reg_event.ip = request.remote_addr

        new_user.events.append(reg_event)

        db.session.add(new_user)
        db.session.commit()

        access_token = create_access_token(identity=new_user)
        return create_authentication_successful_response(access_token, HTTPStatus.CREATED, "successfully registered")


@user_api.route("/login", endpoint="login")
class LoginUser(Resource):
    """Handles HTTP requests to URL: /api/v1/user/login."""

    @user_api.expect(auth_request_parser)
    @user_api.response(int(HTTPStatus.OK), "Login succeeded.")
    @user_api.response(int(HTTPStatus.UNAUTHORIZED), "Invalid email or password")
    @user_api.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @user_api.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self) -> Response:
        """Authenticate an existing user and return an access token."""
        request_data = auth_request_parser.parse_args()
        email = request_data.get("email")
        password = request_data.get("password")
        user = User.query.filter_by(email=email).first()

        if not user:
            logger.error(f"user: {email} does not exist")
            abort(HTTPStatus.UNAUTHORIZED, "Invalid email or password", status="fail")

        user_password = bytes(user.password, "utf-8") if isinstance(user.password, str) else user.password
        input_password = bytes(password, "utf-8")

        if not bcrypt.checkpw(input_password, user_password):
            logger.error(f"user: {email} invalid password")
            abort(HTTPStatus.UNAUTHORIZED, "Invalid email or password", status="fail")

        login_event = UserEvent()
        login_event.event_type = UserEventType.LOGIN
        login_event.ip = request.remote_addr
        user.events.append(login_event)

        db.session.add(user)
        db.session.commit()

        access_token = create_access_token(identity=user)
        return create_authentication_successful_response(access_token, HTTPStatus.OK, "successfully logged in")


@user_api.route("/", endpoint="get_user")
class GetUser(Resource):
    """Handles HTTP requests to URL: /api/v1/user."""

    @user_api.doc(security="Bearer")
    @user_api.response(int(HTTPStatus.OK), "Token is currently valid.", user_model)
    @user_api.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @user_api.response(int(HTTPStatus.UNAUTHORIZED), "Token is invalid or expired.")
    @user_api.marshal_with(user_model)
    @jwt_required()
    def get(self) -> User:
        """Validate access token and return user info."""
        return current_user


@user_api.route("/logout", endpoint="logout")
class LogoutUser(Resource):
    """Handles HTTP requests to URL: /api/v1/user/logout."""

    @user_api.doc(security="Bearer")
    @user_api.response(int(HTTPStatus.OK), "Logged out successfully. Token is no longer valid.")
    @user_api.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @user_api.response(int(HTTPStatus.UNAUTHORIZED), "Token is invalid or expired.")
    @user_api.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @jwt_required()
    def post(self) -> ResponseReturnValue:
        """Deauthenticate current user and add their token to blacklist."""
        jti = get_jwt()["jti"]
        db.session.add(BlocklistToken(jti=jti))
        db.session.commit()
        return make_response(jsonify({"status": "success", "message": "successfully logged out"}), HTTPStatus.OK)
