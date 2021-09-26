from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class WithId(object):
    id = Column(String(6), primary_key=True, unique=True, nullable=False)


class WithIcon(object):
    icon = Column(String())
    color = Column(String())
