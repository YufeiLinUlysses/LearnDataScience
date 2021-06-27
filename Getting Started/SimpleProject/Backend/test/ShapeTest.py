import numpy as np
import math
from Backend.src.Sphere import Sphere
from Backend.src.Group import Group
from Backend.src.Ray import Ray
from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix
from Backend.src.Intersection import Intersection
from Backend.src.Material import Material


# ---------------------------------------------------
def test_worldToObject():
    g1 = Group()
    g1.transform = Matrix.rotateY(math.pi/2)
    g2 = Group()
    g2.transform = Matrix.scaling(2, 2, 2)
    g1.addChild(g2)
    s = Sphere()
    s.transform = Matrix.translation(5, 0, 0)
    g2.addChild(s)
    assert s.worldToObject(Tuple.point(-2, 0, -10)) == Tuple.point(0, 0, -1)

# ---------------------------------------------------


def test_normalToWorld():
    g1 = Group()
    g1.transform = Matrix.rotateY(math.pi/2)
    g2 = Group()
    g2.transform = Matrix.scaling(1, 2, 3)
    g1.addChild(g2)
    s = Sphere()
    s.transform = Matrix.translation(5, 0, 0)
    g2.addChild(s)
    assert s.normalToWorld(Tuple.vector(
        3**0.5/3, 3**0.5/3, 3**0.5/3)) == Tuple.vector(0.2857, 0.4286, -0.8571)


# ---------------------------------------------------


def test_normalAt():
    g1 = Group()
    g1.transform = Matrix.rotateY(math.pi/2)
    g2 = Group()
    g2.transform = Matrix.scaling(1, 2, 3)
    g1.addChild(g2)
    s = Sphere()
    s.transform = Matrix.translation(5, 0, 0)
    g2.addChild(s)
    assert s.normalAt(Tuple.point(1.7321, 1.1547, -5.5774)
                      ) == Tuple.vector(0.2857, 0.4286, -0.8571)
