import sqlite3
from typing import Type, Iterable, Any, Tuple, List

from budget.endpoint import BaseEndpoint
from budget.models import data_schema, Model, DataModel


class SqliteEndpoint(BaseEndpoint):
    '''
    Endpoint for SQLite database
    '''

    type_mapping = {
        str: 'TEXT',
        None: 'NULL',
        int: 'INTEGER',
        float: 'REAL',
        bytes: 'BLOB',
    }

    def __init__(self, storage_path: str):
        self.__storage_path = storage_path
        self.__connection = sqlite3.connect(self.__storage_path)
        self.__create_tables()
        super().__init__()

    def insert(self, data_model: DataModel, values: List) -> List:
        statement = f'INSERT INTO {data_model.name} VALUES {values}'
        with self.__connection as conn:
            print(f'executing: {statement}')
            data = conn.execute(f'INSERT INTO ? VALUES ?', (data_model.name, values))
        return data.fetchall()

    def get(self, data_model: DataModel) -> Iterable[Model]:
        with self.__connection as conn:
            data = conn.execute(f'SELECT * FROM {data_model.name};')
        return data.fetchall()

    def update(self, data_model: DataModel, values: List) -> List:
        model_id = values[0]
        fields_set = []
        for name, value in zip(data_model.iter(), values):
            fields_set.append(f'{name} = {value}')
        fields_set = (', '.join(fields_set))
        with self.__connection as conn:
            data = conn.execute(f'UPDATE {data_model.name} SET {fields_set} WHERE id={model_id};')
        return data.fetchall()

    def delete(self, data_model: DataModel, model_id: str) -> None:
        with self.__connection as conn:
            conn.execute(f'DELETE FROM {data_model.name} WHERE id={model_id};')

    def __create_tables(self):
        tables_queries = []
        for data_model in data_schema:
            # create columns definition
            columns_definition = []
            for name, column in data_model.iter(add_field=True):
                column_definition = f'{name} '
                column_definition += f'{self.type_mapping.get(column.type, "TEXT")} '
                column_definition += 'NOT NULL ' if not column.nullable else ''
                column_definition += 'PRIMARY KEY ' if column.primary else ''
                column_definition += 'UNIQUE ' if column.unique else ''
                columns_definition.append(column_definition)
            columns_definition = ', '.join(column_definition for column_definition in columns_definition)
            # create table query
            table_name = data_model.name
            table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition}) WITHOUT ROWID;'
            tables_queries.append(table_query)
        with self.__connection as connection:
            for table_query in tables_queries:
                connection.execute(table_query)
