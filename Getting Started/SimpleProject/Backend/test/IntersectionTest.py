from Backend.src.Intersection import Intersection
from Backend.src.Sphere import Sphere

# ---------------------------------------------------


def test_hit():
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = [i1, i2]
    assert Intersection.hit(xs) == i1

    i1 = Intersection(-1, s)
    i2 = Intersection(1, s)
    xs = [i1, i2]
    assert Intersection.hit(xs) == i2

    i1 = Intersection(-2, s)
    i2 = Intersection(-1, s)
    xs = [i1, i2]
    assert Intersection.hit(xs) == Intersection()

    i1 = Intersection(5, s)
    i2 = Intersection(7, s)
    i3 = Intersection(-3, s)
    i4 = Intersection(2, s)
    xs = [i1, i2, i3, i4]
    assert Intersection.hit(xs) == i4
