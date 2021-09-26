from sqlalchemy import Column, String

from budget.models2._base import WithId, WithIcon, Base, Table


class Tag(WithId, WithIcon, Base, Table):
    __tablename__ = 'tags'

    name = Column(String, nullable=False)
