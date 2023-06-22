from flask import Flask
from flask_bootstrap import Bootstrap

from yaba.admin import admin
from yaba.config import Config
from yaba.logger import configure_logger
from yaba.orm import db, migrate


def create_app() -> Flask:
    """
    Create a new flask app.

    :return: A flask app.
    """
    app = Flask(__name__)

    config = Config()
    app.config.from_object(config)
    app.config.from_envvar("CONFIG_EXT", silent=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f'{app.config["DB_DIALECT"]}'
        f'+{app.config["DB_DRIVER"]}'
        f'://{app.config["DB_USERNAME"]}'
        f':{app.config["DB_PASSWORD"]}'
        f'@{app.config["DB_HOSTNAME"]}'
        f'/{app.config["DB_NAME"]}'
    )

    configure_logger(app.config["LOGGING_LEVEL"])

    with app.app_context():
        from yaba.api.budget import budget_app
        from yaba.api.user.app import login_manager

        app.register_blueprint(budget_app)

        from yaba.frontend import frontend_app

        app.register_blueprint(frontend_app)

        from yaba.api.system import system_app

        app.register_blueprint(system_app)

        from yaba.api.user import user_app

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
    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
