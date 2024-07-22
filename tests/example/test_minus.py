import pytest
import test3


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0),
    (1, 2, -1),
    (2, 1, 1),
    (2, 2, 0),
])
def test_minus(a, b, expected):
    assert test3.example.minus.minus(a, b) == expected
