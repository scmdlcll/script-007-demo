import pytest

from tests.myfuncs import myadd


@pytest.mark.parametrize("num1, num2, sum", [
    (0, 0, 0),
    (1, 2, 3),
    (11, -5, 6),
    # (11, 5, 6),  # broken
])
def test_myadd(num1, num2, sum):
    assert myadd(num1, num2) == sum
