from flask import Blueprint

from .controller import BudgetController


budget_app = Blueprint('budget', __name__)
controller = BudgetController()
