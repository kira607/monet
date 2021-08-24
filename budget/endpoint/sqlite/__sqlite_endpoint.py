from typing import List, Type, Iterable, Any

from budget.endpoint.common.__base_endpoint import BaseEndpoint
from budget.models import models_mapping
from budget.models.model import Model
from budget.models.transaction import Transaction
from contextlib import contextmanager

import sqlite3


class SqliteEndpoint(BaseEndpoint):
    def __init__(self, storage_path: str = '../../../.data/budget.db'):
        self.__storage_path = storage_path
        self.__create_tables()
        super().__init__()

    def insert(self, model: Type[Model], statement: Any) -> Model:
        pass

    def delete(self, model: Type[Model], statement: Any) -> None:
        pass

    def get(self, model: Type[Model]) -> Iterable[Model]:
        with self.__connection() as con:
            data = con.execute('SELECT * FROM Transactions;')
        return data

    def update(self, model: Type[Model], statement: Model) -> Model:
        pass

    def __create_tables(self):
        for model_type, model_name in models_mapping.items():
            pass
        columns = f'{", ".join((f"{name}, {type_}" for name, type_ in Transaction().attributes_types))}'
        transactions = (
            f'CREATE TABLE IF NOT EXISTS Transactions ({columns}) WITHOUT ROWID;'
        )

    @contextmanager
    def __connection(self):
        conn = self.sqlite_connection = sqlite3.connect(self.__storage_path)
        cursor = self.sqlite_connection.cursor()
        yield cursor
        conn.commit()
        cursor.close()
        conn.close()


if __name__ == '__main__':
    e = SqliteEndpoint()
    d = e.get(Transaction)
    print(d)
