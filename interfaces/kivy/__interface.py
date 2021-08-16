from budget import Budget
from .__app import MyApp


class KivyInterface:
    def __init__(self, budget: Budget):
        self.budget = budget
        self.app = MyApp()

    def run(self) -> None:
        self.app.run()
