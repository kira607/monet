from budget.models.converter.request_type import RequestType
from budget.models.model import Model


class ConverterData:
    def __init__(self, model: Model, table: str, request_type: RequestType):
        self.model = model
        self.table = table
        self.request_type = request_type
