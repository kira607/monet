from abc import ABC, abstractmethod

from budget.common.types import EndpointInput, EndpointOutput
from budget.models import Model, DataModel
from ..request_type import RequestType


class BaseConverter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_input(self, model: Model, request_type: RequestType) -> EndpointInput:
        pass

    @abstractmethod
    def get_output(self, data_model: DataModel, data: EndpointOutput) -> Model:
        pass
