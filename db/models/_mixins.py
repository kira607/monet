from sqlalchemy import Column, String

from budget.common import gen_id


class WithId(object):
    id = Column(String(6), primary_key=True, unique=True, nullable=False, default=gen_id)


class WithIcon(object):
    icon = Column(String())
    color = Column(String())
