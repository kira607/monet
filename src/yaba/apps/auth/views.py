from flask import render_template

from .app import auth_app


__import_me__ = None


@auth_app.route('/')
def auth_main() -> str:
    '''Get authentication main page.'''
    return render_template('auth.html')
