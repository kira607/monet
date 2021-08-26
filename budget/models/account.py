from budget.models.model import Model, Field


class Account(Model):
    id = Field(str, primary=True, unique=True, nullable=False)
    name = Field(str, nullable=False)
    currency = Field(str, nullable=False)
    initial_value = Field(float, default=0.0)
    current_value = Field(float, default=0.0, nullable=False)
