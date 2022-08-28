from sqlalchemy import Column, String

from ._base import Base
from ._mixins import WithId, WithIcon


class Tag(WithId, WithIcon, Base):
    __tablename__ = 'tags'

    name = Column(String, nullable=False)

    def __repr__(self):
        return (
            f'<Tag#{self.id} name={self.name}>'
        )