from sqlalchemy import String, Column, Boolean, Float, Unicode

from ._base import Base
from ._mixins import WithId


class Currency(WithId, Base):
    __tablename__ = 'currencies'

    name = Column(String, nullable=False, unique=True)
    symbol = Column(Unicode)
    relative_value = Column(Float, nullable=False)
    main = Column(Boolean, default=False)

    def __repr__(self):
        return (
            f'<Currency#{self.id} name={self.name} symbol={self.symbol} '
            f'relative_value={self.relative_value} main={self.main}>'
        )
