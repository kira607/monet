from budget.models.model.field import Field
from budget.models.model import Model


class Tag(Model):
    id = Field(str, primary=True, unique=True, nullable=False)
    name = Field(str)
    color = Field(str)
    icon = Field(str)
