import datetime
from typing import List

from budget.common import gen_id
from budget.endpoint import BaseEndpoint
from budget.models import DataModel, Model
from budget.models.converter import ModelConverter, RequestType


class Budget:
    '''
    Here will take place all
    planning, filtering, editing, defaulting, etc.
    '''
    def __init__(self, endpoint: BaseEndpoint):
        self.endpoint = endpoint
        self.converter = ModelConverter(type(endpoint))

    def add(self, data_model: DataModel, **kwargs) -> Model:
        new_model = self.__create_model(data_model, **kwargs)
        data = self.converter.get_input(new_model, RequestType.INSERT)
        inserted = self.endpoint.insert(data_model, data)
        return self.converter.get_output(data_model, inserted)

    def get(self, data_model: DataModel, **kwargs) -> List[Model]:
        data = self.endpoint.get(data_model, **kwargs)
        for index, data_item in enumerate(data):
            data[index] = self.converter.get_output(data_model, data_item)
        return data

    def update(self, data_model: DataModel, model_id, **kwargs) -> Model:
        pass

    def delete(self, data_model: DataModel, model_id) -> None:
        pass

    def __create_model(self, data_model: DataModel, **kwargs):
        new_model = data_model.model()
        # set values
        for name, value in kwargs.items():
            if name not in (n[0] for n in data_model.iter()):
                raise ValueError(f'Model of type {data_model.name} has no attribute {name}')
            if name == 'id':
                raise Exception('It is prohibited to set id manually')
            if value is None and not data_model.get_field(name).nullable:
                raise Exception(f'Field {name} cannot be null')
            setattr(new_model, name, value)

        # verify model
        for name, value in new_model.values:
            if value is None and not data_model.get_field(name).nullable and name != 'id':
                raise Exception(f'Field {name} cannot be null')

        # TODO: move id generation into the base model
        while True:
            new_id = gen_id(data_model.id_prefix)
            duplicate = self.endpoint.get(data_model, id=new_id)
            if len(duplicate) == 0:
                new_model.id = new_id
                break
        return new_model

    @staticmethod
    def __now():
        return datetime.datetime.now().strftime('%d-%m-%Y')
