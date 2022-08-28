from flask import Response, make_response

from .app import budget_app, controller


__import_me__ = None


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
