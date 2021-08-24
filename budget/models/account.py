from budget.models.model import Model, Field


class Account(Model):
    id = Field(str, primary=True, unique=True, nullable=False)
    name = Field(str)
    currency = Field(str)
    initial_value = Field(float)
    current_value = Field(float)
