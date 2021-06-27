import abc
import numpy as np
from Tuple import Tuple
from Matrix import Matrix
from Ray import Ray
from Material import Material

# ---------------------
""" 
Shape class is a parent class containing all necessary compnents of a shape. 
Sphere and all other specific classes inherits it.
It contains the following elements:
1. transform: a Matrix, recording the transform matrix
2. material: a Material, recording the material of the shape
3. parent: a Shape, the parent of a shape in a group

Shape class contains the following functions:
__init__
__str__
intersect
localIntersect: an abstract method, would be implemented by other classes
normalAt
localNormalAt: an abstract method, would be implemented by other classes
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/ShapeTest.py
    --- OR ---- 
    python3 -m nose -v ../test/ShapeTest.py
    --- OR ---- 
    python -m nose -v ../test/ShapeTest.py
    ---------------------------------------------------
"""


class Shape():

    # ---------------------
    """
        Shape class takes in no input
    """
    # ---------------------

    def __init__(self):
        self.center = Tuple.point(0, 0, 0)
        self.material = Material()
        self.transform = Matrix(matrix=np.eye(4))
        self.parent = None

    # ---------------------
    """
    Define the output format for Shape class
    """
    # ---------------------

    def __str__(self):
        return "The transform matrix is: \n" + str(self.transform) + "\n" + "The material is as the following: \n" + str(self.material) + "\n"

    # ---------------------
    """
    Find the intersection between the ray and the shape with the world axis
    ---- Inputs: --------
        * ray: a Ray with world axis
    ---- Outputs: --------
        * count: a scalar, the number of intersections
        * results: a tuple, all intersections are listed
    """
    # ---------------------

    def intersect(self, ray: "Ray"):
        localRay = ray.transform(~self.transform)
        return self.localIntersect(localRay)

    # ---------------------
    """  
        Make sure you are on ~/src
        use the test of each different shape's intersect function
    """

    # ---------------------
    """
    Find the intersection with the shape as the main axis and center at the origin
    ---- Inputs: --------
        * ray: a Ray with sphere axis
    ---- Outputs: --------
        * count: a scalar, the number of intersections
        * results: a tuple, all intersections are listed
    """
    # ---------------------
    @abc.abstractmethod
    def localIntersect(self, ray: "Ray"):
        raise NotImplementedError
    # ---------------------
    """  
        Make sure you are on ~/src
        this will be tested by all of the intersect function
    """

    # ---------------------
    """
    Find the normal between the ray and the shape with the world axis
    ---- Inputs: --------
        * ray: a Ray with world axis
    ---- Outputs: --------
        * count: a scalar, the number of intersections
        * results: a tuple, all intersections are listed
    """
    # ---------------------

    def normalAt(self, point: "Tuple", **kwargs):
        localPoint = self.worldToObject(point)
        if "hit" in kwargs:
            localNormal = self.localNormalAt(localPoint, hit=kwargs["hit"])
        else:
            localNormal = self.localNormalAt(localPoint)
        return self.normalToWorld(localNormal)

    # ---------------------
    """  
        Make sure you are on ~/src
        use the test of each different shape's normalAt function
        also, we have a specific test for group normal at the following:
        ---------------------------------------------------
        nosetests -v ../test/ShapeTest.py:test_normalAt
        --- OR ---- 
        python3 -m nose -v ../test/ShapeTest.py:test_normalAt
        --- OR ---- 
        python -m nose -v ../test/ShapeTest.py:test_normalAt
        ---------------------------------------------------
    """

    # ---------------------
    """
    Find the normal with the shape as the main axis and center at the origin
    ---- Inputs: --------
        * ray: a Ray with sphere axis
    ---- Outputs: --------
        * count: a scalar, the number of intersections
        * results: a tuple, all intersections are listed
    """
    # ---------------------
    @abc.abstractmethod
    def localNormalAt(self, point: "Tuple", **kwargs):
        raise NotImplementedError
    # ---------------------
    """  
        Make sure you are on ~/src
        this will be tested with all of normalAt function
    """

    # ---------------------
    """
    World to object converts the normal at the point of the shape to the shape axis
    ---- Inputs: --------
        * point: a Tuple, indicating a point on the Shape 
    ---- Outputs: --------
        * point: a Tuple, the converted point
    """
    # ---------------------

    def worldToObject(self, point: "Tuple"):
        if self.parent != None:
            point = self.parent.worldToObject(point)
        return ~self.transform * point
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/GroupTest.py:test_worldToObject
        --- OR ---- 
        python3 -m nose -v ../test/GroupTest.py:test_worldToObject
        --- OR ---- 
        python -m nose -v ../test/GroupTest.py:test_worldToObject
        ---------------------------------------------------
    """

    # ---------------------
    """
    Normal to World converts the normal at the point of the shape to the world axis
    ---- Inputs: --------
        * nromal: a Tuple, indicating a point on the Shape 
    ---- Outputs: --------
        * normal: a Tuple, the converted normal vector
    """
    # ---------------------

    def normalToWorld(self, normal: "Tuple"):
        normal = (~self.transform).transpose() * normal
        normal.w = 0
        normal.arr[3] = 0
        normal = normal.normalize()
        if self.parent != None:
            normal = self.parent.normalToWorld(normal)
        return normal
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/GroupTest.py:test_normalToWorld
        --- OR ---- 
        python3 -m nose -v ../test/GroupTest.py:test_normalToWorld
        --- OR ---- 
        python -m nose -v ../test/GroupTest.py:test_normalToWorld
        ---------------------------------------------------
    """
