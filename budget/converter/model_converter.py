from typing import Type, Dict

from budget.common.types import EndpointOutput, EndpointInput, Model, Table
from budget.endpoint import (
    BaseEndpoint,
    SqliteEndpoint,
)
from .converters import SqliteConverter, BaseConverter
from .request_type import RequestType


class ModelConverter:
    def __init__(self, endpoint: Type[BaseEndpoint]):
        self.endpoint_mapping: Dict[Type[BaseEndpoint], Type[BaseConverter]] = {
            SqliteEndpoint: SqliteConverter,
        }
        self.__cached_converters: Dict[Type[BaseEndpoint], BaseConverter] = {}
        self.__set_endpoint(endpoint)

    def get_input(self, model: Model, request_type: RequestType) -> EndpointInput:
        return self.__converter.get_input(model, request_type)

    def get_output(self, table: Table, data: EndpointOutput) -> Model:
        return self.__converter.get_output(table, data)

    def __set_endpoint(self, endpoint: Type[BaseEndpoint]):
        self.__converter = self.__cached_converters.get(endpoint)
        if self.__converter is None:
            self.__cached_converters[endpoint] = self.endpoint_mapping[endpoint]()
        self.__converter = self.__cached_converters[endpoint]
