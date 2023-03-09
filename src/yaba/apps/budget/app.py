from flask import Blueprint, render_template
from flask import Response, make_response
from flask_login import login_required, current_user

from .controller import BudgetController


budget_app = Blueprint(
    'budget',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/budget',
)
controller = BudgetController()


@budget_app.route('/', methods=['GET'])
@login_required
def main():
    return render_template('budget_main.html', user=current_user)


@budget_app.route('/transaction/<transaction_id>/', methods=['GET'])
def get_transaction(transaction_id: str) -> Response:
    '''
    Get a transaction by id.

    :param transaction_id: An id of a transaction.
    :return: Transaction model as dict.
    '''
    resp, code = controller.get_transaction(transaction_id)
    response = make_response(resp, code)
    response.headers['ContentType'] = 'application/json'
    return response
