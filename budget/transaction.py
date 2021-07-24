from asset import Asset
from datetime import datetime

class Transaction:
    from_: Asset = None
    to: Asset = None
    value: float = 0.0
    date: datetime = None

    def __init__(self, from_, to, value, date):
        self.from_ = from_
        self.to = to
        self.value = value
        self.date = date

    '''
    {
    'name': '',
    'permanent': '',
    'recurring type': '',
    'plan date': '',
    'plan value': '',
    'fact value': '',
    'category': '',
    'tag': '',
    }
    '''