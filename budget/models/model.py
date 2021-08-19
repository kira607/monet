from typing import List

from budget.models.field import Field


class Model:

    def __init__(self, **kwargs):
        for name, value in kwargs:
            if name in self.__class__.__dict__.keys():
                self.__my_setattr(name, value)
            else:
                raise Exception(f'Not a valid keyword argument: {name}')

    def __setattr__(self, key, value):
        self.__my_setattr(key, value)

    @property
    def attributes(self) -> List:
        a = []
        for attribute in self.__class__.__dict__.keys():
            value = getattr(self, attribute)
            if (
                    attribute[:2] != '__' and
                    not callable(value) and
                    isinstance(value, Field)
            ):
                a.append((attribute, value))
        return a

    def __my_setattr(self, key, value):
        self.__class__.__dict__[key].set_value(value)
