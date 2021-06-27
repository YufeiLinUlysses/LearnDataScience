from Backend.src.Tuple import Tuple
import numpy as np


# ---------------------------------------------------


def test_add():
    t1 = Tuple(arr=np.array([3, -2, 5, 1]))
    t2 = Tuple(arr=np.array([-2, 3, 1, 0]))
    ans = Tuple(arr=np.array([1, 1, 6, 1]))
    assert t1 + t2 == ans

# ---------------------------------------------------


def test_subtract():
    t1 = Tuple.point(3, 2, 1)
    t2 = Tuple.point(5, 6, 7)
    ans = Tuple.vector(-2, -4, -6)
    assert t1 - t2 == ans

    t1 = Tuple.point(3, 2, 1)
    t2 = Tuple.vector(5, 6, 7)
    ans = Tuple.point(-2, -4, -6)
    assert t1 - t2 == ans

    t1 = Tuple.vector(3, 2, 1)
    t2 = Tuple.vector(5, 6, 7)
    ans = Tuple.vector(-2, -4, -6)
    assert t1 - t2 == ans

# ---------------------------------------------------


def test_multiScalar():
    t1 = Tuple(arr=np.array([1, -2, 3, -4]))
    s = 3.5
    ans = Tuple(arr=np.array([3.5, -7, 10.5, -14]))
    assert t1 * s == ans

    t1 = Tuple(arr=np.array([1, -2, 3, -4]))
    s = 0.5
    ans = Tuple(arr=np.array([0.5, -1, 1.5, -2]))
    assert t1 * s == ans

# ---------------------------------------------------


def test_divScalar():
    t1 = Tuple(arr=np.array([1, -2, 3, -4]))
    s = 2
    ans = Tuple(arr=np.array([0.5, -1, 1.5, -2]))
    assert t1 / s == ans

# ---------------------------------------------------


def test_point():
    t1 = Tuple.point(4, -4, 3)
    ans1 = Tuple(arr=np.array([4, -4, 3, 1]))
    assert t1 == ans1

    t2 = Tuple.point(4.3, -4.2, 3.1)
    ans2 = Tuple(arr=np.array([4.3, -4.2, 3.1, 1]))
    assert t2 == ans2

# ---------------------------------------------------


def test_vector():
    t1 = Tuple.vector(4, -4, 3)
    ans1 = Tuple(arr=np.array([4, -4, 3, 0]))
    assert t1 == ans1

    t2 = Tuple.vector(4.3, -4.2, 3.1)
    ans2 = Tuple(arr=np.array([4.3, -4.2, 3.1, 0]))
    assert t2 == ans2

# ---------------------------------------------------


def test_negate():
    t1 = Tuple.vector(0, 0, 0)
    t2 = Tuple.vector(1, -2, 3)
    ans1 = Tuple.vector(-1, 2, -3)
    assert t1 - t2 == ans1

    t3 = Tuple(arr=np.array([1, -2, 3, -4]))
    ans2 = Tuple(arr=np.array([-1, 2, -3, 4]))
    assert ~t3 == ans2

# ---------------------------------------------------


def test_magnitude():
    t1 = Tuple.vector(0, 1, 0)
    assert t1.magnitude() == 1

    t1 = Tuple.vector(0, 0, 1)
    assert t1.magnitude() == 1

    t1 = Tuple.vector(1, 2, 3)
    assert t1.magnitude() == 14**0.5

    t1 = Tuple.vector(-1, -2, -3)
    assert t1.magnitude() == 14**0.5

# ---------------------------------------------------


def test_dot():
    t1 = Tuple.vector(1, 2, 3)
    t2 = Tuple.vector(2, 3, 4)
    assert t1.dot(t2) == 20

# ---------------------------------------------------


def test_cross():
    t1 = Tuple.vector(1, 2, 3)
    t2 = Tuple.vector(2, 3, 4)
    assert t1.cross(t2) == Tuple.vector(-1, 2, -1)
    assert t2.cross(t1) == Tuple.vector(1, -2, 1)

# ---------------------------------------------------


def test_reflectV():
    v = Tuple.vector(1, -1, 0)
    n = Tuple.vector(0, 1, 0)
    assert v.reflectV(n) == Tuple.vector(1, 1, 0)

    v = Tuple.vector(0, -1, 0)
    n = Tuple.vector(2**0.5/2, 2**0.5/2, 0)
    assert v.reflectV(n) == Tuple.vector(1, 0, 0)
