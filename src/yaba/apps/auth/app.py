from flask import Blueprint

from .controller import AuthController


auth_app = Blueprint('auth', __name__, static_folder='static', template_folder='templates', url_prefix='/auth')
controller = AuthController()
