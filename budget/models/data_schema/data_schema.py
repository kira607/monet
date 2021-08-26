from typing import Iterator, List, Optional

from budget.models import Account
from budget.models import Category
from budget.models import Currency
from budget.models import SubCategory
from budget.models import Tag
from budget.models import Operation
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
        except IndexError:
            self.pos = -1
            raise StopIteration

    def get(self, name: str) -> Optional[DataModel]:
        '''
        Get data model by model name

        :param name: name of the model
        :return: data model with the given name
        '''
        for model in self.pure_attrs:
            if model.name == name:
                return model
        return None

    operation = DataModel('Operation', Operation, 'OPN')
    account = DataModel('Account', Account, 'ACT')
    currency = DataModel('Currency', Currency, 'CUR')
    tag = DataModel('Tag', Tag, 'TAG')
    category = DataModel('Category', Category, 'CAT')
    sub_category = DataModel('SubCategory', SubCategory, 'SCT')


data_schema = DataSchema()
