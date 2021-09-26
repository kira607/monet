from budget.common.types import SqliteEndpointInput, SqliteEndpointOutput, Table, Model
from budget.converter.converters.base_converter import BaseConverter
from budget.converter.request_type import RequestType


class SqliteConverter(BaseConverter):
    def __init__(self):
        super().__init__()

    def get_input(self, instance: Model, request_type: RequestType) -> SqliteEndpointInput:
        return instance

    def get_output(self, table: Table, instance: SqliteEndpointOutput) -> Model:
        return instance
