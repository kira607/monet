from budget.storage.common.storage import Storage
from budget.transaction import Transaction
import datetime

class Budget:
    def __init__(self, storage: Storage):
        self.storage = storage

    def add_transaction(self, from_, to, value):
        transaction = Transaction(from_, to, value, self.__now())
        self.storage.save(transaction)
        return transaction

    @staticmethod
    def __now():
        return datetime.datetime.now()