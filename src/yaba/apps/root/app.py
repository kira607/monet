from flask import Blueprint, redirect, url_for, Response

from .controller import RootController

root_app = Blueprint(
    'root',
    __name__,
    static_folder='static',
    template_folder='templates',
    # url_prefix='/root',
    static_url_path='/static/root',
)
controller = RootController()


@root_app.route('/')
def root() -> Response:
    '''Get authentication main page.'''
    return redirect(url_for('budget.main'))
