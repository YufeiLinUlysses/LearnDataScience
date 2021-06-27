import numpy as np
import math
from Backend.src.Triangle import Triangle
from Backend.src.Ray import Ray
from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix
from Backend.src.Intersection import Intersection
from Backend.src.Material import Material
from Backend.src.Computation import Computation


# ---------------------------------------------------


def test_init():
    p1 = Tuple.point(0, 1, 0)
    p2 = Tuple.point(-1, 0, 0)
    p3 = Tuple.point(1, 0, 0)
    t = Triangle(p1, p2, p3)
    assert t.e1 == Tuple.vector(-1, -1, 0)
    assert t.e2 == Tuple.vector(1, -1, 0)
    assert t.normal == Tuple.vector(0, 0, -1)

# ---------------------------------------------------


def test_intersect():
    p1 = Tuple.point(0, 1, 0)
    p2 = Tuple.point(-1, 0, 0)
    p3 = Tuple.point(1, 0, 0)
    n1 = Tuple.vector(0, 1, 0)
    n2 = Tuple.vector(-1, 0, 0)
    n3 = Tuple.vector(1, 0, 0)
    t = Triangle(p1, p2, p3)
    r = Ray(Tuple.point(0, -1, -2), Tuple.vector(0, 1, 0))
    count, result = t.intersect(r)
    assert count == 0
    r = Ray(Tuple.point(1, 1, -2), Tuple.vector(0, 0, 1))
    count, result = t.intersect(r)
    assert count == 0
    r = Ray(Tuple.point(-1, 1, -2), Tuple.vector(0, 0, 1))
    count, result = t.intersect(r)
    assert count == 0
    r = Ray(Tuple.point(0, -1, -2), Tuple.vector(0, 0, 1))
    count, result = t.intersect(r)
    assert count == 0
    r = Ray(Tuple.point(0, 0.5, -2), Tuple.vector(0, 0, 1))
    count, result = t.intersect(r)
    assert result[0].t - 2 <= 0.00001

    t2 = Triangle(p1, p2, p3, n1, n2, n3)
    r = Ray(Tuple.point(-0.2, 0.3, -2), Tuple.vector(0, 0, 1))
    count, result = t2.intersect(r)
    assert result[0].u - 0.45 <= 0.00001
    assert result[0].v - 0.25 <= 0.00001
# ---------------------------------------------------


def test_normalAt():
    p1 = Tuple.point(0, 1, 0)
    p2 = Tuple.point(-1, 0, 0)
    p3 = Tuple.point(1, 0, 0)
    n1 = Tuple.vector(0, 1, 0)
    n2 = Tuple.vector(-1, 0, 0)
    n3 = Tuple.vector(1, 0, 0)

    t = Triangle(p1, p2, p3)
    assert t.normalAt(Tuple.point(0, 0.5, 0)) == t.normal
    assert t.normalAt(Tuple.point(-0.5, 0.75, 0)) == t.normal
    assert t.normalAt(Tuple.point(0.5, 0.25, 0)) == t.normal

    t2 = Triangle(p1, p2, p3, n1, n2, n3)
    i = Intersection(1, t2, 0.45, 0.25)
    assert t2.normalAt(Tuple.point(0, 0, 0),
                       hit=i) == Tuple.vector(-0.5547, 0.83205, 0)
    r = Ray(Tuple.point(-0.2, 0.3, -2), Tuple.vector(0, 0, 1))
    xs = [i]
    comp = Computation(i, r, xs)
    assert comp.normalv == Tuple.vector(-0.5547, 0.83205, 0)
