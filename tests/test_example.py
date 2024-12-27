# tests/test_app.py

import pytest
from app import some_function  # Example function from your app to test

def test_some_function():
    result = some_function(2, 3)
    assert result == 5  # Check that the function works as expected
