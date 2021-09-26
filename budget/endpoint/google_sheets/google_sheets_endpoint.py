from typing import List

from budget.common.types import GoogleSheetsInput, GoogleSheetsOutput, Table
from budget.endpoint import BaseEndpoint


class GoogleSheetsEndpoint(BaseEndpoint):
    def insert(self, table: Table, data: GoogleSheetsInput) -> GoogleSheetsOutput:
        pass

    def get(self, table: Table, **kwargs) -> List[GoogleSheetsOutput]:
        pass

    def update(self, table: Table, data: GoogleSheetsInput) -> GoogleSheetsOutput:
        pass

    def delete(self, table: Table, data: GoogleSheetsInput) -> GoogleSheetsOutput:
        pass
