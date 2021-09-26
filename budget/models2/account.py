from sqlalchemy import Column, String, Float

from ._base import Base, WithId, Table


class Account(WithId, Base, Table):
    __tablename__ = 'accounts'

    name = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    initial_value = Column(Float, default=0.0, nullable=False)
    current_value = Column(Float, default=0.0, nullable=False)
