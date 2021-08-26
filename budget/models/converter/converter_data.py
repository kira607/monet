from budget.models import Model
from budget.models.converter.request_type import RequestType


class ConverterData:
    def __init__(self, model: Model, schema_name: str, request_type: RequestType):
        self.model = model
        self.schema_name = schema_name
        self.request_type = request_type
