from abc import ABC, abstractmethod
from typing import List

from budget.common.types import EndpointOutput, EndpointInput
from budget.common.types import Table


class BaseEndpoint(ABC):
    @abstractmethod
    def insert(self, table: Table, data: EndpointInput) -> EndpointOutput:
        '''
        Insert new model into the storage

        :param table: type of model (to identify table)
        :param data: data to insert (one instance at a call)
        :return: inserted model instance
        '''
        pass

    @abstractmethod
    def get(self, table: Table, **kwargs) -> List[EndpointOutput]:
        '''
        Get all models list from the storage

        :param table: type of model (to identify table)
        :return:
        '''
        pass

    @abstractmethod
    def update(self, table: Table, data: EndpointInput) -> EndpointOutput:
        '''
        Update model in the storage

        :param table: type of model (to identify table)
        :param data: Updated model instance
        :return: Updated model
        '''
        pass

    @abstractmethod
    def delete(self, table: Table, data: EndpointInput) -> EndpointOutput:
        '''
        Delete model from the storage

        :param table: type of model (to identify table)
        :param data: data to identify model in the storage
        :return: None
        '''
        pass
