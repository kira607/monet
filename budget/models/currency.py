from budget.models.base_model import Model, Field


class Currency(Model):
    currency = Field(str, nullable=False)
    relative_value = Field(float, nullable=False)
    main = Field(bool, default=False)
