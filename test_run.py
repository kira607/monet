import os
from datetime import datetime
import pandas as pd
from typing import List

from pandas import DataFrame

from budget.storage.common.storage import Storage
from budget.transaction import Transaction


class TestCsvStorage(Storage):
    df = None

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.__load()
        super().__init__()

    def add(self, transaction: Transaction):
        data = transaction.dict
        index = data['transaction_id']
        del data['transaction_id']
        transaction_data_frame = DataFrame(data=data, index=[index])
        self.df = self.df.append(transaction_data_frame)
        self.__save()

    def delete(self, *, transaction_id: str = None, filters: List[filter] = None):
        self.df = self.df.drop(index=transaction_id)
        self.__save()

    def get(self, *, filters: List[filter] = None):
        print(self.df[self.df.transaction_type != float('nan')])
        # for d in self.df.iterrows():
        #     print(d, type(d), len(d), d[0], d[1], type(d[1]), sep='\n\n')
        #     break

    def __load(self):
        self.df = pd.read_csv(self.file_path, index_col=0)

    def __save(self):
        self.df.to_csv(self.file_path)


path_to_storage = os.path.join(os.getcwd(), '.data/test.csv')
storage = TestCsvStorage(path_to_storage)
# storage.add(Transaction('1', '2', 3, datetime.now()))
print(dict(Transaction('1', '2', 3, datetime.now())))
# storage.delete(transaction_id='T-1IxIed')
storage.get()
