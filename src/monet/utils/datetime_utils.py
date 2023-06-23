"""Helper functions for datetime, timezone and timedelta objects."""


import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone, tzinfo

DT_AWARE = "%m/%d/%y %I:%M:%S %p %Z"
DT_NAIVE = "%m/%d/%y %I:%M:%S %p"
DATE_MONTH_NAME = "%b %d %Y"
ONE_DAY_IN_SECONDS = 86400


@dataclass
class Timespan:
    """A timespan class."""

    days: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0
    milliseconds: int = 0
    microseconds: int = 0
    _total_seconds: int = field(default=0, repr=False)
    _total_milliseconds: int = field(default=0, repr=False)
    _total_microseconds: int = field(default=0, repr=False)

    def __post_init__(self) -> None:
        """Post initialization."""
        (self.milliseconds, self.microseconds) = divmod(self.microseconds, 1000)
        (self.minutes, self.seconds) = divmod(self.seconds, 60)
        (self.hours, self.minutes) = divmod(self.minutes, 60)
        self._total_seconds = self.seconds + (self.days * ONE_DAY_IN_SECONDS)
        self._total_milliseconds = self.total_seconds * 1000 + self.milliseconds
        self._total_microseconds = (
            self.total_seconds * 1000 * 1000 + self.milliseconds * 1000 + self.microseconds
        )

    @property
    def total_seconds(self) -> int:
        """Get a total seconds number in a :class:`Timespan`."""
        return self._total_seconds

    @property
    def total_milliseconds(self) -> int:
        """Get a total milliseconds number in a :class:`Timespan`."""
        return self._total_milliseconds

    @property
    def total_microseconds(self) -> int:
        """Get a total microseconds number in a :class:`Timespan`."""
        return self._total_microseconds

    @classmethod
    def from_timedelta(cls, td: timedelta) -> "Timespan":
        """
        Create a :class:`Timespan` from a timedelta.

        :param td: A timedelta object.
        :return: A :class:`Timespan`.
        """
        (milliseconds, microseconds) = divmod(td.microseconds, 1000)
        (minutes, seconds) = divmod(td.seconds, 60)
        (hours, minutes) = divmod(minutes, 60)
        total_seconds = td.seconds + (td.days * ONE_DAY_IN_SECONDS)
        return cls(
            td.days,
            hours,
            minutes,
            seconds,
            milliseconds,
            microseconds,
            total_seconds,
            (total_seconds * 1000 + milliseconds),
            (total_seconds * 1000 * 1000 + milliseconds * 1000 + microseconds),
        )

    @property
    def pretty(self) -> str:
        """Format a :class:`Timespan` as a human-readable string."""
        if self.days:
            day_or_days = "days" if self.days > 1 else "day"
            return (
                f"{self.days} {day_or_days} "
                f"{self.hours:.0f} hours {self.minutes:.0f} minutes {self.seconds} seconds"
            )
        if self.hours:
            return f"{self.hours:.0f} hours {self.minutes:.0f} minutes {self.seconds} seconds"
        if self.minutes:
            return f"{self.minutes:.0f} minutes {self.seconds} seconds"
        if self.seconds:
            return f"{self.seconds} seconds {self.milliseconds:.0f} milliseconds"
        return f"{self.total_microseconds} mircoseconds"

    @property
    def digital(self) -> str:
        """Format a :class:`Timespan` as a string resembling a digital display."""
        if self.days:
            day_or_days = "days" if self.days > 1 else "day"
            return f"{self.days} {day_or_days}, " f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        if self.seconds:
            return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        return f"00:00:00.{self.total_microseconds}"


def utc_now() -> datetime:
    """Get Current UTC date and time with the microsecond value normalized to zero."""
    return datetime.now(timezone.utc).replace(microsecond=0)


def localized_dt_string(dt: datetime, use_tz: tzinfo | None = None) -> str:
    """
    Convert datetime value to a string, localized for the specified timezone.

    :param dt: datetime value.
    :param use_tz: whether to use the specified timezone.
    :return: datetime as a string, localized for the specified timezone.
    """
    if not dt.tzinfo and not use_tz:
        return dt.strftime(DT_NAIVE)
    if not dt.tzinfo:
        return dt.replace(tzinfo=use_tz).strftime(DT_AWARE)
    return dt.astimezone(use_tz).strftime(DT_AWARE) if use_tz else dt.strftime(DT_AWARE)


def get_local_utcoffset() -> timezone:
    """Get UTC offset from local system and return as timezone object."""
    utc_offset = timedelta(seconds=time.localtime().tm_gmtoff)
    return timezone(offset=utc_offset)


def make_tzaware(
    dt: datetime,
    use_tz: tzinfo | None = None,
    localize: bool = True,
) -> datetime:
    """Make a naive datetime object timezone-aware."""
    if not use_tz:
        use_tz = get_local_utcoffset()
    if localize:
        return dt.astimezone(use_tz)
    return dt.replace(tzinfo=use_tz)


def dtaware_fromtimestamp(timestamp: float, use_tz: tzinfo | None = None) -> datetime:
    """
    Get time-zone aware datetime object from UNIX timestamp.

    :param timestamp: UNIX timestamp.
    :param use_tz: Time zone info to use.
    :return: datetime object, localized to given time zone (or to local by default).
    """
    timestamp_naive = datetime.fromtimestamp(timestamp)
    timestamp_aware = timestamp_naive.replace(tzinfo=get_local_utcoffset())
    return timestamp_aware.astimezone(use_tz) if use_tz else timestamp_aware


def remaining_fromtimestamp(timestamp: float) -> Timespan:
    """
    Calculate time remaining from now until UNIX timestamp value.

    :param timestamp: UNIX timestamp.
    :return: Time remaining from now until UNIX timestamp value.
    """
    now = datetime.now(timezone.utc)
    dt_aware = dtaware_fromtimestamp(timestamp, use_tz=timezone.utc)
    if dt_aware < now:
        return Timespan()
    return Timespan.from_timedelta(dt_aware - now)


def format_timedelta_digits(td: timedelta) -> str:
    """Format a timedelta object as a string resembling a digital display."""
    return Timespan.from_timedelta(td).digital


def format_timedelta_str(td: timedelta) -> str:
    """Format a timedelta object as a human-readable string."""
    return Timespan.from_timedelta(td).pretty
