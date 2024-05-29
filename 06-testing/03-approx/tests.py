import pytest
from pytest import approx
from mystatistics import *


@pytest.mark.parametrize("ns, expected", [
    ([0.1, 0.1, 0.1], 0.1),
    ([1, 2, 3], 2)
])
def test_average(ns, expected):
    assert average(ns) == approx(expected, abs=0.1)