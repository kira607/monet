from sqlalchemy import Column, String

from ._base import Base
from ._mixins import WithId, WithIcon


class OutcomeCategory(WithId, WithIcon, Base):
    __tablename__ = 'outcome_categories'

    name = Column(String, nullable=False)

    def __repr__(self):
        return (
            f'<OutcomeCategory#{self.id} name={self.name}>'
        )
