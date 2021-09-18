from budget import Budget
from .menu import menu
from interfaces.base_interface import Interface


class Cli(Interface):
    def __init__(self, budget: Budget):
        self.budget = budget
        super().__init__(budget)

    def run(self):
        to_continue = True
        while to_continue:
            to_continue = menu(self.budget)
