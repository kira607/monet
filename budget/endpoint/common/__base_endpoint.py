from abc import ABC, abstractmethod
from typing import List
from budget.models import Transaction


class BaseEndpoint(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add(self, _item):
        pass

    @abstractmethod
    def delete(self, _id: str = None):
        pass

    @abstractmethod
    def get(self, *, filters: List[filter]):
        pass

    @abstractmethod
    def update(self):
        pass
