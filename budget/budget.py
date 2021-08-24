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

    @staticmethod
    def __now():
        return datetime.datetime.now().strftime('%d-%m-%Y')
