from budget.models.field import Field
from budget.models.model import Model


class Category(Model):
    id = Field(str)
    name = Field(str)
    color = Field(str)
    icon = Field(str)
