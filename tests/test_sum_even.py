import pytest
from sum_even import sum_even


def test_sum_even_10():
    assert sum_even(10) == 30

def test_sum_even_7():
    assert sum_even(7) == 12

def test_sum_even_2():
    assert sum_even(2) == 2

def test_sum_even_1():
    assert sum_even(1) == 0

def test_sum_even_0():
    assert sum_even(0) == 0

def test_sum_even_100():
    assert sum_even(100) == 2550
