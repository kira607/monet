from budget.common.datetime import DateTime
from budget.models.model.field import Field
from budget.models.model import Model


class Transaction(Model):
    id = Field(str, primary=True, unique=True, nullable=False)
    name = Field(str, nullable=False)
    from_id = Field(str, nullable=False)
    to_id = Field(str, nullable=False)
    value = Field(float, nullable=False)
    pay_date = Field(DateTime, nullable=False)
    start_date = Field(DateTime)
    due_date = Field(DateTime)
    planned_value = Field(float)
    planned = Field(bool) 
    comment = Field(str)
    tag = Field(str)
