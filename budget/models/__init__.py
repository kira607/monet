from typing import Type, Iterator

from .account import Account
from .category import Category
from .currency import Currency
from .model import Model
from .subcategory import SubCategory
from .tag import Tag
from .transaction import Transaction

models_mapping = {
    Account: 'Account',
    Category: 'Category',
    Currency: 'Currency',
    SubCategory: 'SubCategory',
    Tag: 'Tag',
    Transaction: 'Transaction',
}

prefix_mapping = {
    'TRN': Transaction,
    'ACT': Account,
    'CUR': Currency,
    'TAG': Tag,
    'CAT': Category,
    'SCT': SubCategory,
}


class DataModel:
    name: str
    model: Type[Model]
    id_prefix: str

    def __init__(self, name: str, model: Type[Model], prefix: str):
        self.name = name
        self.model = model
        self.id_prefix = prefix


class DataSchema(Iterator):
    def __iter__(self):
        return self

    def __init__(self):
        self.pure_attrs = []
        for k, v in self.__class__.__dict__.items():
            if k[:2] != '__' and not callable(v) and k[0] != '_':
                self.pure_attrs.append((v.model, v.id_prefix))
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
    subCategory = DataModel('SubCategory', SubCategory, 'SCT')


data_schema = DataSchema()

