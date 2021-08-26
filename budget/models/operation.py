from budget.common.date import Date
from budget.models.model.field import Field
from budget.models.model import Model


class Operation(Model):
    id = Field(str, primary=True, unique=True, nullable=False)
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
