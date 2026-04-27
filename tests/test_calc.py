import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculadora import soma, sub, mult, div

def test_soma():
    assert soma(2, 3) == 5

def test_sub():
    assert sub(5, 2) == 3

def test_mult():
    assert mult(3, 4) == 12

def test_div():
    assert div(10, 2) == 5

def test_div_float():
    assert div(5, 2) == 2.5