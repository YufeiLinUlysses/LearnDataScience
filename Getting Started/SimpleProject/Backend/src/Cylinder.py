import numpy as np

from Shape import Shape
from Tuple import Tuple
from Intersection import Intersection
# ---------------------
""" 
Cylinder class helps to describe a cylinder with a center at point(0,0,0)
It inherits all elements from shape

Cylinder class contains the following functions:
__init__
localIntersect
localNormalAt
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/CylinderTest.py
    --- OR ---- 
    python3 -m nose -v ../test/CylinderTest.py
    --- OR ---- 
    python -m nose -v ../test/CylinderTest.py
    ---------------------------------------------------
"""


class Cylinder(Shape):
    # ---------------------
    """
    Cylinder class takes in a minimum and a maximum to describe the height of a cylinder
    """
    # ---------------------

    def __init__(self, minimum=float("-inf"), maximum=float("inf"), closed=False):
        super().__init__()
        self.minimum = minimum
        self.maximum = maximum
        self.closed = closed

    # ---------------------
    """
    Define equivalence of two Cylinder instances
    """
    # ---------------------

    def __eq__(self, cylinder2: "Cylinder"):
        if type(cylinder2).__name__ != "Cylinder":
            return False
        return self.material == cylinder2.material and self.transform == cylinder2.transform

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
        def checkCaps(t):
            x = ray.origin.x + t*ray.direction.x
            z = ray.origin.z + t*ray.direction.z
            return (x*x + z*z) <= 1

        def intersectCap(xs):
            if not self.closed or abs(ray.direction.y) < 0.00001:
                return len(xs), xs
            t = (self.minimum - ray.origin.y)/ray.direction.y
            if checkCaps(t):
                xs.append(Intersection(t, self))
            t = (self.maximum - ray.origin.y)/ray.direction.y
            if checkCaps(t):
                xs.append(Intersection(t, self))
            return len(xs), xs
        xs = []
        a = ray.direction.x ** 2 + ray.direction.z**2
        if a < 0.0001:
            return intersectCap(xs)
        b = 2*ray.origin.x*ray.direction.x + 2*ray.origin.z*ray.direction.z
        c = ray.origin.x**2 + ray.origin.z**2 - 1
        disc = b*b-4*a*c
        if disc < 0:
            return 0, ()
        t0 = (-b-disc**0.5)/(2*a)
        t1 = (-b+disc**0.5)/(2*a)
        if t0 > t1:
            t0, t1 = t1, t0
        y0 = ray.origin.y + t0*ray.direction.y
        if self.minimum < y0 < self.maximum:
            xs.append(Intersection(t0, self))
        y1 = ray.origin.y + t1*ray.direction.y
        if self.minimum < y1 < self.maximum:
            xs.append(Intersection(t1, self))
        return intersectCap(xs)
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/CylinderTest.py:test_intersect
        --- OR ---- 
        python3 -m nose -v ../test/CylinderTest.py:test_intersect
        --- OR ---- 
        python -m nose -v ../test/CylinderTest.py:test_intersect
        ---------------------------------------------------
    """

    # ---------------------
    """
    Find the normal at a certain point of the Cube
    ---- Inputs: --------
        * point: a Tuple, indicating a point on the Cube 
    ---- Outputs: --------
        * vector: the normal vector
    """
    # ---------------------

    def localNormalAt(self, point: "Tuple"):
        dist = point.x * point.x + point.z * point.z
        if dist < 1 and point.y >= self.maximum-0.00001:
            return Tuple.vector(0, 1, 0)
        elif dist < 1 and point.y <= self.minimum + 0.00001:
            return Tuple.vector(0, -1, 0)
        return Tuple.vector(point.x, 0, point.z)
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/CylinderTest.py:test_normalAt
        --- OR ---- 
        python3 -m nose -v ../test/CylinderTest.py:test_normalAt
        --- OR ---- 
        python -m nose -v ../test/CylinderTest.py:test_normalAt
        ---------------------------------------------------
    """
