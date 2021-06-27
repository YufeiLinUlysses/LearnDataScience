from Shape import Shape
from Tuple import Tuple
from Material import Material
from Intersection import Intersection
# ---------------------
""" 
Sphere class helps to describe a sphere with a center at point(0,0,0)
It inherits all elements from shape
It contains a center element
center: a Tuple marks the center of the sphere

Sphere class contains the following functions:
__init__
localIntersect
localNormalAt
glassSphere
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/SphereTest.py
    --- OR ---- 
    python3 -m nose -v ../test/SphereTest.py
    --- OR ---- 
    python -m nose -v ../test/SphereTest.py
    ---------------------------------------------------
"""


class Sphere(Shape):
    # ---------------------
    """
    Sphere class takes in no input
    center is the center point of sphere
    """
    # ---------------------

    def __init__(self):
        super().__init__()

    # ---------------------
    """
    Define equivalence of two Sphere instances
    """
    # ---------------------

    def __eq__(self, sphere2: "Sphere"):
        if type(sphere2).__name__ != "Sphere":
            return False
        return self.center == sphere2.center and self.material == sphere2.material and self.transform == sphere2.transform

    # ---------------------
    """
    Find the intersection between the ray and the sphere
    ---- Inputs: --------
        * ray: a Ray 
    ---- Outputs: --------
        * count: a scalar, the number of intersections
        * results: a tuple, all intersections are listed
    """
    # ---------------------

    def localIntersect(self, ray: "Ray"):
        sphereToRay = ray.origin-self.center
        a = ray.direction.dot(ray.direction)
        b = 2 * ray.direction.dot(sphereToRay)
        c = sphereToRay.dot(sphereToRay) - 1
        discriminant = b*b - 4*a*c
        if discriminant < 0:
            return 0, []

        elif discriminant == 0:
            return 1, [Intersection((-b-discriminant**0.5)/(2*a), self), ]
        t1 = (-b-discriminant**0.5)/(2*a)
        t1 = Intersection(t1, self)
        t2 = (-b+discriminant**0.5)/(2*a)
        t2 = Intersection(t2, self)
        return 2, [t1, t2]
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/SphereTest.py:test_intersect
        --- OR ---- 
        python3 -m nose -v ../test/SphereTest.py:test_intersect
        --- OR ---- 
        python -m nose -v ../test/SphereTest.py:test_intersect
        ---------------------------------------------------
    """

    # ---------------------
    """
    Find the normal at a certain point of the sphere
    ---- Inputs: --------
        * point: a Tuple, indicating a point on the sphere 
    ---- Outputs: --------
        * vector: the normal vector
    """
    # ---------------------

    def localNormalAt(self, point: "Tuple"):
        return point-self.center
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/SphereTest.py:test_normalAt
        --- OR ---- 
        python3 -m nose -v ../test/SphereTest.py:test_normalAt
        --- OR ---- 
        python -m nose -v ../test/SphereTest.py:test_normalAt
        ---------------------------------------------------
    """

    # ---------------------
    """
    glassSphere method creates a glass sphere with transparency of 1 and refractive index 1.5
    ---- Outputs: --------
        * s: a Sphere
    """
    # ---------------------
    @staticmethod
    def glassSphere():
        s = Sphere()
        s.material = Material(transparency=1, refractiveIndex=1.5)
        return s
