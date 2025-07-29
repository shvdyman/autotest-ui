import pytest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0

@pytest.mark.parametrize('number, excepted', [ (1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, excepted: int):
    assert number ** 2 == excepted
    