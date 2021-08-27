import os
import sqlite3

from budget import Budget
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
    budget = Budget(endpoint)
    print(budget.get(data_schema.operation))

    # budget.add(data_schema.operation, name='carrots', from_id='', to_id='', value=32.0)


if __name__ == '__main__':
    main()
