import os

from app import MainApp
from db import DbClient

storage_path = os.path.join(os.getcwd(), '.data/sqlite/budget.db')


if __name__ == '__main__':
    db_client = DbClient(storage_path)
    MainApp(db_client).run()
