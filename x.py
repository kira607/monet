import db


def main():
    client = db.DbClient('.data/sqlite/budget.db')
    transactions = client.get(db.models.Transaction, filters=())


if __name__ == '__main__':
    main()