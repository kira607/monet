from flask import Blueprint
from flask import Response, current_app, make_response, request

from .controller import SystemController


system_app = Blueprint(
    'system',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/system',
)
controller = SystemController()


@system_app.route('/deploy_web_hook', methods=['POST'])
def deploy_web_hook() -> Response:
    '''Trigger a web hook to pull repo code.'''
    current_app.logger.critical("Deploy request recieved. If it's valid, app will restart")
    x_hub_sig = request.headers.get('X-Hub-Signature')
    data = request.data
    resp, code = controller.deploy_web_hook(x_hub_sig, data)  # type: ignore
    response = make_response(resp, code)
    return response
