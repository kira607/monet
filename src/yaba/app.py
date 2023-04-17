from flask import Flask

from yaba.admin import admin
from yaba.apps.budget import budget_app
from yaba.apps.root import root_app
from yaba.apps.system import system_app
from yaba.apps.user import user_app
from yaba.apps.user.app import login_manager
from yaba.config import YabaConfig
from yaba.logger import configure_logger
from yaba.orm import db, migrate


def create_app() -> Flask:
    '''
    Create a new flask app.

    :return: A flask app.
    '''
    configure_logger()
    app = Flask(__name__)
    app.register_blueprint(user_app)
    app.register_blueprint(budget_app)
    app.register_blueprint(root_app)
    app.register_blueprint(system_app)
    app.logger.info(f'Registered blueprints: {list(app.blueprints.keys())}')

    config = YabaConfig()
    app.logger.info(f'Loaded config: {config}')
    app.config.from_object(config)

    db.init_app(app)
    app.logger.info(f'Models: {db.Model.__subclasses__()}')
    migrate.init_app(app, db)
    login_manager.init_app(app)
    admin.init_app(app)

    return app


def main() -> None:
    '''Run entry point.'''
    app = create_app()
    app.run(debug=True)


if __name__ == '__main__':
    main()
