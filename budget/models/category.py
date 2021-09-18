from budget.models.base_model import Model, Field


class Category(Model):
    name = Field(str, nullable=False)
    color = Field(str, nullable=False)
    icon = Field(str, nullable=False)
