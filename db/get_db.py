import os
from .db_client import DbClient

sp = os.path.join(os.getcwd(), 'db/budget.db')
# sp = './.data/sqlite/budget.db'
print(f'db file path: {sp}')
instance = DbClient(sp)

def get_db():
    return instance