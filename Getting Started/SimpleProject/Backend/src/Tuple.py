import numpy as np
# ---------------------
""" 
Tuple class describes the tuple we use to build a 3D renderer
This class is a base class for points and vectors
Each tuple contain 4 elements: x,y,z,w in a numpy array
x,y,z,w are all float value
x: x-coordinate, y: y-coordinate, z: z-coordinate
w = 0 indicate a vector, w = 1 indicate a point

Tuple class contains the following functions:
__init__
__str__
__eq__
__add__
__sub__
__mul__
__truediv__
__invert__
point
vector
magnitude
dot
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/TupleTest.py
    --- OR ---- 
    python3 -m nose -v ../test/TupleTest.py
    --- OR ---- 
    python -m nose -v ../test/TupleTest.py
    ---------------------------------------------------
"""


class Tuple():
    # ---------------------
    """
    Tuple class takes in a numpy array
    arr[0] is x, arr[1] is y, arr[2] is z, arr[3] is w
    """
    # ---------------------

    def __init__(self, arr):
        self.arr = arr

    # ---------------------
    """
    Define the output format for Tuple class
    """
    # ---------------------

    def __str__(self):
        return "({0},{1},{2},{3})".format(self.arr[0], self.arr[1], self.arr[2], self.arr[3])

    # ---------------------
    """
    Define equivalence of two Tuple instances
    This is based on numpy allclose function with absolute tolerance 0.00001
    """
    # ---------------------

    def __eq__(self, tuple2):
        return np.allclose(self.arr, tuple2.arr, atol=0.00001)

    # ---------------------
    """
    Define the sum between two Tuples
    Works for both points and vector
    ---- Inputs: --------
        * tuple2: A Tuple
    ---- Outputs: --------
        * Tuple: the sum of two tuples
    
    """
    # ---------------------

    def __add__(self, tuple2):
        return Tuple(self.arr + tuple2.arr)
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TupleTest.py:test_add
        --- OR ---- 
        python3 -m nose -v ../test/TupleTest.py:test_add
        --- OR ---- 
        python -m nose -v ../test/TupleTest.py:test_add
        ---------------------------------------------------
    """

    # ---------------------
    """
    Define the difference between two Tuples
    Works for both points and vector
    ---- Inputs: --------
        * tuple2: A Tuple
    ---- Outputs: --------
        * Tuple: the difference of two tuples
    """
    # ---------------------

    def __sub__(self, tuple2):
        return Tuple(self.arr - tuple2.arr)
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TupleTest.py:test_subtract
        --- OR ---- 
        python3 -m nose -v ../test/TupleTest.py:test_subtract
        --- OR ---- 
        python -m nose -v ../test/TupleTest.py:test_subtract
        ---------------------------------------------------
    """

    # ---------------------
    """
    Define the product of a Tuple and a scalar
    This is used for finding the point lies scalar times further in the direction of the given vector
    The order is not interchangeable, must be tuple * scalar
    Works vector only
    ---- Inputs: --------
        * scalar: A scalar
    ---- Outputs: --------
        * Tuple: the product of a Tuple and a scalar
    """
    # ---------------------

    def __mul__(self, scalar):
        return Tuple(self.arr * scalar)
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TupleTest.py:test_multiScalar
        --- OR ---- 
        python3 -m nose -v ../test/TupleTest.py:test_multiScalar
        --- OR ---- 
        python -m nose -v ../test/TupleTest.py:test_multiScalar
        ---------------------------------------------------
    """

    # ---------------------
    """
    Define the division of a Tuple and a scalar
    The order is not interchangeable, must be tuple / scalar
    Works for vector only
    ---- Inputs: --------
        * scalar: A scalar
    ---- Outputs: --------
        * Tuple: the product of a Tuple and a scalar
    """
    # ---------------------

    def __truediv__(self, scalar):
        return Tuple(self.arr / scalar)
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TupleTest.py:test_divScalar
        --- OR ---- 
        python3 -m nose -v ../test/TupleTest.py:test_divScalar
        --- OR ---- 
        python -m nose -v ../test/TupleTest.py:test_divScalar
        ---------------------------------------------------
    """
    # ---------------------
    """
    Negate multiply each element in the array by -1
    Works for both point and vector
    ---- Outputs: --------
        * Tuple: the negated tuple
    """
    # ---------------------

    def __invert__(self):
        return Tuple(-self.arr)
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TupleTest.py:test_negate
        --- OR ---- 
        python3 -m nose -v ../test/TupleTest.py:test_negate
        --- OR ---- 
        python -m nose -v ../test/TupleTest.py:test_negate
        ---------------------------------------------------
    """


    # ---------------------
    """
    Point is a Tuple having w=1
    point is a static method
    ---- Inputs: --------
        * x: x-coordinate
        * y: y-coordinate
        * z: z-coordinate
    ---- Outputs: --------
        * Tuple: a Point
    """
    # ---------------------
    @staticmethod
    def point(x, y, z):
        return Tuple(np.array([x, y, z, 1]))
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TupleTest.py:test_point
        --- OR ---- 
        python3 -m nose -v ../test/TupleTest.py:test_point
        --- OR ---- 
        python -m nose -v ../test/TupleTest.py:test_point
        ---------------------------------------------------
    """

    # ---------------------
    """
    Vector is a Tuple having w=0
    vector is a static method
    ---- Inputs: --------
        * x: x-coordinate
        * y: y-coordinate
        * z: z-coordinate
    ---- Outputs: --------
        * Tuple: a Point
    """
    # ---------------------
    @staticmethod
    def vector(x, y, z):
        return Tuple(np.array([x, y, z, 0]))
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TupleTest.py:test_vector
        --- OR ---- 
        python3 -m nose -v ../test/TupleTest.py:test_vector
        --- OR ---- 
        python -m nose -v ../test/TupleTest.py:test_vector
        ---------------------------------------------------
    """


    # ---------------------
    """
    Magnituude is used for discovering the distance represented by a vector
    Magnitude is calculated based on Pythagoras' theorem
    Works for vector only
    ---- Outputs: --------
        * magnitude: a scalar
    """
    # ---------------------
    def magnitude(self):
        return np.sqrt(sum(self.arr**2))
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TupleTest.py:test_magnitude
        --- OR ---- 
        python3 -m nose -v ../test/TupleTest.py:test_magnitude
        --- OR ---- 
        python -m nose -v ../test/TupleTest.py:test_magnitude
        ---------------------------------------------------
    """

    # ---------------------
    """
    Normalize is used to converting a vector to a unit vector to make sure the rays are calculated standardly
    Works for vector only
    ---- Outputs: --------
        * normalizedVector: a Tuple
    """
    # ---------------------

    def normalize(self):
        return self/self.magnitude()
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TupleTest.py:test_magnitude
        --- OR ---- 
        python3 -m nose -v ../test/TupleTest.py:test_magnitude
        --- OR ---- 
        python -m nose -v ../test/TupleTest.py:test_magnitude
        ---------------------------------------------------
    """


    # ---------------------
    """
    Dot product is a standard way to understand the angle between two vectors, the smaller the result, the larger the angle
    It is widely used to find intersactions of rays and objects.
    Works for vector only
    ---- Outputs: --------
        * dotProduct: a scalar
    """
    # ---------------------

    def dot(self, tuple2):
        return self.arr@tuple2.arr
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TupleTest.py:test_dot
        --- OR ---- 
        python3 -m nose -v ../test/TupleTest.py:test_dot
        --- OR ---- 
        python -m nose -v ../test/TupleTest.py:test_dot
        ---------------------------------------------------
    """

    # ---------------------
    """
    Cross product is a standard way to find a third vector perpendicular to the existing two vectors.
    However, given the vector has directions, and can be pointing the opposite direction
    If we have the cross product order changed then we would have the result vector pointing to the opposite direction
    Works for vector only
    ---- Outputs: --------
        * crossProduct: a Tuple perpendicular to the given two vectors
    """
    # ---------------------

    def cross(self, tuple2):
        crossP = np.cross(self.arr[:-1], tuple2.arr[:-1])
        return Tuple.vector(crossP[0],crossP[1],crossP[2])
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/TupleTest.py:test_cross
        --- OR ---- 
        python3 -m nose -v ../test/TupleTest.py:test_cross
        --- OR ---- 
        python -m nose -v ../test/TupleTest.py:test_cross
        ---------------------------------------------------
    """
