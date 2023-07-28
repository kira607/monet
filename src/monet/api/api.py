"""API blueprint configuration."""
from flask import Blueprint
from flask_restx import Api

from .user import user_api

api_blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(
    api_blueprint,
    version="1.0",
    title="Monet API",
    description="An API for interacting with Monet resources",
    doc="/doc",
    authorizations=authorizations,
)

api.add_namespace(user_api, path="/user")
