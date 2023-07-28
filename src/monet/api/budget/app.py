from flask import Blueprint, Response, make_response

budget_app = Blueprint(
    "budget",
    __name__,
    static_folder="static",
    template_folder="templates",
    url_prefix="/budget",
)


@budget_app.route("/transaction/<transaction_id>/", methods=["GET"])
def get_transaction(transaction_id: str) -> Response:
    """
    Get a transaction by id.

    :param transaction_id: An id of a transaction.
    :return: Transaction model as dict.
    """
    resp, code = {"id": transaction_id, "value": 100}, 200
    response = make_response(resp, code)
    response.headers["ContentType"] = "application/json"
    return response
