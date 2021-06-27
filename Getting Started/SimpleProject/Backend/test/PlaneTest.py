import numpy as np
import math
from Backend.src.Plane import Plane
from Backend.src.Ray import Ray
from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix
from Backend.src.Intersection import Intersection
from Backend.src.Material import Material


# ---------------------------------------------------


def test_intersect():
    s = Plane()
    r = Ray(Tuple.point(0, 10, 0), Tuple.vector(0, 0, 1))
    count, result = s.intersect(r)
    assert count == 0

    s = Plane()
    r = Ray(Tuple.point(0, 0, 0), Tuple.vector(0, 0, 1))
    count, result = s.intersect(r)
    assert count == 0

    s = Plane()
    r = Ray(Tuple.point(0, 1, 0), Tuple.vector(0, -1, 0))
    count, result = s.intersect(r)
    assert count == 1
    assert result[0].t == 1
    assert result[0].shape == s

    s = Plane()
    r = Ray(Tuple.point(0, -1, 0), Tuple.vector(0, 1, 0))
    count, result = s.intersect(r)
    assert count == 1
    assert result[0].t == 1
    assert result[0].shape == s

# ---------------------------------------------------


def test_normalAt():
    s = Plane()
    assert s.normalAt(Tuple.point(0, 0, 0)) == Tuple.vector(0, 1, 0)
    assert s.normalAt(Tuple.point(10, 0, -10)) == Tuple.vector(0, 1, 0)
    assert s.normalAt(Tuple.point(-5, 0, 150)) == Tuple.vector(0, 1, 0)
