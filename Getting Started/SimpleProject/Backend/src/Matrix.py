import math
import numpy as np
from Tuple import Tuple
# ---------------------
""" 
Matrix class helps to describe a set of elements.
Each matrix contains 3 elements: weight ,height, matrix
width, height are all float value
width: defining the number of columns, height: defining the number of rows
matrix: defining a numpy matrix containing necessary numbers

Note: matrix class contains several transformation matrices. 
In order to chain them, we need to have the last operation matrix multiply the previous matrix

Matrix class contains the following functions:
__init__
__str__
__eq__
__mul__
__invert__
identity
determinant
translation
scaling
rotateX
rotateY
rotateZ
shearing
viewTransform
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/MatrixTest.py
    --- OR ---- 
    python3 -m nose -v ../test/MatrixTest.py
    --- OR ---- 
    python -m nose -v ../test/MatrixTest.py
    ---------------------------------------------------
"""


class Matrix():
    # ---------------------
    """
    Matrix class takes in two numbers
    w is width, h is height, matrix is a matrix
    """
    # ---------------------

    def __init__(self, w: int = None, h: int = None, matrix: np.ndarray = None):
        if w == h == None:
            try:
                if matrix.size != 0:
                    self.matrix = matrix
                    self.width = matrix.shape[1]
                    self.height = matrix.shape[0]
            except:
                self.width = 0
                self.height = 0
                self.matrix = np.zeros((1, 1))
        else:
            self.width = w
            self.height = h
            self.matrix = np.zeros((h, w))

    # ---------------------
    """
    Define the output format for Matrix class
    """
    # ---------------------

    def __str__(self):
        return str(self.matrix)

    # ---------------------
    """
    Define equivalence of two Matrix instances
    This is based on numpy allclose function with absolute tolerance 0.00001
    """
    # ---------------------

    def __eq__(self, matrix2: "Matrix"):
        return np.allclose(self.matrix, matrix2.matrix, atol=0.0001)

    # ---------------------
    """
    Define the multiplication between two Matrix (Cross product)
    This helps to perform transformations
    Define the multiplication between matrix and vector
    Define the multiplication between matrix and scalar
    Order matters, it is not interchangable
    ---- Inputs: --------
        * value: A Matrix or a Tuple or a float
    ---- Outputs: --------
        * Matrix: the result from matrix multiplication or a tuple from matrix and tuple multiplication or a matrix from matrix and scalar multiplication
    """
    # ---------------------

    def __mul__(self, value):
        if type(value) == float:
            return Matrix(matrix=self.matrix*value)
        elif type(value).__name__ == "Tuple":
            return Tuple(arr=np.matmul(self.matrix, value.arr))
        return Matrix(matrix=np.matmul(self.matrix, value.matrix))
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/MatrixTest.py:test_mul
        --- OR ---- 
        python3 -m nose -v ../test/MatrixTest.py:test_mul
        --- OR ---- 
        python -m nose -v ../test/MatrixTest.py:test_mul
        ---------------------------------------------------
    """

    # ---------------------
    """
    This calculates the inversion of a matrix
    ---- Outputs: --------
        * Matrix: the inverse of the matrix
    """
    # ---------------------

    def __invert__(self):
        return Matrix(matrix=np.linalg.inv(self.matrix))
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/MatrixTest.py:test_inversion
        --- OR ---- 
        python3 -m nose -v ../test/MatrixTest.py:test_inversion
        --- OR ---- 
        python -m nose -v ../test/MatrixTest.py:test_inversion
        ---------------------------------------------------
    """

    # ---------------------
    """
    Define the identity based on the matrix's shape
    ---- Outputs: --------
        * Matrix: the identity matrix
    """
    # ---------------------

    def identity(self):
        return Matrix(matrix=np.eye(self.height))
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/MatrixTest.py:test_identity
        --- OR ---- 
        python3 -m nose -v ../test/MatrixTest.py:test_identity
        --- OR ---- 
        python -m nose -v ../test/MatrixTest.py:test_identity
        ---------------------------------------------------
    """

    # ---------------------
    """
    Obtain the transposed matrix of the original one
    Transpose means flipping the matrix over the left diagonal
    ---- Outputs: --------
        * Matrix: the transposed matrix
    """
    # ---------------------

    def transpose(self):
        return Matrix(matrix=self.matrix.T)
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/MatrixTest.py:test_transpose
        --- OR ---- 
        python3 -m nose -v ../test/MatrixTest.py:test_transpose
        --- OR ---- 
        python -m nose -v ../test/MatrixTest.py:test_transpose
        ---------------------------------------------------
    """

    # ---------------------
    """
    Obtain the determinant of the matrix
    It is used to determine whether this matrix has an inversion
    ---- Outputs: --------
        * result: a scalar, the determinant
    """
    # ---------------------

    def determinant(self):
        return np.linalg.det(self.matrix)
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/MatrixTest.py:test_deter
        --- OR ---- 
        python3 -m nose -v ../test/MatrixTest.py:test_deter
        --- OR ---- 
        python -m nose -v ../test/MatrixTest.py:test_deter
        ---------------------------------------------------
    """

    # ---------------------
    """
    Translation matrix helps to transform a point to a desired location
    However, it does not work for vectors
    Inverse of the translation matrix means working on the opposite direction
    translation is a static method
    ---- Inputs: --------
        * x: the amount wants to transform on x-axis
        * y: the amount wants to transform on y-axis
        * z: the amount wants to transform on z-axis
    ---- Outputs: --------
        * Matrix: the translation matrix
    """
    # ---------------------
    @staticmethod
    def translation(x: float, y: float, z: float):
        m = np.eye(4)
        m[0, 3] = x
        m[1, 3] = y
        m[2, 3] = z
        return Matrix(matrix=m)
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/MatrixTest.py:test_translation
        --- OR ---- 
        python3 -m nose -v ../test/MatrixTest.py:test_translation
        --- OR ---- 
        python -m nose -v ../test/MatrixTest.py:test_translation
        ---------------------------------------------------
    """

    # ---------------------
    """
    Scale matrix helps to transform the size of an object
    Inverse of the scaling matrix means scaling by the inverse of the input
    scaling is a static method
    ---- Inputs: --------
        * x: the amount wants to be scaled on x-axis
        * y: the amount wants to be scaled on y-axis
        * z: the amount wants to be scaled on z-axis
    ---- Outputs: --------
        * Matrix: the scaling matrix
    """
    # ---------------------
    @staticmethod
    def scaling(x: float, y: float, z: float):
        m = np.eye(4)
        m[0, 0] = x
        m[1, 1] = y
        m[2, 2] = z
        return Matrix(matrix=m)
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/MatrixTest.py:test_scaling
        --- OR ---- 
        python3 -m nose -v ../test/MatrixTest.py:test_scaling
        --- OR ---- 
        python -m nose -v ../test/MatrixTest.py:test_scaling
        ---------------------------------------------------
    """

    # ---------------------
    """
    RotateX matrix helps to rotate the object according to x-axis
    Inverse of the matrix means rotating at an opposite direction
    rotateX is a static method
    ---- Inputs: --------
        * angle: the rotate angle in radian
    ---- Outputs: --------
        * Matrix: the rotation matrix
    """
    # ---------------------
    @staticmethod
    def rotateX(theta: float):
        m = np.eye(4)
        m[1, 1] = math.cos(theta)
        m[1, 2] = -math.sin(theta)
        m[2, 1] = math.sin(theta)
        m[2, 2] = math.cos(theta)
        return Matrix(matrix=m)
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/MatrixTest.py:test_rotateX
        --- OR ---- 
        python3 -m nose -v ../test/MatrixTest.py:test_rotateX
        --- OR ---- 
        python -m nose -v ../test/MatrixTest.py:test_rotateX
        ---------------------------------------------------
    """

    # ---------------------
    """
    RotateY matrix helps to rotate the object according to y-axis
    Inverse of the matrix means rotating at an opposite direction
    rotateY is a static method
    ---- Inputs: --------
        * angle: the rotate angle in radian
    ---- Outputs: --------
        * Matrix: the rotation matrix
    """
    # ---------------------
    @staticmethod
    def rotateY(theta: float):
        m = np.eye(4)
        m[0, 0] = math.cos(theta)
        m[0, 2] = math.sin(theta)
        m[2, 0] = -math.sin(theta)
        m[2, 2] = math.cos(theta)
        return Matrix(matrix=m)
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/MatrixTest.py:test_rotateY
        --- OR ---- 
        python3 -m nose -v ../test/MatrixTest.py:test_rotateY
        --- OR ---- 
        python -m nose -v ../test/MatrixTest.py:test_rotateY
        ---------------------------------------------------
    """

    # ---------------------
    """
    RotateZ matrix helps to rotate the object according to z-axis
    Inverse of the matrix means rotating at an opposite direction
    rotateZ is a static method
    ---- Inputs: --------
        * angle: the rotate angle in radian
    ---- Outputs: --------
        * Matrix: the rotation matrix
    """
    # ---------------------
    @staticmethod
    def rotateZ(theta: float):
        m = np.eye(4)
        m[0, 0] = math.cos(theta)
        m[0, 1] = -math.sin(theta)
        m[1, 0] = math.sin(theta)
        m[1, 1] = math.cos(theta)
        return Matrix(matrix=m)
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/MatrixTest.py:test_rotateY
        --- OR ---- 
        python3 -m nose -v ../test/MatrixTest.py:test_rotateY
        --- OR ---- 
        python -m nose -v ../test/MatrixTest.py:test_rotateY
        ---------------------------------------------------
    """

    # ---------------------
    """
    Shearing matrix helps to slant a straight line. 
    X-coordinates would change in proportion to Y-axis and Z-axis, 
    Y-coordinates changes in proportion to X-axis and Z-axis,
    Z-coordinates changes in proportion to X-axis and Y-axis.
    Inverse of the matrix means shifting the line on an opposite direction
    shearing is a static method
    ---- Inputs: --------
        * xy: a float, the change of X-coordinates in proportion to Y-axis
        * xz: a float, the change of X-coordinates in proportion to Z-axis
        * yx: a float, the change of Y-coordinates in proportion to X-axis
        * yz: a float, the change of Y-coordinates in proportion to Z-axis
        * zx: a float, the change of Z-coordinates in proportion to X-axis
        * zy: a float, the change of Z-coordinates in proportion to Y-axis
    ---- Outputs: --------
        * Matrix: the rotation matrix
    """
    # ---------------------
    @staticmethod
    def shearing(xy: float, xz: float, yx: float, yz: float, zx: float, zy: float):
        m = np.eye(4)
        m[0, 1] = xy
        m[0, 2] = xz
        m[1, 0] = yx
        m[1, 2] = yz
        m[2, 0] = zx
        m[2, 1] = zy
        return Matrix(matrix=m)
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/MatrixTest.py:test_shearing
        --- OR ---- 
        python3 -m nose -v ../test/MatrixTest.py:test_shearing
        --- OR ---- 
        python -m nose -v ../test/MatrixTest.py:test_shearing
        ---------------------------------------------------
    """

    # ---------------------
    """
    View transformation matrix helps to transform the camera
    Inverse of the view transform matrix means undo the transformation on the camera
    viewTransformation is a static method
    ---- Inputs: --------
        * fromV: a Point, indicating where the eye is in the scene
        * toV: a Point, indicating the direction the eye is looking at the scene
        * upV: a Vector, indicating which direction is up in the scene
    ---- Outputs: --------
        * Matrix: the view transformation matrix
    """
    # ---------------------
    @staticmethod
    def viewTransformation(fromV: "Tuple", toV: "Tuple", upV: "Tuple"):
        forward = (toV-fromV).normalize()
        upn = upV.normalize()
        left = forward.cross(upn)
        trueUp = left.cross(forward)
        orientation = Matrix(matrix=np.array([
            [left.x, left.y, left.z, 0],
            [trueUp.x, trueUp.y, trueUp.z, 0],
            [-forward.x, -forward.y, -forward.z, 0],
            [0, 0, 0, 1]
        ]))
        return orientation*Matrix.translation(-fromV.x, -fromV.y, -fromV.z)
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/MatrixTest.py:test_viewTransformation
        --- OR ---- 
        python3 -m nose -v ../test/MatrixTest.py:test_viewTransformation
        --- OR ---- 
        python -m nose -v ../test/MatrixTest.py:test_viewTransformation
        ---------------------------------------------------
    """
