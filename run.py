import sys

sys.path.insert(1, '/home/kirill/programming/budget/')

from interfaces.cli import Cli
from budget import Budget, CsvStorage

if __name__ == '__main__':
    path_to_storage = '/home/kirill/programming/budget/storage.csv'
    storage = CsvStorage(path_to_storage)
    budget = Budget(storage)
    interface = Cli(budget)

    interface.run()
