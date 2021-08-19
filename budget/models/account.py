from budget.models.field import Field


class Account:
    id = Field(str)
    name = Field(str)
    currency = Field(str)
    initial_value = Field(float)
    current_value = Field(float)
