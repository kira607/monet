import datetime


class Date:
    def __init__(self, year, month, day):
        self._dt = datetime.date(year, month, day)

    def __str__(self):
        return self._dt.strftime('%d.%m.%Y')

    @classmethod
    def from_str(cls, string: str) -> 'Date':
        d, m, y = tuple(int(x) for x in tuple(string.split('.')))
        return cls(y, m, d)
