from typing import List

from budget.common.types import GoogleSheetsInput, GoogleSheetsOutput
from budget.endpoint import BaseEndpoint
from budget.models import DataModel


class GoogleSheetsEndpoint(BaseEndpoint):
    def insert(self, data_model: DataModel, data: GoogleSheetsInput) -> GoogleSheetsOutput:
        pass

    def get(self, data_model: DataModel, **kwargs) -> List[GoogleSheetsOutput]:
        pass

    def update(self, data_model: DataModel, data: GoogleSheetsInput) -> GoogleSheetsOutput:
        pass

    def delete(self, data_model: DataModel, data: GoogleSheetsInput) -> GoogleSheetsOutput:
        pass
