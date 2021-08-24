from abc import ABC, abstractmethod
from typing import Type, Any, Iterable

from budget.models import Model


class BaseEndpoint(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def insert(self, model: Type[Model], data: Any) -> Model:
        '''
        Insert new model into storage

        :param model: type of model (to identify table)
        :param data: data to insert (one instance at a call)
        :return: inserted model instance
        '''
        pass

    @abstractmethod
    def delete(self, model: Type[Model], data: Any) -> None:
        '''
        Delete model from storage

        :param model: type of model (to identify table)
        :param data: data to identify model in the storage
        :return: None
        '''
        pass

    @abstractmethod
    def get(self, model: Type[Model]) -> Iterable[Model]:
        '''
        Get all models list from the storage

        :param model: type of model (to identify table)
        :return:
        '''
        pass

    @abstractmethod
    def update(self, model: Type[Model], data: Model) -> Model:
        '''
        Update model in the storage

        :param model: type of model (to identify table)
        :param data: Updated model instance
        :return: Updated model
        '''
        pass
