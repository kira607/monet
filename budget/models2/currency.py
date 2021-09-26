from sqlalchemy import String, Column, Boolean, Float, Unicode

from budget.models2._base import WithId, Base, Table


class Currency(WithId, Base, Table):
    __tablename__ = 'currencies'

    name = Column(String, nullable=False, unique=True)
    symbol = Column(Unicode)
    relative_value = Column(Float, nullable=False)
    main = Column(Boolean, default=False)
