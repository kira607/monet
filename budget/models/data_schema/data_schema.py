from typing import Iterator, List

from budget.models import Account
from budget.models import Category
from budget.models import Currency
from budget.models import SubCategory
from budget.models import Tag
from budget.models import Transaction
from budget.models.data_schema import DataModel


class DataSchema(Iterator):
    def __iter__(self):
        return self

    def __init__(self):
        self.pure_attrs: List[DataModel] = []
        for k, v in self.__class__.__dict__.items():
            if k[:2] != '__' and not callable(v) and k[0] != '_':
                self.pure_attrs.append(v)
        self.pos = -1

    def __next__(self):
        try:
            self.pos += 1
            return self.pure_attrs[self.pos]
        except IndexError as e:
            self.pos = -1
            raise StopIteration

    transaction = DataModel('Transaction', Transaction, 'TRN')
    account = DataModel('Account', Account, 'ACT')
    currency = DataModel('Currency', Currency, 'CUR')
    tag = DataModel('Tag', Tag, 'TAG')
    category = DataModel('Category', Category, 'CAT')
    sub_category = DataModel('SubCategory', SubCategory, 'SCT')


data_schema = DataSchema()
