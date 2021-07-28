import os
from datetime import datetime

from budget import CsvStorage
from budget.transaction import Transaction

path_to_storage = os.path.join(os.getcwd(), '.data/transactions.csv')
storage = CsvStorage(path_to_storage)
storage.add(Transaction('1', '2', 3, datetime.now()))
