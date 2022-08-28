from marshmallow import Schema
from marshmallow.fields import Str


class Transaction(Schema):
    '''A transaction schema.'''

    id = Str()  # noqa: A002, A003
