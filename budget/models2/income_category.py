from sqlalchemy import Column, String

from budget.models2._base import WithId, WithIcon, Base, Table


class IncomeCategory(WithId, WithIcon, Base, Table):
    __tablename__ = 'income_categories'

    name = Column(String, nullable=False)
