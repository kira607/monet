from typing import Tuple

from .asset import Asset
from datetime import datetime
import random
import string


def gen_transaction_id(prefix='T-', postfix=''):
    id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    return prefix + id + postfix


class Transaction:
    transaction_id = gen_transaction_id()
    asset_from_id: Asset = None
    asset_to_id: Asset = None  # category
    value: float = 0.0
    pay_date: datetime = None
    plan_date = None
    plan_interval = None
    transaction_direction = None  # income, outcome, internal
    transaction_type = None  # planned, unplanned, ...

    def __init__(self, from_, to, value, date):
        self.asset_from_ = from_
        self.asset_to = to
        self.value = value
        self.pay_date = date

    @property
    def dict(self):
        return {
            'transaction_id': self.transaction_id,
            'asset_from_id': self.asset_from_id,
            'asset_to_id': self.asset_to,
            'value': self.value,
            'pay_date': self.pay_date,
            'plan_date': self.plan_date,
            'plan_interval': self.plan_interval,
            'transaction_direction': self.transaction_direction,
            'transaction_type': self.transaction_type,
        }

    @property
    def list(self):
        return [
            self.transaction_id,
            self.asset_from_id,
            self.asset_to,
            self.value,
            self.pay_date,
            self.plan_date,
            self.plan_interval,
            self.transaction_direction,
            self.transaction_type,
        ]

    '''
    {
    'name': '',
    'permanent': '',
    'recurring type': '',
    'plan date': '',
    'plan value': '',
    'fact value': '',
    'category': '',
    'tag': '',
    }
    '''