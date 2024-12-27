# tests/test_example.py
from tests/test_example.py
# Test the add function
def test_addition():
    result = add(3, 5)
    assert result == 8, f"Expected 8, but got {result}"

# Test the subtract function
def test_subtraction():
    result = subtract(10, 4)
    assert result == 6, f"Expected 6, but got {result}"

# Optionally, you can also add edge case tests
def test_addition_negative():
    result = add(-1, -1)
    assert result == -2, f"Expected -2, but got {result}"

def test_subtraction_zero():
    result = subtract(0, 0)
    assert result == 0, f"Expected 0, but got {result}"
