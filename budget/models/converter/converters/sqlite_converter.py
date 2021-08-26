from budget.models.converter.converter_data import ConverterData
from budget.models.converter.converters.base_converter import BaseConverter
from budget.models.converter.request_type import RequestType


class SqliteConverter(BaseConverter):
    def __init__(self, data: ConverterData):
        super().__init__(data)

    def get_data(self):
        return self._data.model
