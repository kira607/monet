from sqlalchemy import Column, String

from budget.models2._base import WithId, WithIcon, Base, Table


class OutcomeCategory(WithId, WithIcon, Base, Table):
    __tablename__ = 'outcome_categories'

    name = Column(String, nullable=False)
