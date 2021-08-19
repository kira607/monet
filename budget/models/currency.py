from budget.models.field import Field
from budget.models.model import Model


class Currency(Model):
    currency = Field(str)
    relative_value = Field(float)
    main = Field(bool)
