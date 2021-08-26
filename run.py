from budget import Budget
from config import Interface, Storage, storage_path

if __name__ == '__main__':
    storage = Storage(storage_path)
    budget = Budget(storage)
    interface = Interface(budget)
    interface.run()
