from stack import *

"""
    nosetests -v stack_test.py
    nosetests -v stack_test.py:funcName
"""


def test_checkParenthesis():
    assert checkParenthesis("((()))") == True
    assert checkParenthesis("(()") == False
    assert checkParenthesis("([)]") == False
    assert checkParenthesis("{([)]}") == False


def test_decimalToBase():
    assert decimalToBase(3, 2) == "11"
    assert decimalToBase(3, 3) == "10"
    assert decimalToBase(3, 4) == "3"
    assert decimalToBase(16, 16) == "10"
    assert decimalToBase(15, 16) == "F"


def test_toPostFix():
    assert toPostFix("A+B*C") == "A B C * +"
    assert toPostFix("(A+B)*C") == "A B + C *"

def test_postFixEval():
    assert postFixEval(toPostFix("(3+2)/5")) == 1.0
    assert postFixEval(toPostFix("3*4-5")) == 7
