import numpy as np

from Shape import Shape
from Tuple import Tuple
from Intersection import Intersection
# ---------------------
""" 
Cube class helps to describe a cube with a center at point(0,0,0)
It inherits all elements from shape

Cube class contains the following functions:
__init__
localIntersect
localNormalAt
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/CubeTest.py
    --- OR ---- 
    python3 -m nose -v ../test/CubeTest.py
    --- OR ---- 
    python -m nose -v ../test/CubeTest.py
    ---------------------------------------------------
"""


class Cube(Shape):
    # ---------------------
    """
    Cube class takes in no input
    """
    # ---------------------

    def __init__(self):
        super().__init__()

    # ---------------------
    """
    Define equivalence of two Cube instances
    """
    # ---------------------

    def __eq__(self, cube2: "Cube"):
        if type(cube2).__name__ != "Cube":
            return False
        return self.material == cube2.material and self.transform == cube2.transform

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
        def checkAxis(origin, direction):
            tminNumerator = (-1-origin)
            tmaxNumerator = (1-origin)
            if abs(direction) >= 0.00001:
                tmin = tminNumerator/direction
                tmax = tmaxNumerator/direction
            else:
                tmin = tminNumerator * float(np.Infinity)
                tmax = tmaxNumerator * float(np.Infinity)
            if tmin > tmax:
                tmin, tmax = tmax, tmin
            return tmin, tmax
        xtmin, xtmax = checkAxis(ray.origin.x, ray.direction.x)
        ytmin, ytmax = checkAxis(ray.origin.y, ray.direction.y)
        ztmin, ztmax = checkAxis(ray.origin.z, ray.direction.z)

        tmin = max(xtmin, ytmin, ztmin)
        tmax = min(xtmax, ytmax, ztmax)
        if tmin > tmax:
            return 0, []
        return 2, [Intersection(tmin, self), Intersection(tmax, self)]

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
        maxc = max(abs(point.x), abs(point.y), abs(point.z))
        if maxc - abs(point.x) <= 0.0001:
            return Tuple.vector(point.x, 0, 0)
        elif maxc - abs(point.y) <= 0.0001:
            return Tuple.vector(0, point.y, 0)
        return Tuple.vector(0, 0, point.z)
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/CubeTest.py:test_normalAt
        --- OR ---- 
        python3 -m nose -v ../test/CubeTest.py:test_normalAt
        --- OR ---- 
        python -m nose -v ../test/CubeTest.py:test_normalAt
        ---------------------------------------------------
    """
