from Tuple import Tuple
from Intersection import Intersection
from Ray import Ray
# ---------------------
""" 
Computation class helps to save all necessary results takes place after we obtain an intersection object
It contains the following elements:
1. t: a scalar, the intersection is t units away from the origin of the ray
2. object: a class inheriting Shape, indicating the shape that has the intersection
3. point: a Tuple, the intersection point
4. eyev: a Tuple, the eye vector
5. normalv: a Tuple, the normal at the point
6. inside: a Bool, indicates whether the intersection is inside or outside the shape
7. reflectv: a Tuple, the reflected vector
8. n1: a float, a refractivity index
9. n2: a float, a refractivity index

Computation class contains the following functions:
__init__
__str__
schlick
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/ComputationTest.py
    --- OR ---- 
    python3 -m nose -v ../test/ComputationTest.py
    --- OR ---- 
    python -m nose -v ../test/ComputationTest.py
    ---------------------------------------------------
"""


class Computation():
    t = 0
    shape = None
    point = Tuple()
    eyev = Tuple()
    normalv = Tuple()
    inside = False

    # ---------------------
    """
    Set up the computation object
    ---- Inputs: --------
        * intersection: an Intersection
        * ray: a Ray
        * xs: an Intersection Array, containing all intersections from the world
    ---- Outputs: --------
        * comp: a Computation
    """
    # ---------------------

    def __init__(self, intersection: "Intersection", ray: "Ray", xs=[]):
        self.t = intersection.t
        self.shape = intersection.shape

        self.point = ray.position(self.t)
        self.eyev = ~ray.direction
        self.normalv = self.shape.normalAt(self.point, hit=intersection)
        if self.normalv.dot(self.eyev) < 0:
            self.inside = True
            self.normalv = ~self.normalv

        self.overPoint = self.point + self.normalv * 0.00001
        self.underPoint = self.point - self.normalv * 0.00001

        # reflectivity
        self.reflectv = ray.direction.reflectV(self.normalv)

        # refractivity
        containers = []
        for i in xs:
            if i == intersection:
                if len(containers) == 0:
                    self.n1 = 1
                else:
                    self.n1 = containers[-1].material.refractiveIndex
            if i.shape in containers:
                containers.remove(i.shape)
            else:
                containers.append(i.shape)
            if i == intersection:
                if len(containers) == 0:
                    self.n2 = 1
                else:
                    self.n2 = containers[-1].material.refractiveIndex
                break
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/ComputationTest.py:test_init
        --- OR ---- 
        python3 -m nose -v ../test/ComputationTest.py:test_init
        --- OR ---- 
        python -m nose -v ../test/ComputationTest.py:test_init
        ---------------------------------------------------
    """

    # ---------------------
    """
    Define the output format for Computation class
    """
    # ---------------------

    def __str__(self):
        return "T: " + str(self.t) + "\n" + "Object: "+str(self.shape)+"\n" + "Point: "+str(self.point) + "\n" + "Eye: "+str(self.eyev) + "\n" + "Normal: "+str(self.normalv) + + "\n" + "Over Point: "+str(self.overPoint) + "\n" + "Under Point: "+str(self.underPoint) + "\n" + "Reflect Vector: "+str(self.reflectv) + "\n" + "n1: "+str(self.n1) + "\n" + "n2: "+str(self.n2)

    # ---------------------
    """
    Schlick implements the Fresnel effect to determine the reflectance
    ---- Outputs: --------
        * num: a float, the reflectance of the ray
    """
    # ---------------------

    def schlick(self):
        cos = self.eyev.dot(self.normalv)
        if self.n1 > self.n2:
            n = self.n1/self.n2
            sin2T = n * n * (1-cos*cos)
            if sin2T > 1:
                return 1
            cosT = (1-sin2T)
            cos = cosT
        r0 = (self.n1-self.n2)/(self.n1 + self.n2)
        r0 = r0 * r0

        return r0 + (1-r0)*((1-cos) ** 5)
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/ComputationTest.py:test_schlick
        --- OR ---- 
        python3 -m nose -v ../test/ComputationTest.py:test_schlick
        --- OR ---- 
        python -m nose -v ../test/ComputationTest.py:test_schlick
        ---------------------------------------------------
    """
