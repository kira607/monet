from sqlalchemy import Column, String, ForeignKey

from budget.models2._base import WithId, WithIcon, Base, Table
from budget.models2.income_category import IncomeCategory


class IncomeSubcategory(WithId, WithIcon, Base, Table):
    __tablename__ = 'income_subcategories'

    name = Column(String, nullable=False)
    parent = ForeignKey(IncomeCategory.id)
