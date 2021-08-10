from datetime import datetime
from typing import Union

from .common.utils import gen_id


class DateTime:
    def __init__(
            self,
            year: int = 1,
            month: int = 1,
            day: int = 1,
            *,
            dt: datetime = None
    ):
        self.__format = '%d-%m-%Y'
        self.__dt = datetime(year, month, day) or dt

    def __str__(self):
        return self.__dt.strftime(self.__format)


class Transaction:
    value: float = Field(float)
    fields_types = {
        'id': str,
        'name': str,
        'from_id': str,
        'to_id': str,
        'value': float,
        'pay_date': DateTime,
        'start_date': DateTime,
        'due_date': DateTime,
        'planned_value': float,
        'comment': str,
    }

    def __init__(
            self,
            from_id: str,
            to_id: str,
            value: float,
            date: Union[DateTime, datetime],
    ):
        self.__init_fields()
        self.id = gen_id('T-')
        self.from_id = from_id
        self.to_id = to_id
        self.value = value
        self.pay_date = date if isinstance(date, DateTime) else DateTime(dt=date)

    def dict(self):
        d = {}
        for fn, _ in self.__dict__.items():
            d[fn] = getattr(self, fn)
        return d

    def __init_fields(self):
        self.id = str()
        self.name = str()
        self.from_id = str()
        self.to_id = str()
        self.value = float()
        self.pay_date = DateTime()
        self.start_date = DateTime()
        self.due_date = DateTime()
        self.planned_value = float()
        self.comment = str()

