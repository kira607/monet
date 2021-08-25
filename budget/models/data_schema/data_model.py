from typing import Type

from budget.models import Model


class DataModel:
    name: str
    model: Type[Model]
    id_prefix: str

    def __init__(self, name: str, model: Type[Model], prefix: str):
        self.name = name
        self.model = model
        self.id_prefix = prefix