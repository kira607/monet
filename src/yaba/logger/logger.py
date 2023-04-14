import logging
import os

from werkzeug.local import LocalProxy
from flask import current_app


logger = LocalProxy(lambda: current_app.logger)


def configure_logger() -> None:
    '''Configure app logger.'''
    logging.basicConfig(format='{asctime} [{levelname}]: {message}', style='{', level=os.getenv('LOGGING_LEVEL'))
