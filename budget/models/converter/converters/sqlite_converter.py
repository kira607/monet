from budget.models.converter.converter_data import ConverterData
from budget.models.converter.converters.base_converter import BaseConverter
from budget.models.converter.request_type import RequestType


class SqliteConverter(BaseConverter):
    def __init__(self, data: ConverterData):
        super().__init__(data)

    def get_data(self):
        table = self._data.schema_name
        model = self._data.model
        rt_map = {
            RequestType.GET: None,
            RequestType.INSERT: self.cast([v for _, v in model.values]),
            RequestType.UPDATE: self.cast([v for _, v in model.values]),
            RequestType.DELETE: model.id,
        }
        return rt_map[self._data.request_type]

    def cast(self, l):
        for n, v in enumerate(l):
            acceptable = [str, None, int, float, bytes]
            if type(v) not in acceptable:
                l[n] = str(v)
        return tuple(l)
