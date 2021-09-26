from sqlalchemy import Column, String, ForeignKey

from .income_category import IncomeCategory
from ._base import Base
from ._mixins import WithId, WithIcon


class IncomeSubcategory(WithId, WithIcon, Base):
    __tablename__ = 'income_subcategories'

    name = Column(String, nullable=False)
    parent = ForeignKey(IncomeCategory.id)

    def __repr__(self):
        return (
            f'<IncomeSubcategory#{self.id} name={self.name}, parent={self.parent}>'
        )
