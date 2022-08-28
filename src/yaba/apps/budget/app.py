from flask import Blueprint

from .controller import BudgetController


budget_app = Blueprint('budget', __name__, static_folder='static', template_folder='templates', url_prefix='/budget')
controller = BudgetController()
