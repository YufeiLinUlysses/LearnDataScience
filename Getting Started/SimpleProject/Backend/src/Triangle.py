import numpy as np

from Shape import Shape
from Tuple import Tuple
from Intersection import Intersection
# ---------------------
""" 
Triangle class helps to describe a triangle in the world,
it is established based on the input point values. 
It could be used to form a large shape by different combinations. 
It is useful for reading obj files
It inherits all elements from shape

Here, we combine the definition of smooth triangle and triangle together.
If you input n1,n2 and n3 for a triangle, it would be a smooth triangle.

Cone class contains the following functions:
__init__
localIntersect
localNormalAt
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/TriangleTest.py
    --- OR ---- 
    python3 -m nose -v ../test/TriangleTest.py
    --- OR ---- 
    python -m nose -v ../test/TriangleTest.py
    ---------------------------------------------------
"""


class Triangle(Shape):
    # ---------------------
    """
    Triangle class takes in three points to describe the three corners of the triangle
    """
    # ---------------------

    def __init__(self, p1: "Tuple", p2: "Tuple", p3: "Tuple", n1: "Tuple" = None, n2: "Tuple" = None, n3: "Tuple" = None):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.e1 = p2-p1
        self.e2 = p3-p1
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.normal = (self.e2.cross(self.e1)).normalize()
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TriangleTest.py:test_init
        --- OR ---- 
        python3 -m nose -v ../test/TriangleTest.py:test_init
        --- OR ---- 
        python -m nose -v ../test/TriangleTest.py:test_init
        ---------------------------------------------------
    """

    # ---------------------
    """
    Define equivalence of two Triangle instances
    """
    # ---------------------

    def __eq__(self, t2: "Triangle"):
        if type(t2).__name__ != "Triangle":
            return False
        return self.material == t2.material and self.transform == t2.transform and t2.p1 == self.p1 and t2.p2 == self.p2 and t2.p3 == self.p3

    # ---------------------
    """
    Define print format for triangle instances
    """
    # ---------------------

    def __str__(self):
        result = "p1:"+str(self.p1)+"\n" + "p2:" + \
            str(self.p2)+"\n"+"p3:"+str(self.p3)+"\n"
        if self.n1 != None:
            result += "n1:"+str(self.n1) + "\n" + "n2: " + \
                str(self.n2) + "\n" + "n3: "+str(self.n3) + "\n"
        return result

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
        de2 = ray.direction.cross(self.e2)
        det = self.e1.dot(de2)
        if abs(det) < 0.00001:
            return 0, []
        f = 1/det
        op1 = ray.origin-self.p1
        u = op1.dot(de2) * f
        if u < 0 or u > 1:
            return 0, []
        oe1 = op1.cross(self.e1)
        v = ray.direction.dot(oe1)*f
        if v < 0 or (u+v) > 1:
            return 0, []
        t = self.e2.dot(oe1)
        if self.n1 != None:
            return 1, [Intersection(t, self, u, v), ]
        return 1, [Intersection(t, self), ]
        # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TriangleTest.py:test_intersect
        --- OR ---- 
        python3 -m nose -v ../test/TriangleTest.py:test_intersect
        --- OR ---- 
        python -m nose -v ../test/TriangleTest.py:test_intersect
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

    def localNormalAt(self, point: "Tuple", **kwargs):
        if "hit" not in kwargs:
            return self.normal
        hit = kwargs["hit"]
        return self.n2 * hit.u + self.n3 * hit.v + self.n1 * (1-hit.u-hit.v)
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TriangleTest.py:test_normalAt
        --- OR ---- 
        python3 -m nose -v ../test/TriangleTest.py:test_normalAt
        --- OR ---- 
        python -m nose -v ../test/TriangleTest.py:test_normalAt
        ---------------------------------------------------
    """
