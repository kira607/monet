from typing import List, Tuple, Any, Union

from budget.models.base_model import Field


class Model:
    _fields = {}

    def __new__(cls, *args, **kwargs):
        # TODO: id gen
        instance = super(Model, cls).__new__(cls)
        common_fields = {
            'id': Field(str, primary=True, unique=True, nullable=False)
        }
        instance._fields = common_fields.copy()
        for k, v in cls.__dict__.items():
            if isinstance(v, Field):
                v._name = k
                instance._fields[k] = v
        return instance

    def __init__(self, **kwargs):
        for name, value in self._fields.items():
            if name == 'id':
                pass  # gen id
            elif value.nullable:
                self._fields[name].set_value(None)
        for name, value in kwargs.items():
            if name in self._fields.keys():
                self.__custom_setattr(name, value)
            else:
                raise Exception(f'Not a valid keyword argument: {name}')

    def __setattr__(self, key, value):
        if key in self._fields.keys():
            self.__custom_setattr(key, value)
        else:
            super(Model, self).__setattr__(key, value)

    def __getattr__(self, name):
        try:
            return self._fields[name].value
        except KeyError as e:
            raise e

    @property
    def cols_num(self) -> int:
        return len(self._fields)

    @property
    def values(self) -> List[Tuple[str, Any]]:
        '''
        Get attributes names and their values of the model

        :return: List containing name of a field and its value in a (name, value) format
        '''
        return self.__attrs(False)

    @property
    def fields(self) -> List[Tuple[str, Field]]:
        '''
        Get attributes names and their objects of the model

        :return: List containing name of a field and its object in a (name, object) format
        '''
        return self.__attrs(True)

    def __attrs(self, _obj: bool = False) -> List[Tuple[str, Union[Field, Any]]]:
        '''
        Get attributes values of the model

        :param _obj: return Field objects instead of actual values
        :return: -
        '''
        a = []
        for name, field in self._fields.items():
            a.append((name, field if _obj else field.value))
        return a

    def __custom_setattr(self, key, value):
        try:
            self._fields[key].set_value(value)
        except TypeError as e:
            raise TypeError(f'field {key}: {e}')
