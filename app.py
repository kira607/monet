from flask import Flask

from apps.budget import budget_app


def create_app() -> Flask:
    new_app = Flask(__name__)
    new_app.register_blueprint(budget_app)
    return new_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
