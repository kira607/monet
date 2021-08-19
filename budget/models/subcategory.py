from budget.models.field import Field
from budget.models.model import Model


class SubCategory(Model):
    id = Field(str)
    name = Field(str)
    parent_category = Field(str)
    color = Field(str)
    icon = Field(str)
