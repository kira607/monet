import os
from datetime import datetime
import pandas as pd
from typing import List

from pandas import DataFrame

from budget.common.utils import gen_id
from budget.endpoint.common.__base_endpoint import BaseEndpoint
from budget.models.operation import Operation


class Query:
    def __init__(
            self,
            *,
            transaction_id=None,
            asset_from_id=None,
            asset_to_id=None,
            value=None,
            pay_date=None,
            start_date=None,
            due_date=None,
    ):
        pass

    @property
    def pandas_query(self):
        return 0


class TestCsvEndpoint(BaseEndpoint):
    df = None

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.__load()
        super().__init__()

    def add(self, transaction: Operation):
        while self.__is_duplicated(transaction):
            print(f'duplicate id {transaction.transaction_id}')
            transaction.transaction_id = gen_id('T-')
        transaction_data_frame = self.__transaction_to_data_frame(transaction)
        self.df = self.df.append(transaction_data_frame)
        self.__save()

    def delete(self, *, transaction_id: str = None, filters: List[filter] = None):
        self.df = self.df.drop(index=transaction_id)
        self.__save()

    def get(self, query: Query = None):
        # print(self.df[self.df['value'] > 4])
        if query is None:
            return self.df
        pass

    def __load(self):
        self.df = pd.read_csv(self.file_path, index_col=0)

    def __save(self):
        self.df.to_csv(self.file_path)

    @staticmethod
    def __transaction_to_data_frame(transaction: Operation) -> DataFrame:
        data = transaction.dict
        index = data['transaction_id']
        del data['transaction_id']
        data['pay_date'] = pd.to_datetime(data['pay_date'])
        return DataFrame(data=data, index=[index])

    def __is_duplicated(self, transaction):
        index = transaction.transaction_id
        try:
            other_transaction = self.get(Query(transaction_id=f'=={index}'))
        except KeyError:
            return False
        return other_transaction is not None


path_to_storage = os.path.join(os.getcwd(), '.data/test.csv')
storage = TestCsvEndpoint(path_to_storage)
t = Operation('1', '2', 3, datetime.now().strftime('%d-%m-%Y'))
storage.add(t)
print(t.plan_value)
# storage.delete(transaction_id='T-1IxIed')
storage.get()