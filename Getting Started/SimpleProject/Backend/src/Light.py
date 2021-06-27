import numpy as np
from Tuple import Tuple
from Color import Color
# ---------------------
""" 
Light class describes the light in the world. 
Each light contains 2 elements: position and intensity
position: a Tuple, the origin where light locates
intensity: a Color, the color of the light

Light class contains the following functions:
__init__
__str__
__eq__
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/LightTest.py
    --- OR ---- 
    python3 -m nose -v ../test/LightTest.py
    --- OR ---- 
    python -m nose -v ../test/LightTest.py
    ---------------------------------------------------
"""


class Light():
    # ---------------------
    """
    Light takes in two parameters: position and intensity
    position is a Tuple
    intensity is a Color
    """
    # ---------------------

    def __init__(self, position: "Tuple" = None, intensity: "Color" = None):
        if not position and not intensity:
            self.position = Tuple.point(0, 0, 0)
            self.intensity = Color()
        else:
            self.position = position
            self.intensity = intensity

    # ---------------------
    """
    Define the output format for Light class
    """
    # ---------------------

    def __str__(self):
        return "Position: " + str(self.position) + " Color: " + str(self.intensity)

    # ---------------------
    """
    Define equivalence of two Light instances
    """
    # ---------------------

    def __eq__(self, light2: "Light"):
        return self.intensity == light2.intensity and self.position == light2.position
