from recursion import *

"""
    nosetests -v recursion_test.py
    nosetests -v recursion_test.py:funcName
"""


def test_listSum():
    assert listSum(numList=[1, 2, 3]) == 6

def test_changeBase():
    assert changeBase(1453, 16) == "5AD"