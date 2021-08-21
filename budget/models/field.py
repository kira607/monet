from typing import Any, Type


class Field:
    _type: type
    _value: Any

    def __init__(self, field_type: Type, default: Any = None):
        self._type = field_type
        self.__value_check(default)
        self._value = default

    def set_value(self, value):
        self.__value_check(value)
        self._value = value

    @property
    def value(self):
        return self._value

    def __value_check(self, value):
        # type check
        if not isinstance(value, self._type) and value is not None:
            raise TypeError(f'value type must be {self._type.__name__}')

    def __repr__(self):
        return f'<class Field({self._type.__name__}, {self._value})>'
