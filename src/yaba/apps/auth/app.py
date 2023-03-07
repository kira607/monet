from flask import Blueprint
from flask import render_template
from flask_login import LoginManager

from .controller import AuthController


auth_app = Blueprint(
    'auth',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/auth',
    static_url_path='/static/auth',
)
controller = AuthController()


@auth_app.route('/')
def login() -> str:
    '''Get authentication main page.'''
    return render_template('auth.html')
