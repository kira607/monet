from flask import Flask

from yaba.apps.auth import auth_app
from yaba.apps.budget import budget_app


def create_app() -> Flask:
    '''
    Create a new flask app.

    :return: A flask app.
    '''
    new_app = Flask(__name__)
    new_app.register_blueprint(budget_app)
    new_app.register_blueprint(auth_app)
    return new_app


def main() -> None:
    '''Run entry point.'''
    app = create_app()
    app.run()


if __name__ == '__main__':
    main()
