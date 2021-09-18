from budget.models.base_model import Model, Field


class Account(Model):
    name = Field(str, nullable=False)
    currency = Field(str, nullable=False)
    initial_value = Field(float, default=0.0)
    current_value = Field(float, default=0.0, nullable=False)
