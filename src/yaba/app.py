import os

from flask import Flask

from yaba.apps.budget import budget_app
from yaba.apps.root import root_app
from yaba.apps.system import system_app
from yaba.apps.user import user_app
from yaba.apps.user.app import login_manager
from yaba.logger import configure_logger
from yaba.orm import DB_URI, db, migrate


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

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    return app


def main() -> None:
    '''Run entry point.'''
    app = create_app()
    app.run(debug=True)


if __name__ == '__main__':
    main()

