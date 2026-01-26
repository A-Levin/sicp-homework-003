import pytest
from count_digits import count_digits


def test_count_digits_12345():
    assert count_digits(12345) == 5

def test_count_digits_7():
    assert count_digits(7) == 1

def test_count_digits_100():
    assert count_digits(100) == 3

def test_count_digits_0():
    assert count_digits(0) == 1

def test_count_digits_999999():
    assert count_digits(999999) == 6
