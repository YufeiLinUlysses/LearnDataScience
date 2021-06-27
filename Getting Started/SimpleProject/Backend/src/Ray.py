from Tuple import Tuple
from Matrix import Matrix
# ---------------------
""" 
Ray class helps to describe the ray in the picture
Each ray contains 2 elements: origin and direction
origin, direction are both Tuple value
origin: the start point of the ray, direction: the moving direction of the ray

Ray class contains the following functions:
__init__
__str__
__eq__
position
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/RayTest.py
    --- OR ---- 
    python3 -m nose -v ../test/RayTest.py
    --- OR ---- 
    python -m nose -v ../test/RayTest.py
    ---------------------------------------------------
"""


class Ray():
    # ---------------------
    """
    Ray class takes in two Tuples
    origin is the origin of the ray, a point
    direction is the direction of the ray, a vector
    """
    # ---------------------

    def __init__(self, origin: "Tuple" = Tuple(), direction: "Tuple" = Tuple()):
        self.origin = origin
        self.direction = direction

    # ---------------------
    """
    Define the output format for Ray class
    """
    # ---------------------

    def __str__(self):
        return "origin: " + str(self.origin) + " direction: " + str(self.direction)

    # ---------------------
    """
    Define equivalence of two Ray instances
    """
    # ---------------------

    def __eq__(self, ray2: "Ray"):
        return self.direction == ray2.direction and self.origin == ray2.origin

    # ---------------------
    """
    Define the final point based on the given direction and origin of the ray
    ---- Inputs: --------
        * lambda: a float 
    ---- Outputs: --------
        * Tuple: the point on the line that is t units away from origin
    """
    # ---------------------

    def position(self, t: float):
        return self.origin + self.direction * t
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/RayTest.py:test_position
        --- OR ---- 
        python3 -m nose -v ../test/RayTest.py:test_position
        --- OR ---- 
        python -m nose -v ../test/RayTest.py:test_position
        ---------------------------------------------------
    """

    # ---------------------
    """
    Helps to find the new ray after a transformation
    ---- Inputs: --------
        * matrix: a transformation matrix 
    ---- Outputs: --------
        * Ray: the new transformed ray
    """
    # ---------------------

    def transform(self, matrix: "Matrix"):
        return Ray(origin=matrix*self.origin, direction=matrix*self.direction)
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/RayTest.py:test_transform
        --- OR ---- 
        python3 -m nose -v ../test/RayTest.py:test_transform
        --- OR ---- 
        python -m nose -v ../test/RayTest.py:test_transform
        ---------------------------------------------------
    """
