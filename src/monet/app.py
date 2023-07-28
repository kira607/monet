from flask import Flask

from monet.admin import admin
from monet.config import ConfigName, get_config
from monet.jwt import jwt
from monet.logger import configure_logger
from monet.orm import db, migrate


def create_app(environment_name: ConfigName) -> Flask:
    """
    Create a new flask app.

    :return: A flask app.
    """
    app = Flask(__name__)

    config = get_config(environment_name)
    app.config.from_object(config)

    configure_logger(app.config["LOGGING_LEVEL"])
    app.logger.info(f"Configured app for '{environment_name}'")

    with app.app_context():
        from monet.api import api_blueprint

        app.register_blueprint(api_blueprint)

    app.logger.info(f"Registered blueprints: {list(app.blueprints.keys())}")

    db.init_app(app)
    app.logger.info(f"Models: {db.Model.__subclasses__()}")
    migrate.init_app(app, db)
    admin.init_app(app)
    jwt.init_app(app)

    return app
