from typing import List
from budget.transaction import Transaction
from budget.storage.common.storage import Storage
import pandas as pd


class CsvStorage(Storage):
    df = None

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.__load()
        super().__init__()

    def add(self, transaction: Transaction):
        t = transaction.dict()
        self.df = self.df.append(transaction.dict(), ignore_index=True)
        self.__save()

    def delete(self, *, transaction_id: str = None, filters: List[filter] = []):
        pass

    def get(self, *, filters: List[filter]):
        pass

    def __load(self):
        self.df = pd.read_csv(self.file_path)

    def __save(self):
        self.df.to_csv(self.file_path)
