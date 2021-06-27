import numpy as np

from Shape import Shape
from Tuple import Tuple
from Intersection import Intersection
# ---------------------
""" 
Group class helps to describe a collection of multiple shapes and they would be transformed together
It inherits all elements from shape
The group's normal is calculated within each sub shapes.
It has an array of shapes

Group class contains the following functions:
__init__
localIntersect
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/GroupTest.py
    --- OR ---- 
    python3 -m nose -v ../test/GroupTest.py
    --- OR ---- 
    python -m nose -v ../test/GroupTest.py
    ---------------------------------------------------
"""


class Group(Shape):
    # ---------------------
    """
    Group class takes in no input
    """
    # ---------------------

    def __init__(self, objs=None):
        super().__init__()
        if objs == None:
            self.objects = []
        else:
            for i in objs:
                i.parent = self
            self.objects = objs

    # ---------------------
    """
    Define equivalence of two Cube instances
    """
    # ---------------------

    def __eq__(self, group2: "Group"):
        if type(group2).__name__ != "Group":
            return False
        if len(self.objects) != len(group2.objects):
            return False
        for i in range(len(self.objects)):
            if self.objects[i] != group2.objects[i]:
                return False
        return True

    # ---------------------
    """
    Add child addas a shape to the object array of the group
    ---- Inputs: --------
        * shape: a Shape, that is any form like sphere, cube, cylinder or cone
    """
    # ---------------------

    def addChild(self, shape):
        shape.parent = self
        self.objects.append(shape)

    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/GroupTest.py:test_addChild
        --- OR ---- 
        python3 -m nose -v ../test/GroupTest.py:test_addChild
        --- OR ---- 
        python -m nose -v ../test/GroupTest.py:test_addChild
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
        xs = []
        c = 0
        for i in self.objects:
            count, result = i.intersect(ray)
            c += count
            xs += result
        xs = sorted(xs, key=lambda x: x.t)
        return c, xs
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/GroupTest.py:test_intersect
        --- OR ---- 
        python3 -m nose -v ../test/GroupTest.py:test_intersect
        --- OR ---- 
        python -m nose -v ../test/GroupTest.py:test_intersect
        ---------------------------------------------------
    """
