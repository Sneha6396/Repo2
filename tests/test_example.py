import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.calculator import add, subtract

def test_add():
    # This test will pass
    assert add(2, 3) == 5

def test_subtract():
    # This test will fail
    assert subtract(10, 5) == 6 
