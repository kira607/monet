import datetime
from typing import List

from budget.common.types import Table, Model
from budget.endpoint import BaseEndpoint
from budget.converter import ModelConverter, RequestType


class Budget:
    '''
    Here will take place all
    planning, filtering, editing, defaulting, etc.
    '''
    def __init__(self, endpoint: BaseEndpoint):
        self.endpoint = endpoint
        self.converter = ModelConverter(type(endpoint))

    def add(self, table: Table, instance: Model) -> Model:
        data = self.converter.get_input(instance, RequestType.INSERT)
        inserted = self.endpoint.insert(table, data)
        return self.converter.get_output(table, inserted)

    def get(self, table: Table, **kwargs) -> List[Model]:
        data = self.endpoint.get(table, **kwargs)
        for index, data_item in enumerate(data):
            data[index] = self.converter.get_output(table, data_item)
        return data

    def update(self, table: Table, instance: Model) -> Model:
        data = self.converter.get_input(instance, RequestType.UPDATE)
        updated = self.endpoint.update(table, data)
        return self.converter.get_output(table, updated)

    def delete(self, table: Table, instance: Model) -> None:
        data = self.converter.get_input(instance, RequestType.DELETE)
        self.endpoint.delete(table, data)

    @staticmethod
    def __now():
        return datetime.datetime.now().strftime('%d-%m-%Y')
