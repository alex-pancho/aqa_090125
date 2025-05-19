import pytest
from calculator import add, subtract, multiply, divide

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_subtract_positive_numbers():
    assert subtract(5, 2) == 3

def test_multiply_positive_numbers():
    assert multiply(4, 3) == 12

def test_divide_positive_numbers():
    assert divide(10, 2) == 5

def test_add_negative_numbers():
    assert add(-1, -4) == -5

def test_multiply_with_zero():
    assert multiply(7, 0) == 0