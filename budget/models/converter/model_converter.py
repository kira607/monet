from typing import Type, Any, Dict

from budget.endpoint import (
    BaseEndpoint,
    SqliteEndpoint,
)
from budget.models import Model, data_schema
from .converter_data import ConverterData, RequestType
from .converters import SqliteConverter, BaseConverter


class ModelConverter:
    def __init__(self):
        self.endpoint_mapping: Dict[Type[BaseEndpoint], Type[BaseConverter]] = {
            SqliteEndpoint: SqliteConverter,
        }

    def convert(
            self,
            model: Model,
            endpoint: Type[BaseEndpoint],
            request_type: RequestType = RequestType.GET
    ) -> Any:
        '''
        Convert model object into a endpoint specific data type

        :param model: model object to convert
        :param endpoint: type of endpoint to which data type conversion will be executed
        :param request_type: type of request
        :return: endpoint specific data type
        '''
        model_name = type(model).__name__
        if (data_model := data_schema.get(model_name)) is None:
            raise RuntimeError(f'Unexpected model type: {model_name}')
        data = ConverterData(model, data_model.name, request_type)
        converter = self.endpoint_mapping[endpoint](data)
        return converter.get_data()
