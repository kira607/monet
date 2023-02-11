from flask import Flask

from yaba.apps import auth_app
from yaba.apps import budget_app
from yaba.apps import system_app


def create_app() -> Flask:
    '''
    Create a new flask app.

    :return: A flask app.
    '''
    new_app = Flask(__name__)
    new_app.register_blueprint(budget_app)
    new_app.register_blueprint(auth_app)
    new_app.register_blueprint(system_app)
    return new_app


def main() -> None:
    '''Run entry point.'''
    app = create_app()
    app.run()


if __name__ == '__main__':
    main()
