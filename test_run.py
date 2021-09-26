import os

from budget.endpoint.sqlite.sqlite_endpoint_v2 import SqliteEndpoint
from budget.models2 import Tables, Transaction

storage_path = os.path.join(os.getcwd(), '.data/sqlite/budget.db')


def main():
    endpoint = SqliteEndpoint(storage_path)
    t = endpoint.insert(Tables.transactions, Transaction(id='kdkdkd', name='carrot'))
    print(t, type(t), t.name)
    t = endpoint.get(Tables.transactions)
    print(t)


if __name__ == '__main__':
    main()
