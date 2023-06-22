from flask import Flask
from flask_bootstrap import Bootstrap

from monet.admin import admin
from monet.config import ConfigName, get_config
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

    with app.app_context():
        from monet.api.budget import budget_app
        from monet.api.user.app import login_manager

        app.register_blueprint(budget_app)

        from monet.frontend import frontend_app

        app.register_blueprint(frontend_app)

        from monet.api.system import system_app

        app.register_blueprint(system_app)

        from monet.api.user import user_app

        app.register_blueprint(user_app)

        app.logger.info(f"Registered blueprints: {list(app.blueprints.keys())}")

    db.init_app(app)
    app.logger.info(f"Models: {db.Model.__subclasses__()}")
    migrate.init_app(app, db)
    login_manager.init_app(app)
    admin.init_app(app)
    Bootstrap(app)

    return app


def main() -> None:
    """Run entry point."""
    app = create_app("development")
    app.run(debug=True)


if __name__ == "__main__":
    main()
