from budget.endpoint.common.__base_endpoint import BaseEndpoint
from budget.models.transaction import Transaction
import datetime


class Budget:
    '''
    Here will take place all
    planning, filtering, editing, defaulting, etc.
    '''
    def __init__(self, endpoint: BaseEndpoint):
        self.endpoint = endpoint

    def add_transaction(self, from_, to, value):
        transaction = Transaction(from_, to, value, self.__now())
        self.endpoint.add(transaction)
        return transaction

    @staticmethod
    def __now():
        return datetime.datetime.now().strftime('%d-%m-%Y')
