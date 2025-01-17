import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import add, subtract

# example.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
