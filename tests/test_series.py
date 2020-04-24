import pytest
from math_series.series import fibonacci, lucas


@pytest.mark.parametrize(
    "test_input, expected", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13)]
)
def test_fibonacci(test_input, expected):
    assert fibonacci(test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected", [(0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11), (6, 18), (7, 29)]
)
def test_lucas(test_input, expected):
    assert lucas(test_input) == expected
