import pytest
from product_digits import product_digits


def test_product_digits_12345():
    assert product_digits(12345) == 120

def test_product_digits_99():
    assert product_digits(99) == 81

def test_product_digits_10():
    assert product_digits(10) == 0

def test_product_digits_7():
    assert product_digits(7) == 7

def test_product_digits_111():
    assert product_digits(111) == 1

def test_product_digits_23():
    assert product_digits(23) == 6
