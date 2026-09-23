# test_app.py
import pytest
from hypothesis import given, strategies as st


# Application functions
def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(a, b):
    return add(a, b), divide(a, b)


# Unit test
def test_add():
    assert add(10, 20) == 30


# Unit test for exception
def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


# Hypothesis property-based test
@given(st.integers(), st.integers())
def test_add_hypothesis(a, b):
    assert add(a, b) == a + b


# Integration test
def test_calculate():
    result = calculate(20, 5)
    assert result == (25, 4)