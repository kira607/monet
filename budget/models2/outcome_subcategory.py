from sqlalchemy import Column, String, ForeignKey

from budget.models2._base import WithId, WithIcon, Base, Table
from budget.models2.outcome_category import OutcomeCategory


class OutcomeSubcategory(WithId, WithIcon, Base, Table):
    __tablename__ = 'outcome_subcategories'

    name = Column(String, nullable=False)
    parent = ForeignKey(OutcomeCategory.id)
