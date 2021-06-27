import numpy as np
import math
from Backend.src.Sphere import Sphere
from Backend.src.Ray import Ray
from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix
from Backend.src.Intersection import Intersection
from Backend.src.Material import Material



# ---------------------------------------------------


def test_intersect():
    s = Sphere()
    r = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
    count, result = s.intersect(r)
    assert result[0].t - 4 <= 0.0001
    assert result[1].t - 6 <= 0.0001

    r = Ray(Tuple.point(0, 1, -5), Tuple.vector(0, 0, 1))
    count, result = s.intersect(r)
    assert result[0].t - 5 <= 0.0001

    r = Ray(Tuple.point(0, 2, -5), Tuple.vector(0, 0, 1))
    count, result = s.intersect(r)
    assert count == 0

    r = Ray(Tuple.point(0, 0, 0), Tuple.vector(0, 0, 1))
    count, result = s.intersect(r)
    assert result[0].t + 1 <= 0.0001
    assert result[1].t - 1 <= 0.0001

    r = Ray(Tuple.point(0, 0, 5), Tuple.vector(0, 0, 1))
    count, result = s.intersect(r)
    assert result[0].t + 6 <= 0.0001
    assert result[0].shape == s
    assert result[0] == Intersection(-6, s)
    assert result[1].t + 4 <= 0.0001

# ---------------------------------------------------


def test_transform():
    s = Sphere()
    assert np.allclose(s.transform.matrix, np.eye(4), atol=0.00001)
    s.transform = Matrix.translation(2, 3, 4)
    assert np.allclose(s.transform.matrix, Matrix.translation(
        2, 3, 4).matrix, atol=0.00001)

    r = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
    s = Sphere()
    s.transform = Matrix.scaling(2, 2, 2)
    count, xs = s.intersect(r)
    assert count == 2
    assert xs[0].t == 3
    assert xs[1].t == 7
    assert Intersection.hit(xs) == xs[0]

    s = Sphere()
    s.transform = Matrix.translation(5, 0, 0)
    count, xs = s.intersect(r)
    assert count == 0


# ---------------------------------------------------


def test_nromalAt():
    s = Sphere()
    assert s.normalAt(Tuple.point(1, 0, 0)) == Tuple.vector(1, 0, 0)
    assert s.normalAt(Tuple.point(0, 1, 0)) == Tuple.vector(0, 1, 0)
    assert s.normalAt(Tuple.point(0, 0, 1)) == Tuple.vector(0, 0, 1)
    assert s.normalAt(Tuple.point(3**0.5/3, 3**0.5/3, 3**0.5/3)
                      ) == Tuple.vector(3**0.5/3, 3**0.5/3, 3**0.5/3)

    s.transform = Matrix.translation(0, 1, 0)
    assert s.normalAt(Tuple.point(0, 1.70711, -0.70711)
                      ) == Tuple.vector(0, 0.70711, -0.70711)

    s.transform = Matrix.scaling(1, 0.5, 1)*Matrix.rotateZ(math.pi/5)
    assert s.normalAt(Tuple.point(0, 2**0.5/2, -2**0.5/2)
                      ) == Tuple.vector(0, 0.97014, -0.24254)

# ---------------------------------------------------


def test_material():
    s = Sphere()
    m = Material()
    assert s.material == m
    m.ambient = 1
    s.material = m
    assert s.material == m
