from enum import Enum


class RequestType(Enum):
    GET = 'GET'
    INSERT = 'INSERT'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
