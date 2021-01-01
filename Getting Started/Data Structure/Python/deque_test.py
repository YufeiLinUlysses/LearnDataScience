from deque import *

"""
    nosetests -v deque_test.py
    nosetests -v deque_test.py:funcName
"""

def test_checkPal():
    assert checkPal("radar") == True
    assert checkPal("lsdkfjfskf") == False
    
