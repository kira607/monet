from typing import List

from pandas import DataFrame

from budget.models.transaction import Transaction
from budget.endpoint.common.__base_endpoint import BaseEndpoint
import pandas as pd


class CsvEndpoint(BaseEndpoint):
    df = None

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.__load()
        print(self.df.head())
        super().__init__()

    def add(self, transaction: Transaction):
        transaction_data_frame = DataFrame(data=transaction.dict, index=[transaction.transaction_id])
        self.df = self.df.append(transaction_data_frame)
        self.__save()

    def delete(self, *, transaction_id: str = None, filters: List[filter] = None):
        pass

    def get(self, *, filters: List[filter]):
        pass

    def __load(self):
        self.df = pd.read_csv(self.file_path)

    def __save(self):
        self.df.to_csv(self.file_path)
