from budget import Budget
from interfaces.base_interface import Interface
from .app import MainApp


class KivyInterface(Interface):
    def __init__(self, budget: Budget):
        super().__init__(budget)
        self.app = MainApp(budget)

    def run(self) -> None:
        self.app.run()
