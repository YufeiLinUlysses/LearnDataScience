from Tuple import Tuple
# ---------------------
""" 
Intersection class helps to save a intersection point of the shape and the ray
It contains two elements: t, object
t: a scalar recording the intersection is t unit apart from the ray's origin
shape: the shape used to be intersected with the given ray

Intersection class contains the following functions:
__init__
__eq__
hit
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/IntersectionTest.py
    --- OR ---- 
    python3 -m nose -v ../test/IntersectionTest.py
    --- OR ---- 
    python -m nose -v ../test/IntersectionTest.py
    ---------------------------------------------------
"""


class Intersection():
    # ---------------------
    """
    Intersection class takes in no input
    t is the intersection point
    shape is the shape used to make calculation
    """
    # ---------------------

    def __init__(self, t: float = None, shape=None, u=None, v=None):
        self.t = t
        self.shape = shape
        self.u = u
        self.v = v

    # ---------------------
    """
    Define equivalence of two Intersection instances
    """
    # ---------------------

    def __eq__(self, i2: "Intersection"):
        if i2 == None:
            return False
        return self.t == i2.t and self.shape == i2.shape and self.u == i2.u and self.v == i2.v

    # ---------------------
    """
    Define the print format of Intersection instances
    """
    # ---------------------

    def __str__(self):
        return "t:" + str(self.t) + "\n" + "shape:" + str(self.shape)+"\n" + "u:" + str(self.u) + "\n" + "v:" + str(self.v) + "\n"

    # ---------------------
    """
    Find the intersection with the smallest t-value, ignore those negative values
    ---- Inputs: --------
        * xs: a list of intersections
    ---- Outputs: --------
        * results: the intersection with the smallest non-negative t-value or empty Intersection instance
    """
    # ---------------------
    @staticmethod
    def hit(xs):
        xs = [i for i in xs if i.t >= 0]
        if len(xs) == 0:
            return Intersection()
        return min(xs, key=lambda x: x.t)
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/IntersectionTest.py:test_hit
        --- OR ---- 
        python3 -m nose -v ../test/IntersectionTest.py:test_hit
        --- OR ---- 
        python -m nose -v ../test/IntersectionTest.py:test_hit
        ---------------------------------------------------
    """
