from budget.common import Date
from budget.models.base_model import Model, Field


class Operation(Model):
    name = Field(str, nullable=False)
    from_id = Field(str, nullable=False)
    to_id = Field(str, nullable=False)
    value = Field(float, nullable=False)
    pay_date = Field(Date)
    start_date = Field(Date)
    due_date = Field(Date)
    planned_value = Field(float)
    planned = Field(bool) 
    comment = Field(str)
    tag = Field(str)
