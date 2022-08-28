from datetime import datetime
from enum import Enum


class TransactionType(Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'
    TRANSFER = 'transfer'


class BudgetController:
    def get_transaction(self, id: str):
        return {
            'id': id,
            'label': 'Bought some carrots)))',
            'value': 44.98,
            'date': datetime(2022, 7, 14),
            'tags': ['Healthy-99kfG1'],
            'type': TransactionType.OUTCOME.value,
            'source': 'Cash-kkcQx9',
            'destination': 'Food-QQpf98',
        }, 200

    def insert_transaction(self, request):
        pass
