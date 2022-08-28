import pytest
from yaba.apps.budget.coolf import coolf


@pytest.mark.parametrize(
    'x, y, expected',
    (
        (1, 2, 2),
        (100, 200, 299),
    ),
)
def test_coolf(x, y, expected) -> None:
    '''Test coolf.'''
    result = coolf(x, y)
    assert result == expected
