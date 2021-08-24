from budget.models.model.field import Field
from budget.models.model import Model


class SubCategory(Model):
    id = Field(str, primary=True, unique=True, nullable=False)
    name = Field(str)
    parent_category = Field(str)
    color = Field(str)
    icon = Field(str)
