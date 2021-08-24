from budget.models.converter.converter_data import ConverterData
from budget.models.converter.converters.base import BaseConverter
from budget.models.converter.request_type import RequestType


class SqliteConverter(BaseConverter):
    def __init__(self, data: ConverterData):
        super().__init__(data)

    def get_data(self):
        return self.__create_statement()

    def __create_statement(self):
        rt_map = {
            RequestType.GET: f'SELECT * FROM {self._data.table};',
            RequestType.INSERT: (
                f'INSERT INTO {self._data.table} VALUES ({", ".join(str(v) for _, v in self._data.model.attributes)});'
            ),
            RequestType.UPDATE: (
                f'UPDATE {self._data.table} SET '
                f'{", ".join((f"{k} = {v}" for k, v in self._data.model.attributes))} WHERE id={self._data.model.id};'
            ),
            RequestType.DELETE: f'DELETE FROM {self._data.table} WHERE id={self._data.model.id};',
        }
        return rt_map[self._data.request_type]

