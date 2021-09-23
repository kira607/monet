from budget import Budget
from budget.models import data_schema
from interfaces.base_interface import Interface
from .app import MainApp


class KivyInterface(Interface):
    def __init__(self, budget: Budget):
        super().__init__(budget)
        hello = budget.get(data_schema.operation)
        t = ''
        for hey in hello:
            t += str(hey.values) + '\n'
        self.app = MainApp(t)

    def run(self) -> None:
        self.app.run()
