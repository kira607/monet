from datetime import datetime
from enum import Enum
from typing import Any, Dict, Tuple

from flask import Request


class TransactionType(Enum):
    '''A transaction type enum.'''

    INCOME = 'income'
    OUTCOME = 'outcome'
    TRANSFER = 'transfer'


class BudgetController:
    '''A controller for budget app.'''

    def get_transaction(self, transaction_id: str) -> Tuple[Dict[str, Any], int]:
        '''
        Get a transaction by id.

        :param transaction_id: id of a transaction to get.
        '''
        return {
            'id': transaction_id,
            'label': 'Bought some carrots)))',
            'value': 44.98,
            'date': datetime(2022, 7, 14),
            'tags': ['Healthy-99kfG1'],
            'type': TransactionType.OUTCOME.value,
            'source': 'Cash-kkcQx9',
            'destination': 'Food-QQpf98',
        }, 200

    def insert_transaction(self, request: Request) -> None:
        '''
        Insert a new transaction.

        :param request: transaction data
        :type request: Request
        :return: None
        :rtype: NoneType
        '''
        pass
