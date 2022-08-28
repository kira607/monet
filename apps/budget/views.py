from flask import make_response

from .app import budget_app, controller


__version__ = '0.1'


@budget_app.route('/transaction/<id>/', methods=['GET'])
def get_transaction(id: str):
    resp, code = controller.get_transaction(id)
    response = make_response(resp, code)
    response.headers['ContentType'] = 'application/json'
    return response
