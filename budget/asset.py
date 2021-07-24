from enum import Enum

class AssetType(Enum):
    NONE = -1
    INCOME = 0
    OUTCOME = 1

class Asset:
    asset_id: int = 0
    name: str = ''
    value: float = 0.0
    __type__ = AssetType.NONE

    def __init__(self, name: str, value: float, type: AssetType) -> None:
        self.name = name
        self.value = value
        self.__type__ = type

    @property
    def type(self):
        return self.__type__

    def change_value(self, val: float):
        self.value += val

    def __str__(self):
        return f'{self.name} {self.value} {self.__type__.name}'
    