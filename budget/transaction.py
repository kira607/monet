from datetime import datetime

from .asset import Asset
from .common.utils import gen_id


transaction_conf = {
    'transaction_id': str,
    'asset_from_id': str,
    'asset_to_id': str,
    'value': float,
    'plan_value': float,
    'pay_date': datetime,
    'start_date': datetime,
    'due_date': datetime,
}


class Transaction:
    transaction_id = gen_id('T-')
    asset_from_id: Asset = None
    asset_to_id: Asset = None  # category
    value: float = 0.0
    pay_date: datetime = None
    start_date = None
    due_date = None

    def __init__(self, from_, to, value, date):
        self.asset_from_id = from_
        self.asset_to_id = to
        self.value = value
        self.pay_date = date
        setattr(self, 'plan_value', 4)

    @property
    def dict(self):
        return {
            'transaction_id': self.transaction_id,
            'asset_from_id': self.asset_from_id,
            'asset_to_id': self.asset_to_id,
            'value': self.value,
            'pay_date': self.pay_date,
            'start_date': self.start_date,
            'due_date': self.due_date,
        }

    @property
    def list(self):
        return (
            self.transaction_id,
            self.asset_from_id,
            self.asset_to_id,
            self.value,
            self.pay_date,
            self.start_date,
            self.due_date,
        )