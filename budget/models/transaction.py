from enum import Enum

from sqlalchemy import Column, String, Float, DateTime, Enum as SqlEnum, Boolean

from ._base import Base
from ._mixins import WithId


class PlanType(Enum):
    year = 'year'
    month = 'month'
    week = 'week'
    day = 'day'
    someday = 'someday'


class TransactionType(Enum):
    income = 'income'
    outcome = 'outcome'
    transfer = 'transfer'


class Transaction(WithId, Base):
    __tablename__ = 'transactions'

    name = Column(String(500), nullable=False)
    from_ = Column(String(6))  # foreign key
    to = Column(String(6))
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
            f'from_={self.from_} '
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