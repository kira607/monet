from sqlalchemy import Column, String

from ._base import Base
from ._mixins import WithId, WithIcon


class IncomeCategory(WithId, WithIcon, Base):
    __tablename__ = 'income_categories'

    name = Column(String, nullable=False)

    def __repr__(self):
        return (
            f'<IncomeCategory#{self.id} name={self.name}>'
        )
