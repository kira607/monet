import os

from interfaces.kivy import KivyInterface as Interface
from budget.endpoint.sqlite import SqliteEndpoint as Storage

storage_path = os.path.join(os.getcwd(), '.data/sqlite')
