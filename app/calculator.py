from calculator import add, subtract

import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import add, subtract

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
