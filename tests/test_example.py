# tests/test_example.py
import pytest
from app.myapp import add, subtract  # Import the functions to test

# Test for the add function
def test_add():
    result = add(2, 3)  # Expected result is 5
    assert result == 5, f"Expected 5, but got {result}"  # Check if the result is correct

# Test for the subtract function
def test_subtract():
    result = subtract(5, 3)  # Expected result is 2
    assert result == 2, f"Expected 2, but got {result}"  # Check if the result is correct

# Test with negative numbers
def test_add_negative():
    result = add(-1, 1)  # Expected result is 0
    assert result == 0, f"Expected 0, but got {result}"

# Test with zero
def test_add_zero():
    result = add(0, 0)  # Expected result is 0
    assert result == 0, f"Expected 0, but got {result}"

def test_subtract_negative():
    result = subtract(-5, -3)  # Expected result is -2
    assert result == -2, f"Expected -2, but got {result}"
