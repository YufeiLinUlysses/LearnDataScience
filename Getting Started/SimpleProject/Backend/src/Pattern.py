import numpy as np
from Color import Color
from Matrix import Matrix
from Tuple import Tuple
from Intersection import Intersection
# ---------------------
"""
Pattern class helps to establish the patterns that would show up on the shape
It contains a transform matrix and two colors to match up the colors, but could be expanded later.
1. transform: a Matrix, a transform matrix.
2. c1: a Color, one color in the pattern
3. c2: a Color, one color in the pattern
4. patternType: a String, indicates the type of pattern used in the material

Currently we only support 4 types of patterns:
stripe, gradient, ring and checker, we will support more in the future

Pattern class contains the following functions:
__init__
__eq__
__str__
patternAtObject
stripe
gradient
ring
checker
"""
# ---------------------
"""
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/PatternTest.py
    --- OR ----
    python3 -m nose -v ../test/PatternTest.py
    --- OR ----
    python -m nose -v ../test/PatternTest.py
    ---------------------------------------------------
"""


class Pattern():
    # ---------------------
    """
        Pattern class takes in two colors and a transform matrix and a string indicating the pattern type
    """
    # ---------------------

    def __init__(self, c1: "Color", c2: "Color", transform: "Matrix" = None, patternType: str = "stripe"):
        self.c1 = c1
        self.c2 = c2
        if transform != None:
            self.transform = transform
        else:
            self.transform = Matrix(matrix=np.eye(4))
        self.patternType = patternType

    # ---------------------
    """
    Define equivalence of two Sphere instances
    """
    # ---------------------

    def __eq__(self, pattern2: "Pattern"):
        return pattern2.c1 == self.c1 and pattern2.c2 == self.c2 and pattern2.transform == self.transform

    # ---------------------
    """
    Define the string of pattern
    """
    # ---------------------

    def __str__(self):
        return "Color1: " + str(self.c1) + "\nColor2: " + str(self.c2) + "\nTransfrom Matrix: \n" + str(self.transform) + "\nPattern Type: " + self.patternType

    # ---------------------
    """
    Stripe pattern looks like ababab across the main axis
    ---- Inputs: --------
        * point: a Point
        * objTransform: a Matrix, the transform matrix of the object
    ---- Outputs: --------
        * color: a Color, the color at the point
    """
    # ---------------------

    def patternAtObject(self, point: "Tuple", objTransform: "Matrix"):
        objPoint = ~objTransform * point
        patternPoint = ~self.transform*objPoint
        if self.patternType == "stripe":
            return self.stripe(patternPoint)
        elif self.patternType == "gradient":
            return self.gradient(patternPoint)
        elif self.patternType == "ring":
            return self.ring(patternPoint)
        elif self.patternType == "checker":
            return self.checker(patternPoint)
        else:
            return Color(patternPoint.x, patternPoint.y, patternPoint.z)
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/PatternTest.py:test_patternAtObject
        --- OR ----
        python3 -m nose -v ../test/PatternTest.py:test_patternAtObject
        --- OR ----
        python -m nose -v ../test/PatternTest.py:test_patternAtObject
        ---------------------------------------------------
    """

    # ---------------------
    """
    Stripe pattern looks like ababab across the main axis
    ---- Inputs: --------
        * point: a Point
    ---- Outputs: --------
        * color: a Color, the color at the point
    """
    # ---------------------

    def stripe(self, point: "Tuple"):
        return self.c1 if np.floor(point.x) % 2 == 0 else self.c2
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/PatternTest.py:test_stripe
        --- OR ----
        python3 -m nose -v ../test/PatternTest.py:test_stripe
        --- OR ----
        python -m nose -v ../test/PatternTest.py:test_stripe
        ---------------------------------------------------
    """

    # ---------------------
    """
    Gradient pattern looks like a->b incrementally across the main axis
    ---- Inputs: --------
        * point: a Point
    ---- Outputs: --------
        * color: a Color, the color at the point
    """
    # ---------------------

    def gradient(self, point: "Tuple"):
        distance = self.c2-self.c1
        fraction = float(point.x - np.floor(point.x))
        return self.c1 + distance * fraction
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/PatternTest.py:test_gradient
        --- OR ----
        python3 -m nose -v ../test/PatternTest.py:test_gradient
        --- OR ----
        python -m nose -v ../test/PatternTest.py:test_gradient
        ---------------------------------------------------
    """

    # ---------------------
    """
    Ring pattern looks like ababab along x-axis and z-axis and in a circle
    ---- Inputs: --------
        * point: a Point
    ---- Outputs: --------
        * color: a Color, the color at the point
    """
    # ---------------------

    def ring(self, point: "Tuple"):
        if np.floor((point.x**2 + point.z**2)) % 2 == 0:
            return self.c1
        return self.c2
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/PatternTest.py:test_ring
        --- OR ----
        python3 -m nose -v ../test/PatternTest.py:test_ring
        --- OR ----
        python -m nose -v ../test/PatternTest.py:test_ring
        ---------------------------------------------------
    """

    # ---------------------
    """
    3D Checker pattern looks like ababab along x-axis and y-axis and in a square but does not influence z-axis
    ---- Inputs: --------
        * point: a Point
    ---- Outputs: --------
        * color: a Color, the color at the point
    """
    # ---------------------

    def checker(self, point: "Tuple"):
        if (np.floor(np.array([point.x, point.y, point.z])).sum()) % 2 == 0:
            return self.c1
        return self.c2
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/PatternTest.py:test_checker
        --- OR ----
        python3 -m nose -v ../test/PatternTest.py:test_checker
        --- OR ----
        python -m nose -v ../test/PatternTest.py:test_checker
        ---------------------------------------------------
    """
