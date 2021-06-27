import numpy as np
from Matrix import Matrix
from Tuple import Tuple
from Ray import Ray
from Canvas import Canvas
from World import World
# ---------------------
""" 
Camera class helps to set up a camera in the scene and this would define the angle and distance we will be looking at the scene.
Each camera contains 7 elements:
hsize: a float, define the horizontal size of the canvas in pixels
vsize: a float, define the vertical size of the canvas in pixels
fieldOfView: a float, the radian angle describes how much the camera could see
transform: a Matrix, describe the transform matrix of the camera
halfWidth: a float, define the view on half of the width
halfHeight: a float, define the view on half of the height
pixelSize: a float define the size of a pixel in the scene

Camera class contains the following functions:
__init__
__eq__
rayForPixel
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/CameraTest.py
    --- OR ---- 
    python3 -m nose -v ../test/CameraTest.py
    --- OR ---- 
    python -m nose -v ../test/CameraTest.py
    ---------------------------------------------------
"""


class Camera():
    # ---------------------
    """
    Camera class takes in three numbers
    hsize is horizontal size, vsize is vertical size, fieldOfView is the field of view of the camera
    """
    # ---------------------

    def __init__(self, hsize: float, vsize: float, fieldOfView: float):
        self.hsize = hsize
        self.vsize = vsize
        self.fieldOfView = fieldOfView
        self.transform = Matrix(matrix=np.eye(4))
        # In this part we calculate pixelSize
        halfView = np.tan(fieldOfView/2)
        # determine whether it is a horizontal or vertical view
        aspect = hsize/vsize
        if aspect >= 1:
            self.halfWidth = halfView
            self.halfHeight = halfView/aspect
        else:
            self.halfWidth = halfView * aspect
            self.halfHeight = halfView
        self.pixelSize = self.halfWidth * 2/self.hsize

    # ---------------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/CameraTest.py:test_init
        --- OR ---- 
        python3 -m nose -v ../test/CameraTest.py:test_init
        --- OR ---- 
        python -m nose -v ../test/CameraTest.py:test_init
        ---------------------------------------------------
    """

    # ---------------------
    """
    Define equivalence of two Canvas instances
    """
    # ---------------------

    def __eq__(self, camera2: "Camera"):
        return self.fieldOfView == camera2.fieldOfView and self.transform == camera2.transform and self.hsize == camera2.hsize and self.vsize == camera2.vsize

    # ---------------------
    """
    rayForPixel takes in the x and y coordinate and get the ray on that point
    ---- Inputs: --------
        * px: a float, x coordinate
        * py: a float, y coordinate 
    ---- Outputs: --------
        * ray: a ray on that pixel point
    """
    # ---------------------

    def rayForPixel(self, px: float, py: float):
        xOffset = (px+0.5) * self.pixelSize
        yOffset = (py+0.5) * self.pixelSize
        wx = self.halfWidth - xOffset
        wy = self.halfHeight - yOffset
        pixel = ~self.transform * Tuple.point(wx, wy, -1)
        origin = ~self.transform * Tuple.point(0, 0, 0)
        direction = (pixel-origin).normalize()
        return Ray(origin, direction)
    # ---------------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/CameraTest.py:test_rayForPixel
        --- OR ---- 
        python3 -m nose -v ../test/CameraTest.py:test_rayForPixel
        --- OR ---- 
        python -m nose -v ../test/CameraTest.py:test_rayForPixel
        ---------------------------------------------------
    """

    # ---------------------
    """
    render generates the image
    ---- Inputs: --------
        * world: a World containing all shapes and lights
    ---- Outputs: --------
        * image: a Canvas containing the calculated values
    """
    # ---------------------

    def render(self, world: "World"):
        image = Canvas(self.hsize, self.vsize)
        for y in range(self.vsize):
            for x in range(self.hsize):
                ray = self.rayForPixel(x, y)
                color = world.colorAt(ray)
                image.writePixel(x, y, color)
        return image
        # ---------------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/CameraTest.py:test_render
        --- OR ---- 
        python3 -m nose -v ../test/CameraTest.py:test_render
        --- OR ---- 
        python -m nose -v ../test/CameraTest.py:test_render
        ---------------------------------------------------
    """
