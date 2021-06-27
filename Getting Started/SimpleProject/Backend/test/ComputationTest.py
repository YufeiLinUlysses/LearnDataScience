from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix
from Backend.src.Ray import Ray
from Backend.src.Computation import Computation
from Backend.src.Sphere import Sphere
from Backend.src.Plane import Plane
from Backend.src.Intersection import Intersection

import numpy as np


# ---------------------------------------------------


def test_init():
    ray = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(4, shape)
    comp = Computation(i, ray)
    assert comp.t == i.t
    assert comp.shape == i.shape
    assert comp.point == Tuple.point(0, 0, -1)
    assert comp.eyev == Tuple.vector(0, 0, -1)
    assert comp.normalv == Tuple.vector(0, 0, -1)
    assert comp.inside == False

    ray = Ray(Tuple.point(0, 0, 0), Tuple.vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(1, shape)
    comp = Computation(i, ray)
    assert comp.t == i.t
    assert comp.shape == i.shape
    assert comp.point == Tuple.point(0, 0, 1)
    assert comp.eyev == Tuple.vector(0, 0, -1)
    assert comp.inside == True
    assert comp.normalv == Tuple.vector(0, 0, -1)

    ray = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
    shape = Sphere()
    shape.transform = Matrix.translation(0, 0, 1)
    i = Intersection(1, shape)
    comp = Computation(i, ray)
    assert comp.overPoint.z < -0.00001/2
    assert comp.point.z > comp.overPoint.z

    ray = Ray(Tuple.point(0, 1, -1), Tuple.vector(0, -2**0.5/2, 2**0.5/2))
    shape = Plane()
    shape.transform = Matrix.translation(0, 0, 1)
    i = Intersection(2**0.5, shape)
    comp = Computation(i, ray)
    assert comp.reflectv == Tuple.vector(0, 2**0.5/2, 2**0.5/2)

    A = Sphere.glassSphere()
    A.transform = Matrix.scaling(2, 2, 2)
    B = Sphere.glassSphere()
    B.transform = Matrix.translation(0, 0, -0.25)
    B.material.refractiveIndex = 2
    C = Sphere.glassSphere()
    C.transform = Matrix.translation(0, 0, 0.25)
    C.material.refractiveIndex = 2.5
    ray = Ray(Tuple.point(0, 0, -4), Tuple.vector(0, 0, 1))
    xs = [Intersection(2, A), Intersection(2.75, B),
          Intersection(3.25, C), Intersection(4.75, B),
          Intersection(5.25, C), Intersection(6, A)]
    result = [(1, 1.5), (1.5, 2), (2, 2.5), (2.5, 2.5), (2.5, 1.5), (1.5, 1)]
    assert A != B and B != C and A != C
    for i in range(6):
        c = Computation(xs[i], ray, xs)
        assert c.n1 == result[i][0]
        assert c.n2 == result[i][1]

    s = Sphere.glassSphere()
    s.transform = Matrix.translation(0, 0, 1)
    ray = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
    i = Intersection(5, s)
    xs = [i]
    c = Computation(i, ray, xs)
    assert c.underPoint.z > 0.00001/2
    assert c.point.z < c.underPoint.z

# ---------------------------------------------------


def test_schlick():
    s = Sphere.glassSphere()
    ray = Ray(Tuple.point(0, 0, 2**0.5/2), Tuple.vector(0, 1, 0))
    xs = [Intersection(-2**0.5/2, s), Intersection(2**0.5/2, s)]
    comp = Computation(xs[1], ray, xs)
    assert comp.schlick() - 1 <= 0.00001

    ray = Ray(Tuple.point(0, 0, 0), Tuple.vector(0, 1, 0))
    xs = [Intersection(-1, s), Intersection(1, s)]
    comp = Computation(xs[1], ray, xs)
    assert comp.schlick() - 0.04 <= 0.00001

    ray = Ray(Tuple.point(0, 0.99, -2), Tuple.vector(0, 0, 1))
    xs = [Intersection(1.8589, s)]
    comp = Computation(xs[0], ray, xs)
    assert comp.schlick() - 0.48873 <= 0.00001
