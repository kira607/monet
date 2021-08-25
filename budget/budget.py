import datetime

from budget.endpoint import BaseEndpoint


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
