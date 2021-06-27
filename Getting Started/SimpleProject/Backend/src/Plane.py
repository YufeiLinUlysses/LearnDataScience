from Shape import Shape
from Tuple import Tuple
from Intersection import Intersection
# ---------------------
""" 
Plane class helps to describe a plane with a center at point(0,0,0)
It inherits all elements from shape

Plane class contains the following functions:
__init__
localIntersect
localNormalAt
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/PlaneTest.py
    --- OR ---- 
    python3 -m nose -v ../test/PlaneTest.py
    --- OR ---- 
    python -m nose -v ../test/PlaneTest.py
    ---------------------------------------------------
"""


class Plane(Shape):
    # ---------------------
    """
    Plane class takes in no input
    """
    # ---------------------

    def __init__(self):
        super().__init__()

    # ---------------------
    """
    Define equivalence of two Plane instances
    """
    # ---------------------

    def __eq__(self, plane2: "Plane"):
        if type(plane2).__name__ != "Plane":
            return False
        return self.material == plane2.material and self.transform == plane2.transform

    # ---------------------
    """
    Find the intersection between the ray and the plane
    ---- Inputs: --------
        * ray: a Ray 
    ---- Outputs: --------
        * count: a scalar, the number of intersections
        * results: a tuple, all intersections are listed
    """
    # ---------------------

    def localIntersect(self, ray: "Ray"):
        if abs(ray.direction.y) < 0.00001:
            return 0, ()
        return 1, [Intersection(-ray.origin.y/ray.direction.y, self), ]
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/PlaneTest.py:test_intersect
        --- OR ---- 
        python3 -m nose -v ../test/PlaneTest.py:test_intersect
        --- OR ---- 
        python -m nose -v ../test/PlaneTest.py:test_intersect
        ---------------------------------------------------
    """

    # ---------------------
    """
    Find the normal at a certain point of the Plane
    ---- Inputs: --------
        * point: a Tuple, indicating a point on the Plane
        * hit: an Intersection, just follow the definition of shape localNormalAt
    ---- Outputs: --------
        * vector: the normal vector
    """
    # ---------------------

    def localNormalAt(self, point: "Tuple"):
        return Tuple.vector(0, 1, 0)
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/PlaneTest.py:test_normalAt
        --- OR ---- 
        python3 -m nose -v ../test/PlaneTest.py:test_normalAt
        --- OR ---- 
        python -m nose -v ../test/PlaneTest.py:test_normalAt
        ---------------------------------------------------
    """
