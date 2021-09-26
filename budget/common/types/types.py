from typing import Union, Any

from pandas import DataFrame

from budget.models import (
    Base,
)

Table = Base
Model = Base

SqliteEndpointInput = Table
SqliteEndpointOutput = Table

# TODO: define data types for google sheets
GoogleSheetsInput = Any
GoogleSheetsOutput = Any

CsvEndpointInput = DataFrame
CsvEndpointOutput = DataFrame

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
