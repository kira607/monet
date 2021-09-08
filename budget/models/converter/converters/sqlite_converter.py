from budget.common import Date
from budget.common.types import SqliteEndpointInput, SqliteEndpointOutput
from budget.models import Model, DataModel
from budget.models.converter.converters.base_converter import BaseConverter
from budget.models.converter.request_type import RequestType


class SqliteConverter(BaseConverter):
    def __init__(self):
        super().__init__()

    def get_input(self, model: Model, request_type: RequestType) -> SqliteEndpointInput:
        return model

    def get_output(self, data_model: DataModel, data: SqliteEndpointOutput) -> Model:
        model = data_model.model()
        for kw, new_value in zip(model.fields, data):
            name, field = kw
            new_type = field.type
            if new_value is not None and new_value != 'None':
                if new_type == Date:
                    new_value = new_type.from_str(new_value)
                else:
                    new_value = new_type(new_value)
            else:
                new_value = None if name != 'id' else 'None'
            setattr(model, name, new_value)
        return model
