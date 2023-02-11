from flask import Response, current_app, make_response, request

from .app import controller, system_app


__import_me__ = None


@system_app.route('/deploy_web_hook', methods=['POST'])
def deploy_web_hook() -> Response:
    '''Trigger a web hook to pull repo code.'''
    current_app.logger.critical("Deploy request recieved. If it's valid, app will restart")
    x_hub_sig = request.headers.get('X-Hub-Signature')
    data = request.data
    resp, code = controller.deploy_web_hook(x_hub_sig, data)  # type: ignore
    response = make_response(resp, code)
    return response
