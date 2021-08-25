import sqlite3
from contextlib import contextmanager
from typing import Type, Iterable, Any

from budget.endpoint import BaseEndpoint
from budget.models import data_schema, Model, Transaction


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
        tables_queries = []
        for data_model in data_schema:
            # create columns definition
            columns_definition = []
            for name, column in data_model.fields():
                column_definition = f'{name} '
                column_definition += 'NOT NULL ' if not column.nullable else ''
                column_definition += 'PRIMARY KEY ' if column.primary else ''
                column_definition += 'UNIQUE ' if column.unique else ''
                columns_definition.append(column_definition)
            columns_definition = ', '.join(column_definition for column_definition in columns_definition)
            # create table query
            table_name = data_model.name
            table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition}) WITHOUT ROWID;'
            tables_queries.append(table_query)

    @contextmanager
    def __connection(self):
        # TODO: handle exception here
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
