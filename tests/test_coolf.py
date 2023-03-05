import pytest

from yaba.apps.budget.coolf import coolf


@pytest.mark.parametrize(
    'x, y, expected',
    (
        (1, 2, 2),
        (100, 200, 299),
    ),
)
def test_coolf(x: int, y: int, expected: int) -> None:
    '''Test coolf.'''
    result = coolf(x, y)
    assert result == expected
