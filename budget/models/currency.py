from budget.models.model.field import Field
from budget.models.model import Model


class Currency(Model):
    id = Field(str, primary=True, unique=True, nullable=False)
    currency = Field(str, nullable=False)
    relative_value = Field(float, nullable=False)
    main = Field(bool, default=False)
