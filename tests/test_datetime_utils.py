import pytest

from monet.utils.datetime_utils import Timespan


@pytest.mark.parametrize(
    "kwargs," "expected_total_seconds," "expected_total_milliseconds," "expected_total_microseconds,",
    (
        (
            {
                "days": 0,
                "hours": 0,
                "minutes": 0,
                "seconds": 0,
                "milliseconds": 0,
                "microseconds": 0,
            },
            0,
            0,
            0,
        ),
        (
            {
                "days": 1,
                "hours": 0,
                "minutes": 0,
                "seconds": 0,
                "milliseconds": 0,
                "microseconds": 0,
            },
            86400,
            86400000,
            86400000000,
        ),
        (  # TODO: this should not pass, but it does
            {
                "days": 1,
                "hours": 0,
                "minutes": 0,
                "seconds": 0,
                "milliseconds": 1,
                "microseconds": 0,
            },
            86400,
            86400000,
            86400000000,
        ),
    ),
)
def test_timespan(
    kwargs: dict[str, int],
    expected_total_seconds: int,
    expected_total_milliseconds: int,
    expected_total_microseconds: int,
) -> None:
    """Test :class:`Timespan` totals calculations."""
    ts = Timespan(**kwargs)
    assert ts.total_seconds == expected_total_seconds
    assert ts.total_milliseconds == expected_total_milliseconds
    assert ts.total_microseconds == expected_total_microseconds
