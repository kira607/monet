import os

from budget import Budget
from budget.endpoint import SqliteEndpoint
from interfaces import KivyInterface

storage_path = os.path.join(os.getcwd(), '.data/sqlite/budget.db')
Storage = SqliteEndpoint
Interface = KivyInterface

if __name__ == '__main__':
    storage = Storage(storage_path)
    budget = Budget(storage)
    interface = Interface(budget)
    interface.run()
