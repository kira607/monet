from sqlalchemy import Column, String, Float

from ._base import Base
from ._mixins import WithId


class Account(WithId, Base):
    __tablename__ = 'accounts'

    name = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    initial_value = Column(Float, default=0.0, nullable=False)
    current_value = Column(Float, default=0.0)

    def __repr__(self):
        return (
            f'<Account#{self.id} name={self.name} currency={self.currency} '
            f'initial_value={self.initial_value}, current_value={self.current_value}>'
        )
