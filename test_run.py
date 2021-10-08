import os

from budget import Budget
from budget.endpoint.sqlite.sqlite_endpoint import SqliteEndpoint
from budget.models import Tables, Account, Currency, IncomeCategory, IncomeSubcategory, OutcomeCategory, \
    OutcomeSubcategory, Tag, Transaction

storage_path = os.path.join(os.getcwd(), '.data/sqlite/budget.db')


my_data = {
    Currency: (
        Currency(name='USD', symbol='$', relative_value=0),
        Currency(name='EUR', symbol='€', relative_value=0),
        Currency(name='RUB', symbol='₽', relative_value=1, main=True),
    ),
    Account: (
        Account(name='Тинькофф', currency='RUB', initial_value=804.63),
        Account(name='Подушка USD', currency='USD', initial_value=1),
        Account(name='Подушка EUR', currency='EUR', initial_value=1),
        Account(name='Подушка RUB', currency='RUB', initial_value=70200.07),
        Account(name='Копилка', currency='RUB', initial_value=18107.11),
        Account(name='Райфайзен', currency='RUB', initial_value=654.06),
        Account(name='Налик', currency='RUB', initial_value=11),
    ),
    IncomeCategory: (
        IncomeCategory(name='Люксофт'),
    ),
    IncomeSubcategory: (
        IncomeSubcategory(name='Аванс', parent='Люксофт'),
        IncomeSubcategory(name='Зарплата', parent='Люксофт'),
    ),
    OutcomeCategory: (
        OutcomeCategory(name='Продукты'),
        OutcomeCategory(name='Развлечения'),
        OutcomeCategory(name='Подарки'),
        OutcomeCategory(name='Счета'),
        OutcomeCategory(name='Дом'),
        OutcomeCategory(name='Транспорт'),
        OutcomeCategory(name='Кафе'),
        OutcomeCategory(name='Одежда'),
    ),
    OutcomeSubcategory: (),
    Tag: (),
    Transaction: (),
}


def main():
    endpoint = SqliteEndpoint(storage_path)
    budget = Budget(endpoint)


if __name__ == '__main__':
    main()
