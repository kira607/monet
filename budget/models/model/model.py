from typing import List, Tuple, Any

from budget.models.model.field import Field


class Model:
    def __init__(self, **kwargs):
        for name, value in kwargs:
            if name in self.__class__.__dict__.keys():
                self.__custom_setattr(name, value)
            else:
                raise Exception(f'Not a valid keyword argument: {name}')
        self.get_field_switch = False

    def __setattr__(self, key, value):
        if key in self.__class__.__dict__.keys():
            self.__custom_setattr(key, value)
        else:
            super(Model, self).__setattr__(key, value)

    def __getattribute__(self, item):
        obj = super(Model, self).__getattribute__(item)
        if isinstance(obj, Field) and not self.__get_field_switch:
            return obj.value
        return obj

    @property
    def attributes(self) -> List[Tuple[str, Any]]:
        a = []
        for attribute_name in self.__class__.__dict__.keys():
            attribute_value = self.__custom_getattr(attribute_name, True)
            if (
                    attribute_name[:2] != '__' and
                    not callable(attribute_value) and
                    isinstance(attribute_value, Field)
            ):
                a.append((attribute_name, attribute_value.value))
        return a

    @property
    def fields(self) -> List[Tuple[str, Field]]:
        '''
        Get fields of a model.

        :return: List of model fields in a (name, model object) tuple
        '''
        a = []
        for attribute_name in self.__class__.__dict__.keys():
            attribute_value = self.__custom_getattr(attribute_name, True)
            if (
                    attribute_name[:2] != '__' and
                    not callable(attribute_value) and
                    isinstance(attribute_value, Field)
            ):
                a.append((attribute_name, attribute_value))
        return a

    def __custom_setattr(self, key, value):
        self.__class__.__dict__[key].set_value(value)

    def __custom_getattr(self, attribute_name, get_field_obj: bool = False):
        self.__get_field_switch = get_field_obj
        value = getattr(self, attribute_name)
        self.__get_field_switch = False
        return value
