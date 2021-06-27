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


def test_addChild():
    g = Group()
    s = Sphere()
    g.addChild(s)
    assert s in g.objects
    assert s.parent == g


# ---------------------------------------------------


def test_intersect():
    p = Group()
    r = Ray(Tuple.point(0, 0, 0), Tuple.vector(0, 0, 1))
    count, result = p.intersect(r)
    assert count == 0
    s1 = Sphere()
    s2 = Sphere()
    s2.transform = Matrix.translation(0, 0, -3)
    s3 = Sphere()
    s3.transform = Matrix.translation(5, 0, 0)
    r = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
    q = Group()
    q.addChild(s1)
    q.addChild(s2)
    q.addChild(s3)
    count, result = q.intersect(r)
    assert count == 4
    assert result[0].shape == s2
    assert result[1].shape == s2
    assert result[2].shape == s1
    assert result[3].shape == s1
    g = Group()
    g.transform = Matrix.scaling(2, 2, 2)
    s = Sphere()
    s.transform = Matrix.translation(5, 0, 0)
    g.addChild(s)
    r = Ray(Tuple.point(10, 0, -10), Tuple.vector(0, 0, 1))
    count, xs = g.intersect(r)
    assert count == 2
