from enum import Enum

from sqlalchemy import Column, String, Float, DateTime, Enum as SqlEnum, Boolean, Integer

from ._base import Base
from ._mixins import WithId


class PlanType(Enum):
    YEAR = 'year'
    MONTH = 'month'
    WEEK = 'week'
    DAY = 'day'
    SOMEDAY = 'someday'


class TransactionType(Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'
    TRANSFER = 'transfer'


class Transaction(Base, WithId):
    __tablename__ = 'transactions'

    name = Column(String(500), nullable=False)
    from_ = Column('from', String(6))  # foreign key
    to = Column(String(6))  # foreign key
    value = Column(Float(16))
    pay_date = Column(DateTime())
    plan_date = Column(DateTime())
    plan_type = Column(SqlEnum(PlanType))
    planned_value = Column(Float(16))
    planned = Column(Boolean())
    comment = Column(String(1000))
    tag = Column(String(6))
    type = Column(SqlEnum(TransactionType))

    def __repr__(self):
        return (
            f'<Transaction#{self.id} '
            f'name={self.name} '
            f'from={self.from_} '
            f'to={self.to} '
            f'value={self.value} '
            f'pay_date={self.pay_date} '
            f'plan_date={self.plan_date} '
            f'plan_type={self.plan_type} '
            f'planned_value={self.planned_value} '
            f'planned={self.planned} '
            f'comment={self.comment} '
            f'tag={self.tag} '
            f'type={self.type}>'
        )