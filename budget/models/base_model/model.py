from typing import List, Tuple, Any, Union, Type, Dict

from budget.models.base_model import Field


class Model:
    _fields = {}

    def __new__(cls, *args, **kwargs):
        # TODO: id gen
        instance = super(Model, cls).__new__(cls)
        fields = cls.__load_fields()
        instance._fields = fields.copy()
        return instance

    def __init__(self, **kwargs):
        for name, value in self._fields.items():
            if name == 'id':
                pass  # gen id
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

    @classmethod
    def cols_num(cls):
        pass

    def get_cols_num(self) -> int:
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

    @classmethod
    def __load_fields(cls) -> Dict[str, Field]:
        fields = {
            'id': Field(str, primary=True, unique=True, nullable=False)
        }
        for k, v in cls.__dict__.items():
            if isinstance(v, Field):
                v = v._get_clear_copy()
                v._name = k
                fields[k] = v
        return fields
