from abc import ABC, abstractmethod
from typing import List
from budget.models.transaction import Transaction


class BaseEndpoint(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add(self, transaction: Transaction):
        pass

    @abstractmethod
    def delete(self, *, transaction_id: str = None, filters: List[filter] = None):
        pass

    @abstractmethod
    def get(self, *, filters: List[filter]):
        pass
