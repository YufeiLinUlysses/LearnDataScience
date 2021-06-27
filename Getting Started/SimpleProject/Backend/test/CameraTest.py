from Backend.src.Camera import Camera
from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix
from Backend.src.Ray import Ray
from Backend.src.World import World
from Backend.src.Color import Color
import math
# ---------------------------------------------------


def test_init():
    c = Camera(200, 125, math.pi/2)
    assert c.pixelSize - 0.01 <= 0.00001

    c = Camera(125, 200, math.pi/2)
    assert c.pixelSize - 0.01 <= 0.00001

# ---------------------------------------------------


def test_rayForPixel():
    c = Camera(201, 101, math.pi/2)
    assert c.rayForPixel(100, 50) == Ray(
        Tuple.point(0, 0, 0), Tuple.vector(0, 0, -1))

    c = Camera(201, 101, math.pi/2)
    assert c.rayForPixel(0, 0) == Ray(
        Tuple.point(0, 0, 0), Tuple.vector(0.66519, 0.33259, -0.66851))

    c = Camera(201, 101, math.pi/2)
    c.transform = Matrix.rotateY(math.pi/4) * Matrix.translation(0, -2, 5)
    assert c.rayForPixel(100, 50) == Ray(
        Tuple.point(0, 2, -5), Tuple.vector(2**0.5/2, 0, -2**0.5/2))

# ---------------------------------------------------


def test_render():
    w = World.defaultWorld()
    c = Camera(11, 11, math.pi/2)
    f = Tuple.point(0, 0, -5)
    t = Tuple.point(0, 0, 0)
    u = Tuple.vector(0, 1, 0)
    c.transform = Matrix.viewTransformation(f, t, u)
    image = c.render(w)
    assert image.pixelAt(5, 5) == Color(0.38066, 0.47583, 0.2855)
