from .menu import menu
from budget.budget import Budget

class Interface:
    pass

class Cli(Interface):
    def __init__(self, budget: Budget):
        self.budget = budget

    def run(self):
        to_continue = True
        while to_continue:
            to_continue = menu(self.budget)