from collections import Iterator
from typing import List

from ._base import Base
from .account import Account
from .currency import Currency
from .income_category import IncomeCategory
from .income_subcategory import IncomeSubcategory
from .outcome_category import OutcomeCategory
from .outcome_subcategory import OutcomeSubcategory
from .tag import Tag
from .transaction import Transaction


class Tables(Iterator):
    def __init__(self):
        self.pure_attrs: List[Base] = []
        for k, v in self.__class__.__dict__.items():
            if k[:2] != '__' and not callable(v) and k[0] != '_':
                self.pure_attrs.append(v)
        self.pos = -1

    def __next__(self):
        try:
            self.pos += 1
            return self.pure_attrs[self.pos]
        except IndexError:
            self.pos = -1
            raise StopIteration

    accounts = Account
    currencies = Currency
    income_categories = IncomeCategory
    income_subcategories = IncomeSubcategory
    outcome_categories = OutcomeCategory
    outcome_subcategories = OutcomeSubcategory
    tags = Tag
    transactions = Transaction
