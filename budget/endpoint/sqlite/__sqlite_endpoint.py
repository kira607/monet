import sqlite3
from typing import Type, Iterable, Any, Tuple, List

from budget.common import Date
from budget.endpoint import BaseEndpoint
from budget.models import data_schema, Model, DataModel


class SqliteEndpoint(BaseEndpoint):
    '''
    Endpoint for SQLite database
    '''

    type_definition_mapping = {
        str: 'TEXT',
        None: 'NULL',
        int: 'INTEGER',
        float: 'REAL',
        bytes: 'BLOB',
    }

    cast_mapping = {
        Date: str,
    }

    def __init__(self, storage_path: str):
        self.__storage_path = storage_path
        self.__connection = sqlite3.connect(self.__storage_path)
        self.__create_tables()
        super().__init__()

    def insert(self, data_model: DataModel, data: Model) -> List[Tuple]:
        values = self.__get_values(data)
        sql = f'INSERT INTO {data_model.name} VALUES ({",".join(("?" for _ in range(data_model.columns_num)))})'
        with self.__connection as conn:
            conn.execute(sql, values)
        return self.get(data_model, id=data.id)

    def get(self, data_model: DataModel, **kwargs) -> List[Tuple]:
        where = []
        for k, v in kwargs.items():
            if k in (n[0] for n in data_model.iter()):
                v = self.__cast_value(v, True)
                where.append(f'{k}={v}')
        sql = f'SELECT * FROM {data_model.name}'
        if len(where) > 0:
            where = ', '.join(where)
            sql += f' WHERE {where}'
        sql += ';'
        with self.__connection as conn:
            data = conn.execute(sql)
        return data.fetchall()

    def update(self, data_model: DataModel, data: Model) -> List[Tuple]:
        update_string = self.__get_update_string(data_model, data)
        placeholders = (data.id,)
        sql = f'UPDATE {data_model.name} SET {update_string} WHERE id=?;'
        with self.__connection as conn:
            conn.execute(sql, placeholders)
        return self.get(data_model, id=data.id)

    def delete(self, data_model: DataModel, data: Model) -> None:
        with self.__connection as conn:
            conn.execute(f'DELETE FROM {data_model.name} WHERE id=?;', (data.id,))

    def __create_tables(self):
        tables_queries = []
        for data_model in data_schema:
            # create columns definition
            columns_definition = []
            for name, column in data_model.iter(add_field=True):
                column_definition = f'{name} '
                column_definition += f'{self.type_definition_mapping.get(column.type, "TEXT")} '
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

    def __get_values(self, model: Model) -> List[Any]:
        '''
        Get values of the model, each type casted to type acceptable for sqlite.

        acceptable types are decentralized so return type hint is Any for now

        :param Model model: model which values should be casted
        :return: list of values, casted to type acceptable for sqlite
        '''
        values = []
        for _, value in model.values:
            value = self.__cast_value(value)
            values.append(value)
        return values

    def __cast_value(self, value: Any, query_string: bool = False):
        cast = self.cast_mapping.get(type(value), None)
        if cast is not None:
            value = cast(value)
        if query_string:
            if isinstance(value, str):
                value = f'"{value}"'
            if value is None:
                value = "NULL"
        return value

    def __get_update_string(self, data_model: DataModel, model: Model) -> str:
        fields_set = []
        for name, value in zip(data_model.iter(), self.__get_values(model)):
            name = name[0]
            value = self.__cast_value(value, True)
            fields_set.append(f'{name}={value}')
        return ', '.join(fields_set)
