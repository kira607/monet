from typing import Type

from budget.models.converter.converter_data import ConverterData
from budget.models.converter.request_type import RequestType
from budget.models.converter.converters.sqlite_converter import SqliteConverter
from budget.models import (
    Account,
    Category,
    Currency,
    SubCategory,
    Tag,
    Transaction,
    BaseModel,
)
from budget.endpoint import (
    BaseEndpoint,
    SqliteEndpoint,
    # GoogleSheetsEndpoint,
    CsvEndpoint,
)


class ModelConverter:
    def __init__(self):
        self.table_mapping = {
            Account: 'Account',
            Category: 'Category',
            Currency: 'Currency',
            SubCategory: 'SubCategory',
            Tag: 'Tag',
            Transaction: 'Transaction',
        }
        self.endpoint_mapping = {
            SqliteEndpoint: SqliteConverter,
            # GoogleSheetsEndpoint: 'GoogleSheetsEndpoint',
            CsvEndpoint: 'CsvEndpoint',
        }

    def convert(self, model: BaseModel, endpoint: Type[BaseEndpoint], request_type: RequestType = RequestType.GET):
        table = self.table_mapping.get(type(model), None)
        if table is None:
            raise RuntimeError(f'Unexpected model type: {type(model).__name__}')
        data = ConverterData(model, table, request_type)
        converter = self.endpoint_mapping[endpoint](data)
        return converter.get_data()
