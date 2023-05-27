import logging
import os

from flask import current_app
from werkzeug.local import LocalProxy


logger = LocalProxy(lambda: current_app.logger)


def configure_logger(level: str) -> None:
    '''Configure app logger.'''
    logging.basicConfig(format='{asctime} [{levelname}]: {message}', style='{', level=level or 'INFO')
