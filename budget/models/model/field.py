from typing import Any, Type, Union

from budget.common import Date


class Field:
    _type: Type
    _value: Any
    default: Any = None
    nullable: bool = True
    primary: bool = False
    unique: bool = False
    check: str = None
    foreign_key: Any = None

    known_types = (str, int, float, bytes, Date, bool)
    FieldType = Type[Union[str, int, float, bytes, Date, bool]]

    def __init__(
            self,
            field_type: FieldType,
            default: Any = None,
            nullable: bool = True,
            primary: bool = False,
            unique: bool = False,
            check: Any = None,
            foreign_key: str = None,
    ) -> None:
        '''
        :param field_type: type of the field
        :param default: default value of the field
        :param nullable: is field nullable (True by default)
        :param primary: is field is a primary key (False by default)
        :param unique: is field values are unique (False by default)
        :param check: string expression describing checks for field
        :param foreign_key: string describing foreign key in a `table.column` format
        '''
        if field_type not in self.known_types:
            raise Exception(f'Field type must be either [{self.known_types}]. Got {field_type}')
        self._type = field_type
        self.__value_check(default)
        self._value = default
        self.nullable = nullable
        self.primary = primary
        self.unique = unique
        self.check = check
        self.foreign_key = foreign_key

    def set_value(self, value):
        self.__value_check(value)
        self._value = value

    @property
    def value(self):
        return self._value

    @property
    def type(self):
        return self._type

    def __value_check(self, value):
        if not isinstance(value, self._type):
            if not self.nullable and value is None:  # value is None when field is not nullable
                raise TypeError(f'value cannot be None and must be {self._type.__name__}')
            elif value is not None:
                raise TypeError(f'value type must be {self._type.__name__}')

    def __repr__(self):
        return f'<class Field({self._type.__name__}, {self._value})>'
