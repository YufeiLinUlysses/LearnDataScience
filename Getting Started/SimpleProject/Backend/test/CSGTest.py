import numpy as np
import math
from Backend.src.CSG import CSG
from Backend.src.Sphere import Sphere
from Backend.src.Cube import Cube
from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix
from Backend.src.Intersection import Intersection
from Backend.src.Material import Material
from Backend.src.Ray import Ray

s1 = Sphere()
s2 = Cube()
c = CSG(s1, s2, "union")

# ---------------------------------------------------


def test_intersectionAllowed():
    lhit = [True, True, True, True, False, False, False, False]
    inl = [True, True, False, False, True, True, False, False]
    inr = [True, False, True, False, True, False, True, False]
    result = [False, True, False, True, False, False, True, True]
    for i in range(8):
        assert c.intersectionAllowed(lhit[i], inl[i], inr[i]) == result[i]
    c.operation = "intersect"
    result = [True, False, True, False, True, True, False, False]
    for i in range(8):
        assert c.intersectionAllowed(lhit[i], inl[i], inr[i]) == result[i]
    c.operation = "difference"
    result = [False, True, False, True, True, True, False, False]
    for i in range(8):
        assert c.intersectionAllowed(lhit[i], inl[i], inr[i]) == result[i]


# ---------------------------------------------------


def test_filterIntersection():
    c.operation = "union"
    xs = [Intersection(1, s1), Intersection(
        2, s2), Intersection(3, s1), Intersection(4, s2)]
    result = c.filterIntersection(xs)
    assert len(result) == 2
    assert result[0] == xs[0]
    assert result[1] == xs[3]

    c.operation = "intersect"
    result = c.filterIntersection(xs)
    assert len(result) == 2
    assert result[0] == xs[1]
    assert result[1] == xs[2]

    c.operation = "difference"
    result = c.filterIntersection(xs)
    assert len(result) == 2
    assert result[0] == xs[0]
    assert result[1] == xs[1]


# ---------------------------------------------------


def test_intersect():
    c.operation = "union"
    r = Ray(Tuple.point(0, 2, -5), Tuple.vector(0, 0, 1))
    count, result = c.intersect(r)
    assert count == 0
    assert result == []

    s1 = Sphere()
    s2 = Sphere()
    s2.transform = Matrix.translation(0, 0, 0.5)
    csg = CSG(s1, s2, "union")
    r = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
    count, result = csg.intersect(r)
    assert count == 2
    assert result[0].t == 4
    assert result[0].shape == s1
    assert result[1].t == 6.5
    assert result[1].shape == s2
