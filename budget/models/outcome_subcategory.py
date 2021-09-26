from sqlalchemy import Column, String, ForeignKey

from budget.models.outcome_category import OutcomeCategory
from ._base import Base
from ._mixins import WithId, WithIcon


class OutcomeSubcategory(WithId, WithIcon, Base):
    __tablename__ = 'outcome_subcategories'

    name = Column(String, nullable=False)
    parent = ForeignKey(OutcomeCategory.id)

    def __repr__(self):
        return (
            f'<OutcomeSubcategory#{self.id} name={self.name} parent={self.parent}>'
        )
