from typing import Tuple, Union

from budget.models import Model

SqliteEndpointInput = Model
SqliteEndpointOutput = Tuple

CsvEndpointInput = None
CsvEndpointOutput = None

EndpointInput = Union[
    SqliteEndpointInput,
    CsvEndpointInput,
]

EndpointOutput = Union[
    SqliteEndpointOutput,
    CsvEndpointOutput,
]
