from app import MainApp
from db import get_db


if __name__ == '__main__':
    db_client = get_db()
    MainApp(db_client).run()
