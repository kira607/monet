from typing import Type, Generator, Tuple, Optional, Any

from budget.models import Model
from budget.models.model import Field


class DataModel:
    name: str
    model: Type[Model]
    id_prefix: str

    def __init__(self, name: str, model: Type[Model], prefix: str):
        self.name = name
        self.model = model
        self.id_prefix = prefix

    def iter(
            self,
            add_value=False,
            add_type=False,
            add_field=False,
    ) -> Generator[Tuple[str, Optional[Any], Optional[Type], Optional[Field]], None, None]:
        for field_obj, kw_value in zip(self.model().fields, self.model().values):
            name, field = field_obj
            name, value = kw_value
            to_yield = [name]
            if add_value:
                to_yield.append(value)
            if add_type:
                to_yield.append(field.type)
            if add_field:
                to_yield.append(field)
            yield tuple(to_yield)
