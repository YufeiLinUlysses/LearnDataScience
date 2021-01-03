import queue as q


"""
    nosetests -v queue_test.py
    nosetests -v queue_test.py:funcName
"""


def test_joseph():
    assert q.joseph(["Bill", "David", "Susan", "Jane",
                          "Kent", "Brad"], 7) == "Susan"
