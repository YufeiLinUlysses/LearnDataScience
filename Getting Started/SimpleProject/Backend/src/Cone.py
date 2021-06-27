import numpy as np

from Shape import Shape
from Tuple import Tuple
from Intersection import Intersection
# ---------------------
""" 
Cone class helps to describe a cone with a center at point(0,0,0)
It inherits all elements from shape

Cone class contains the following functions:
__init__
localIntersect
localNormalAt
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/ConeTest.py
    --- OR ---- 
    python3 -m nose -v ../test/ConeTest.py
    --- OR ---- 
    python -m nose -v ../test/ConeTest.py
    ---------------------------------------------------
"""


class Cone(Shape):
    # ---------------------
    """
    Cone class takes in a minimum and a maximum to describe the height of a cone
    """
    # ---------------------

    def __init__(self, minimum=float("-inf"), maximum=float("inf"), closed=False):
        super().__init__()
        self.minimum = minimum
        self.maximum = maximum
        self.closed = closed

    # ---------------------
    """
    Define equivalence of two Cube instances
    """
    # ---------------------

    def __eq__(self, cone2: "Cone"):
        if type(cone2).__name__ != "Cone":
            return False
        return self.material == cone2.material and self.transform == cone2.transform

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
            yVal = max(self.maximum, self.minimum)
            return (x*x + z*z) <= yVal * yVal

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
        a = ray.direction.x ** 2 + ray.direction.z**2 - ray.direction.y ** 2
        b = 2*ray.origin.x*ray.direction.x + 2*ray.origin.z * \
            ray.direction.z - 2 * ray.origin.y * ray.direction.y
        c = ray.origin.x**2 + ray.origin.z**2 - ray.origin.y**2
        if abs(a) < 0.00001 and abs(b) < 0.00001:
            return intersectCap(xs)
        elif abs(a) < 0.00001:
            xs.append(Intersection(-c/(2*b), self))
        else:
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
        nosetests -v ../test/ConeTest.py:test_intersect
        --- OR ---- 
        python3 -m nose -v ../test/ConeTest.py:test_intersect
        --- OR ---- 
        python -m nose -v ../test/ConeTest.py:test_intersect
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
        y = dist ** 0.5
        if point.y > 0:
            y = -y
        return Tuple.vector(point.x, y, point.z)
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/ConeTest.py:test_normalAt
        --- OR ---- 
        python3 -m nose -v ../test/ConeTest.py:test_normalAt
        --- OR ---- 
        python -m nose -v ../test/ConeTest.py:test_normalAt
        ---------------------------------------------------
    """
