import os
from datetime import datetime
from functools import wraps

import pandas as pd
from typing import List
from sys import getsizeof

from pandas import DataFrame

from budget.common.utils import gen_id
from budget.storage.common.storage import Storage
from budget.transaction import Transaction, DateTime


class Field:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value if value is not None else type()


class Storable:
    def __init__(self):
        pass


class Transaction(Storable):
    id = Field(str)
    value = Field(float)


class Query:
    operations = ['==', '>', '>=', '<', '<=']

    def __init__(self):
        self.__query_data = {
        'id': None,
        'name': None,
        'from_id': None,
        'to_id': None,
        'value': None,
        'pay_date': None,
        'start_date': None,
        'due_date': None,
        'planned_value': None,
        'comment': None,
    }

    @staticmethod
    def __type_check(self, value):
        _T = Transaction.fields_types['']
        if not isinstance(value, _T):
            raise TypeError(f'type of value {value} must be {_T.__name__}, got {type(value).__name__}')

    def __operation_check(self, operation):
        if operation not in self.operations:
            raise ValueError(f'operation must be either {self.operations}, got {operation}')

    def __apply_operation(self, name): pass
    
    @property
    def pandas_query(self):
        return 0


class TestCsvTransactionStorage(Storage):
    pass


class TestCsvStorage(Storage):
    df = None

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.__load()
        super().__init__()

    def add(self, transaction: Transaction):
        while self.__is_duplicated(transaction):
            print(f'duplicate id {transaction.transaction_id}')
            transaction.transaction_id = gen_id('T-')
        transaction_data_frame = self.__transaction_to_data_frame(transaction)
        self.df = self.df.append(transaction_data_frame)
        self.__save()

    def delete(self, *, transaction_id: str = None, filters: List[filter] = None):
        self.df = self.df.drop(index=transaction_id)
        self.__save()

    def get(self, model_type: type):
        # print(self.df[self.df['value'] > 4])
        if query is None:
            return self.df
        data = self.df.query(query.pandas_query)
        transactions = None

    def update(self):
        pass

    def __load(self):
        self.df = pd.read_csv(self.file_path, index_col=0)
        print(getsizeof(self.df))

    def __save(self):
        self.df.to_csv(self.file_path)

    @staticmethod
    def __transaction_to_data_frame(transaction: Transaction) -> DataFrame:
        data = transaction.dict()
        index = data['id']
        del data['id']
        data['pay_date'] = pd.to_datetime(data['pay_date'].dt)
        return DataFrame(data=data, index=[index])

    def __is_duplicated(self, transaction):
        index = transaction.transaction_id
        try:
            other_transaction = self.get(Query().id('==', index))
        except KeyError:
            return False
        return other_transaction is not None


if __name__ == '__main__':
    path_to_storage = os.path.join(os.getcwd(), '.data/test.csv')
    storage = TestCsvStorage(path_to_storage)

    t = Transaction('1', '2', 3, datetime.now())
    print(t.dict())

    print(Transaction.value)

    # storage.get(Transaction).filter(Transaction.value > 2)
    storage.transaction.get()

    # q = Query().id('==', '123').pay_date('==', DateTime())
    # storage.add(t)
    # storage.delete(transaction_id='T-1IxIed')
    # storage.get(Query().id('==', '3'))

    # storage.get(
    #     Query()
    #     .id('>', '13')
    #     .value('==', 13)
    #     .date('>=', '13-02-1999')
    # )
