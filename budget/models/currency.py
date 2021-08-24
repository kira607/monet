from budget.models.model.field import Field
from budget.models.model import Model


class Currency(Model):
    id = Field(str, primary=True, unique=True, nullable=False)
    currency = Field(str)
    relative_value = Field(float)
    main = Field(bool)
