from flask import Blueprint

from .controller import SystemController


system_app = Blueprint('system', __name__, url_prefix='/system')
controller = SystemController()
