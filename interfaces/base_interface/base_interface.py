from abc import ABC, abstractmethod

from budget import Budget


class Interface(ABC):
    def __init__(self, budget: Budget):
        self.budget = budget

    @abstractmethod
    def run(self) -> None:
        pass
