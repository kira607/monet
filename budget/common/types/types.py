from typing import Tuple, Union, Type, Any

from pandas import DataFrame

from budget.models import Model

SqliteEndpointInput = Model
SqliteEndpointOutput = Tuple

# TODO: define data types for google sheets
GoogleSheetsInput = Any
GoogleSheetsOutput = Any

CsvEndpointInput = Type[DataFrame]
CsvEndpointOutput = Type[DataFrame]

EndpointInput = Union[
    SqliteEndpointInput,
    CsvEndpointInput,
    GoogleSheetsInput,
]

EndpointOutput = Union[
    SqliteEndpointOutput,
    CsvEndpointOutput,
    GoogleSheetsOutput,
]
