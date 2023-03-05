import os

from .db import db
from .db import migrate


DB_DIALECT = os.environ.get('DB_DIALECT')
DB_DRIVER = os.environ.get('DB_DRIVER')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOSTNAME = os.environ.get('DB_HOSTNAME')
DB_NAME = os.environ.get('DB_NAME')
DB_URI = (
    f'{DB_DIALECT}'
    f'+{DB_DRIVER}'
    f'://{DB_USERNAME}'
    f':{DB_PASSWORD}'
    f'@{DB_HOSTNAME}'
    f'/{DB_NAME}'
)
