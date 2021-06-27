from Sphere import Sphere
from Color import Color
from Matrix import Matrix
from Light import Light
from Tuple import Tuple
from Ray import Ray
from Computation import Computation
from Material import Material
from Intersection import Intersection
# ---------------------
""" 
World class contains all the lights and shapes in a scene. 
It contains the following 2 elements:
1. lights: an array of Lights
2. shapes: an array of Shapes

World class contains the following functions:
__init__
defaultWorld
intersectWorld
shadeHit
reflectedColor
colorAt
isShadowed
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/WorldTest.py
    --- OR ---- 
    python3 -m nose -v ../test/WorldTest.py
    --- OR ---- 
    python -m nose -v ../test/WorldTest.py
    ---------------------------------------------------
"""


class World():
    # ---------------------
    """
        World class takes in 2 input
        lights is an array of Lights
        shapes is an array of Shapes
    """
    # ---------------------

    def __init__(self, lights=[], shapes=[]):
        self.lights = lights
        self.shapes = shapes

    # ---------------------
    """
        defaultWorld renders a default world 
        containing two sphere, one is larger than the other, with the same center
        the light is also default
        Note: if you want to change material, remember to initialize a new instance, don't change in place
    """
    # ---------------------
    @staticmethod
    def defaultWorld():
        light = Light(Tuple.point(-10, 10, -10), Color(1, 1, 1))

        s1 = Sphere()
        s1.material = Material(color=Color(0.8, 1.0, 0.6),
                               diffuse=0.7, specular=0.2)

        s2 = Sphere()
        s2.material = Material(color=Color(1, 1, 1))
        s2.transform = Matrix.scaling(0.5, 0.5, 0.5)
        return World([light], [s1, s2])
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/WorldTest.py:test_defaultWorld
        --- OR ---- 
        python3 -m nose -v ../test/WorldTest.py:test_defaultWorld
        --- OR ---- 
        python -m nose -v ../test/WorldTest.py:test_defaultWorld
        ---------------------------------------------------
    """

    # ---------------------
    """
    Intersect world sets up the intersection of all objects in the world and the given ray
    Then, sort the intersections by their t value
    ---- Inputs: --------
        * ray: a Ray
    ---- Outputs: --------
        * count: a scalar, the number of intersections
        * results: a tuple, all intersections are listed
    """
    # ---------------------

    def intersectWorld(self, ray: "Ray"):
        total = 0
        result = []
        for s in self.shapes:
            count, intersects = s.intersect(ray)
            if count != 0:
                total += count
                result += intersects
        result.sort(key=lambda x: x.t)
        return total, result
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/WorldTest.py:test_intersectWorld
        --- OR ---- 
        python3 -m nose -v ../test/WorldTest.py:test_intersectWorld
        --- OR ---- 
        python -m nose -v ../test/WorldTest.py:test_intersectWorld
        ---------------------------------------------------
    """

    # ---------------------
    """
    shadeHit helps to calculate the shading on each different object
    ---- Inputs: --------
        * computation: a Computation
        * remaining: an Integer, indicating the number of recursion left
    ---- Outputs: --------
        * color: a Color, the final representation on the object
    """
    # ---------------------

    def shadeHit(self, computation: "Computation", remaining=1):
        col = Color(0, 0, 0)
        for l in self.lights:
            inShadow = self.isShadowed(l, computation.overPoint)
            col += computation.shape.material.lighting(
                l, computation.overPoint, computation.eyev, computation.normalv, inShadow, computation.shape.transform)

        reflected = self.reflectedColor(computation, remaining)
        refracted = self.refractedColor(computation, remaining)

        mat = computation.shape.material
        if mat.reflective > 0 and mat.transparency > 0:
            reflectance = computation.schlick()
            return col + reflected * reflectance + refracted * (1-reflectance)
        return col + reflected + refracted
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/WorldTest.py:test_shadeHit
        --- OR ---- 
        python3 -m nose -v ../test/WorldTest.py:test_shadeHit
        --- OR ---- 
        python -m nose -v ../test/WorldTest.py:test_shadeHit
        ---------------------------------------------------
    """

    # ---------------------
    """
    colorAt helps to calculate the final color on the object
    ---- Inputs: --------
        * ray: a Ray
        * remaining: an Integer, indicates the number of recursion left
    ---- Outputs: --------
        * color: a Color, the final color on the object
    """
    # ---------------------

    def colorAt(self, ray: "Ray", remaining=1):
        count, xs = self.intersectWorld(ray)
        h = Intersection.hit(xs)
        if count == 0:
            return Color(0, 0, 0)
        comp = Computation(h, ray, xs)
        return self.shadeHit(comp, remaining)
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/WorldTest.py:test_colorAt
        --- OR ---- 
        python3 -m nose -v ../test/WorldTest.py:test_colorAt
        --- OR ---- 
        python -m nose -v ../test/WorldTest.py:test_colorAt
        ---------------------------------------------------
    """

    # ---------------------
    """
    isShadowed helps to determine whehter the shape is in shadow
    ---- Inputs: --------
        * l: a Light, indicating the light we want to use to calculate shadow
        * point: a Point, a point on the shape
    ---- Outputs: --------
        * inShadow: a Bool, indicating whether the shape is in shadow
    """
    # ---------------------

    def isShadowed(self, l: "Light", point: "Tuple"):
        v = l.position - point
        distance = v.magnitude()
        direction = v.normalize()
        r = Ray(point, direction)
        count, inters = self.intersectWorld(r)
        h = Intersection.hit(inters)
        return h != Intersection() and h.t < distance

    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/WorldTest.py:test_isShadowed
        --- OR ---- 
        python3 -m nose -v ../test/WorldTest.py:test_isShadowed
        --- OR ---- 
        python -m nose -v ../test/WorldTest.py:test_isShadowed
        ---------------------------------------------------
    """

    # ---------------------
    """
    reflectedColor helps to determine the relfected color based on intersection
    ---- Inputs: --------
        * comp: a Computation, contain all information of intersection
        * remaining: an Integer, indicate the number of recursion left
    ---- Outputs: --------
        * col: a Color, the reflected Color
    """
    # ---------------------

    def reflectedColor(self, comp: "Computation", remaining=1):
        if remaining <= 0:
            return Color()
        r = comp.shape.material.reflective
        if r == 0:
            return Color()
        reflectRay = Ray(comp.overPoint, comp.reflectv)
        color = self.colorAt(reflectRay)
        return color * r

    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/WorldTest.py:test_refelctedColor
        --- OR ---- 
        python3 -m nose -v ../test/WorldTest.py:test_refelctedColor
        --- OR ---- 
        python -m nose -v ../test/WorldTest.py:test_refelctedColor
        ---------------------------------------------------
    """

    # ---------------------
    """
    refractedColor helps to determine the refracted color based on intersection
    ---- Inputs: --------
        * comp: a Computation, contain all information of intersection
        * remaining: an Integer, indicate the number of recursion left
    ---- Outputs: --------
        * col: a Color, the reflected Color
    """
    # ---------------------

    def refractedColor(self, comp: "Computation", remaining=1):
        if comp.shape.material.transparency == 0 or remaining == 0:
            return Color()
        nRatio = comp.n1/comp.n2
        cosI = comp.eyev.dot(comp.normalv)
        sin2T = nRatio * nRatio * (1-cosI*cosI)
        if sin2T > 1:
            return Color()
        cosT = (1-sin2T) ** 0.5
        direction = comp.normalv * (nRatio * cosI - cosT) - comp.eyev * nRatio
        refractRay = Ray(comp.underPoint, direction)
        return self.colorAt(refractRay, remaining - 1) * comp.shape.material.transparency

    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/WorldTest.py:test_refractedColor
        --- OR ---- 
        python3 -m nose -v ../test/WorldTest.py:test_refractedColor
        --- OR ---- 
        python -m nose -v ../test/WorldTest.py:test_refractedColor
        ---------------------------------------------------
    """
