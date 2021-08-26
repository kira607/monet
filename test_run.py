import os
import sqlite3

from budget.common import Date
from budget.endpoint import SqliteEndpoint
from budget.models import Operation, data_schema, Account
from budget.models.converter import ModelConverter, RequestType

storage_path = os.path.join(os.getcwd(), '.data/sqlite/budget.db')


def clear_db():
    conn = sqlite3.connect(storage_path)
    with conn:
        tables = conn.execute('SELECT name FROM sqlite_master WHERE type = "table";')
        tables = [name[0] for name in tables.fetchall()]
        print(f'tables to delete: {tables}')
        for table in tables:
            conn.execute(f'DROP TABLE {table};')


def main():
    # clear_db()
    endpoint = SqliteEndpoint(storage_path)
    converter = ModelConverter()
    # TODO: id generation
    operation = Operation(
        id='OPN-uibi33',
        name='some transaction',
        from_id='',
        to_id='',
        value=14000.0,
        pay_date=Date(2021, 9, 23),
        start_date=None,
        due_date=None,
        planned_value=None,
        planned=None,
        comment=None,
        tag='TAG-ihki44',
    )
    # data = converter.convert(operation, SqliteEndpoint, RequestType.INSERT)
    d = endpoint.get(data_schema.operation)
    print('All data schema:', d)
    d = endpoint.update(data_schema.operation, operation)
    print('Updated data schema:', d)
    d = endpoint.get(data_schema.operation)
    print('All data schema:', d)
    endpoint.delete(data_schema.operation, operation)
    d = endpoint.get(data_schema.operation)
    print('After delete:', d)


if __name__ == '__main__':
    main()
