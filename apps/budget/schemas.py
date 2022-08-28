from marshmallow import Schema
from marshmallow.fields import Str


class Transaction(Schema):
    id = Str()