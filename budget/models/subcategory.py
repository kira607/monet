from budget.models.model.field import Field
from budget.models.model import Model


class SubCategory(Model):
    id = Field(str, primary=True, unique=True, nullable=False)
    name = Field(str, nullable=False)
    parent_category = Field(str, nullable=False)
    color = Field(str, nullable=False)
    icon = Field(str, nullable=False)
