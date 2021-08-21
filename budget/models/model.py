from typing import List

from budget.models.field import Field


class Model:
    def __init__(self, **kwargs):
        for name, value in kwargs:
            if name in self.__class__.__dict__.keys():
                self.__custom_setattr(name, value)
            else:
                raise Exception(f'Not a valid keyword argument: {name}')

    def __setattr__(self, key, value):
        self.__custom_setattr(key, value)

    def __getattribute__(self, item):
        obj = super(Model, self).__getattribute__(item)
        if isinstance(obj, Field):
            return obj.value
        return obj

    def __getattr__(self, item):
        pass

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
                a.append((attribute, self.__custom_getattr(attribute)))
        return a

    def __custom_setattr(self, key, value):
        self.__class__.__dict__[key].set_value(value)
