import numpy as np
# ---------------------
""" 
Color class describes colors based on r,g,b from 0 to 1, if there are exceptions it will be handled in the canvas class while output the image
Each color contains 3 elements: r,g,b in a numpy array
r,g,b are all float value
r: red, g: green, b: blue

Color class contains the following functions:
__init__
__str__
__eq__
__add__
__sub__
__mul__
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/ColorTest.py
    --- OR ---- 
    python3 -m nose -v ../test/ColorTest.py
    --- OR ---- 
    python -m nose -v ../test/ColorTest.py
    ---------------------------------------------------
"""


class Color():
    # ---------------------
    """
    Color class takes in a group of three numbers or a numpy array
    arr[0] is r, arr[1] is g, arr[2] is b
    """
    # ---------------------

    def __init__(self, r: float = None, g: float = None, b: float = None, arr: np.array = None):
        if r == g == b == None:
            try:
                if arr.size != 0:
                    self.arr = arr
                    self.r = arr[0]
                    self.g = arr[1]
                    self.b = arr[2]
            except:
                self.r = 0
                self.g = 0
                self.b = 0
                self.arr = np.array([0, 0, 0])
        else:
            self.r = r
            self.g = g
            self.b = b
            self.arr = np.array([r, g, b])

    # ---------------------
    """
    Define the output format for Color class
    """
    # ---------------------

    def __str__(self):
        return "({0},{1},{2})".format(self.r, self.g, self.b)

    # ---------------------
    """
    Define equivalence of two Color instances
    This is based on numpy allclose function with absolute tolerance 0.00001
    """
    # ---------------------

    def __eq__(self, color2: "Color"):
        return np.allclose(self.arr, color2.arr, atol=0.0001)

    # ---------------------
    """
    Define the sum between two Colors
    ---- Inputs: --------
        * color2: A Color
    ---- Outputs: --------
        * Color: the sum of two Colors
    
    """
    # ---------------------

    def __add__(self, color2: "Color"):
        return Color(arr=self.arr + color2.arr)
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/ColorTest.py:test_add
        --- OR ---- 
        python3 -m nose -v ../test/ColorTest.py:test_add
        --- OR ---- 
        python -m nose -v ../test/ColorTest.py:test_add
        ---------------------------------------------------
    """

    # ---------------------
    """
    Define the difference between two Colors
    ---- Inputs: --------
        * color2: A Color
    ---- Outputs: --------
        * Color: the difference of two Colors
    """
    # ---------------------

    def __sub__(self, color2: "Color"):
        return Color(arr=self.arr - color2.arr)
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/ColorTest.py:test_subtract
        --- OR ---- 
        python3 -m nose -v ../test/ColorTest.py:test_subtract
        --- OR ---- 
        python -m nose -v ../test/ColorTest.py:test_subtract
        ---------------------------------------------------
    """

    # ---------------------
    """
    Define the product of a Color and a scalar or another Color
    Multiplying scalar is to create a new color
    Multiplying two colors together is to blend these colors
    The order is not interchangeable for color * scalar 
    But interchangeable for color * color
    ---- Inputs: --------
        * multi: A scalar or a Color
    ---- Outputs: --------
        * Tuple: the product of a Color and a scalar or another Color
    """
    # ---------------------

    def __mul__(self, multi):
        if type(multi) == float or type(multi) == int:
            return Color(arr=self.arr * multi)
        return Color(arr=self.arr*multi.arr)
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/ColorTest.py:test_multi
        --- OR ---- 
        python3 -m nose -v ../test/ColorTest.py:test_multi
        --- OR ---- 
        python -m nose -v ../test/ColorTest.py:test_multi
        ---------------------------------------------------
    """
