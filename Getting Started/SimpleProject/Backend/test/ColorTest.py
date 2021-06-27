from Backend.src.Color import Color
import numpy as np


# ---------------------------------------------------


def test_add():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)
    assert c1 + c2 == Color(1.6, 0.7, 1.0)

# ---------------------------------------------------


def test_subtract():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)
    assert c1 - c2 == Color(0.2, 0.5, 0.5)

# ---------------------------------------------------


def test_multi():
    c1 = Color(0.2, 0.3, 0.4)
    s = 2
    assert c1 * s == Color(0.4, 0.6, 0.8)

    c1 = Color(1, 0.2, 0.4)
    c2 = Color(0.9, 1, 0.1)
    assert c1 * c2 == Color(0.9, 0.2, 0.04)
    
