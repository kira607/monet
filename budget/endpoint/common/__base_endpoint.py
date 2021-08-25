from abc import ABC, abstractmethod
from typing import Any, Iterable

from budget.models import Model, DataModel


class BaseEndpoint(ABC):
    @abstractmethod
    def insert(self, data_model: DataModel, data: Any) -> Model:
        '''
        Insert new model into the storage

        :param data_model: type of model (to identify table)
        :param data: data to insert (one instance at a call)
        :return: inserted model instance
        '''
        pass

    @abstractmethod
    def get(self, data_model: DataModel) -> Iterable[Model]:
        '''
        Get all models list from the storage

        :param data_model: type of model (to identify table)
        :return:
        '''
        pass

    @abstractmethod
    def update(self, data_model: DataModel, data: Any) -> Model:
        '''
        Update model in the storage

        :param model_id: id of the model (to identify model in the storage)
        :param data_model: type of model (to identify table)
        :param data: Updated model instance
        :return: Updated model
        '''
        pass

    @abstractmethod
    def delete(self, data_model: DataModel, data: Any) -> None:
        '''
        Delete model from the storage

        :param data_model: type of model (to identify table)
        :param data: data to identify model in the storage
        :return: None
        '''
        pass
