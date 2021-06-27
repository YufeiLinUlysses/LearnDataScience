import numpy as np
import math
from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix
from Backend.src.Intersection import Intersection
from Backend.src.Material import Material
from Backend.src.Light import Light
from Backend.src.Color import Color
from Backend.src.Pattern import Pattern


# ---------------------------------------------------


def test_lighting():
    m = Material()
    position = Tuple.point(0, 0, 0)

    eyev1 = Tuple.vector(0, 0, -1)
    normalv = Tuple.vector(0, 0, -1)
    light1 = Light(Tuple.point(0, 0, -10), Color(1, 1, 1))
    assert m.lighting(light1, position, eyev1, normalv) == Color(1.9, 1.9, 1.9)

    eyev2 = Tuple.vector(0, 2**0.5/2, -2**0.5/2)
    assert m.lighting(light1, position, eyev2, normalv) == Color(1, 1, 1)

    light2 = Light(Tuple.point(0, 10, -10), Color(1, 1, 1))
    assert m.lighting(light2, position, eyev1, normalv) == Color(
        0.7364, 0.7364, 0.7364)

    eyev3 = Tuple.vector(0, -2**0.5/2, -2**0.5/2)
    assert m.lighting(light2, position, eyev3, normalv) == Color(
        1.6364, 1.6364, 1.6364)

    light3 = Light(Tuple.point(0, 0, 10), Color(1, 1, 1))
    assert m.lighting(light3, position, eyev1, normalv) == Color(0.1, 0.1, 0.1)

    assert m.lighting(light1, position, eyev1, normalv,
                      True) == Color(0.1, 0.1, 0.1)

    m.pattern = Pattern(Color(1, 1, 1), Color(0, 0, 0))
    m.ambient = 1
    m.diffuse = 0
    m.specular = 0
    assert m.lighting(light1, Tuple.point(0.9, 0, 0),
                      eyev1, normalv) == Color(1, 1, 1)
    assert m.lighting(light1, Tuple.point(1.1, 0, 0),
                      eyev1, normalv) == Color(0, 0, 0)
