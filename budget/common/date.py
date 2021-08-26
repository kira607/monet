import datetime


class Date:
    def __init__(self, year, month, day):
        self._dt = datetime.date(year, month, day)

    def __str__(self):
        return self._dt.strftime('%d.%m.%Y')
