import pytest
from calculator import is_even

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (7, False),
    (0, True),
    (-4, True),
])
def test_is_even(number, expected):
    assert is_even(number) == expected
