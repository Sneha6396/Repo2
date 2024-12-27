# test_example.py
import pytest
from app.myapp import add  # Import the function to be tested

def test_add_function():
    # Testing a simple add function
    result = add(2, 3)
    assert result == 5  # This should pass if the function works correctly
