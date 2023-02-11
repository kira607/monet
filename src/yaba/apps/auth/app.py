from flask import Blueprint

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
