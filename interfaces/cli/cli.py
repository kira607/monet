from menu import menu
from budget import Budget
from budget.storage import CsvStorage

if __name__ == '__main__':
    path_to_storage = '/home/kirill/programming/budget-app/storage.csv'
    storage = CsvStorage(path_to_storage)
    budget = Budget(storage)

    to_continue = True
    while to_continue:
        to_continue = menu(Budget)