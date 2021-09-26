from .account import Account
from .currency import Currency
from .income_category import IncomeCategory
from .income_subcategory import IncomeSubcategory
from .outcome_category import OutcomeCategory
from .outcome_subcategory import OutcomeSubcategory
from .tag import Tag
from .transaction import Transaction


class Tables:
    accounts = Account
    currencies = Currency
    income_categories = IncomeCategory
    income_subcategories = IncomeSubcategory
    outcome_categories = OutcomeCategory
    outcome_subcategories = OutcomeSubcategory
    tags = Tag
    transactions = Transaction
