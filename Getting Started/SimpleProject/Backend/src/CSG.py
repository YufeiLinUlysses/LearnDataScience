import numpy as np

from Shape import Shape
from Tuple import Tuple
from Intersection import Intersection


# ---------------------
""" 
CSG class helps to describe a shape that is built by some combinations of two shapes
The combinations it supports are union, intersection and difference
It inherits all elements from shape

This files contains two parts:
includes function
CSG class

CSG class contains the following functions:
__init__
intersectionAllowed
filterIntersection
localIntersect
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/CSGTest.py
    --- OR ---- 
    python3 -m nose -v ../test/CSGTest.py
    --- OR ---- 
    python -m nose -v ../test/CSGTest.py
    ---------------------------------------------------
"""

# ---------------------
"""
includes check whehter shape1 includes shape2
---- Inputs: --------
    * s1: a Shape, shape1
    * s2: a Shape, shape2
---- Outputs: --------
    * includes: a bool, whether shape1 includes shape2
"""
# ---------------------


def includes(s1, s2):
    if type(s1).__name__ == "CSG":
        return s1.left.includes(s2) or s1.right.includes(s2)
    if type(s1).__name__ == "Group":
        for i in s1.objects:
            if i.includes(s2):
                return True
        return False
    return s1 == s2


# -----------------
"""  
    Make sure you are on ~/src
    this is tested within filterIntersection in CSG class
"""


class CSG(Shape):
    # ---------------------
    """
    Cube class takes in no input
    """
    # ---------------------

    def __init__(self, shape1, shape2, operation: "str"):
        super().__init__()
        self.left = shape1
        self.right = shape2
        self.operation = operation
        shape1.parent = self
        shape2.parent = self

    # ---------------------
    """
    Define equivalence of two Cube instances
    """
    # ---------------------

    def __eq__(self, csg2: "CSG"):
        if type(csg2).__name__ != "CSG":
            return False
        return self.s1 == csg2.s1 and self.s2 == csg2.s2 and self.operation == csg2.operation

    # ---------------------
    """
    Intersection allowed helps to determine whehter there is a intersection
    ---- Inputs: --------
        * lhit: a boolean, indicate whether there is a left hit
        * inl: a boolean, indicate whether there is a inner left hit
        * inr: a boolean, indicates whether there is a inner right hit
    ---- Outputs: --------
        * allowed: a boolean, indicates whether the intersection is allowed
    """
    # ---------------------

    def intersectionAllowed(self, lhit: bool, inl: bool, inr: bool):
        if self.operation == "union":
            return (lhit and not inr) or (not lhit and not inl)
        elif self.operation == "intersect":
            return (lhit and inr) or (not lhit and inl)
        elif self.operation == "difference":
            return (lhit and not inr) or (not lhit and inl)
        return False

    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/CubeTest.py:test_intersectionAllowed
        --- OR ---- 
        python3 -m nose -v ../test/CubeTest.py:test_intersectionAllowed
        --- OR ---- 
        python -m nose -v ../test/CubeTest.py:test_intersectionAllowed
        ---------------------------------------------------
    """

    # ---------------------
    """
    filterIntersection helps to find the valid intersections based on intersectionAllowed
    ---- Inputs: --------
        * xs: a list of Intersections
    ---- Outputs: --------
        * result: a list of Intersections
    """
    # ---------------------

    def filterIntersection(self, xs):
        inl = False
        inr = False
        result = []
        for i in xs:
            lhit = includes(self.left, i.shape)
            tmp = self.intersectionAllowed(lhit, inl, inr)
            if self.intersectionAllowed(lhit, inl, inr):
                result.append(i)
            if lhit:
                inl = not inl
            else:
                inr = not inr
        return result

    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/CubeTest.py:test_filterIntersection
        --- OR ---- 
        python3 -m nose -v ../test/CubeTest.py:test_filterIntersection
        --- OR ---- 
        python -m nose -v ../test/CubeTest.py:test_filterIntersection
        ---------------------------------------------------
    """

    # ---------------------
    """
    Find the intersection between the ray and the cube
    ---- Inputs: --------
        * ray: a Ray 
    ---- Outputs: --------
        * count: a scalar, the number of intersections
        * results: a tuple, all intersections are listed
    """
    # ---------------------

    def localIntersect(self, ray: "Ray"):
        countLeft, leftXs = self.left.intersect(ray)
        countRight, rightXs = self.right.intersect(ray)
        xs = leftXs + rightXs
        xs = sorted(xs, key=lambda x: x.t)
        result = self.filterIntersection(xs)
        return len(result), result
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/CubeTest.py:test_intersect
        --- OR ---- 
        python3 -m nose -v ../test/CubeTest.py:test_intersect
        --- OR ---- 
        python -m nose -v ../test/CubeTest.py:test_intersect
        ---------------------------------------------------
    """
