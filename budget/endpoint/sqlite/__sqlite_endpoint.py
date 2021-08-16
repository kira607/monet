from typing import List

from budget.endpoint.common.__base_endpoint import BaseEndpoint
from budget.models.transaction import Transaction


class SqliteEndpoint(BaseEndpoint):
    def __init__(self, storage_path):
        super().__init__()

    def add(self, transaction: Transaction):
        pass

    def delete(self, *, transaction_id: str = None, filters: List[filter] = None):
        pass

    def get(self, *, filters: List[filter]):
        pass
