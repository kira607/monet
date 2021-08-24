from abc import ABC, abstractmethod

from budget.models.converter.converter_data import ConverterData


class BaseConverter(ABC):
    def __init__(self, data: ConverterData):
        self._data = data

    @abstractmethod
    def get_data(self):
        pass
