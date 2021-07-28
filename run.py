import os
from interfaces.cli import Cli
from budget import Budget, CsvStorage

if __name__ == '__main__':
    path_to_storage = os.path.join(os.getcwd(), '.data/transactions.csv')
    storage = CsvStorage(path_to_storage)
    budget = Budget(storage)
    interface = Cli(budget)

    interface.run()
