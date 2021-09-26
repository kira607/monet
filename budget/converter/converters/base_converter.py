from abc import ABC, abstractmethod

from budget.common.types import EndpointInput, EndpointOutput, Table, Model
from ..request_type import RequestType


class BaseConverter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_input(self, instance: Model, request_type: RequestType) -> EndpointInput:
        pass

    @abstractmethod
    def get_output(self, table: Table, data: EndpointOutput) -> Model:
        pass
