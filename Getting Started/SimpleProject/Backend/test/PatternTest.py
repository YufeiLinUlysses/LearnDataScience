from Backend.src.Pattern import Pattern
from Backend.src.Color import Color
from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix
from Backend.src.Sphere import Sphere

# ---------------------------------------------------

white = Color(1, 1, 1)
black = Color(0, 0, 0)


def test_stripe():
    p = Pattern(Color(1, 1, 1), Color(0, 0, 0))

    assert p.stripe(Tuple.point(0, 0, 0)) == p.c1
    assert p.stripe(Tuple.point(0, 1, 0)) == p.c1
    assert p.stripe(Tuple.point(0, 2, 0)) == p.c1
    assert p.stripe(Tuple.point(0, 0, 1)) == p.c1
    assert p.stripe(Tuple.point(0, 0, 2)) == p.c1
    assert p.stripe(Tuple.point(0.9, 0, 0)) == p.c1
    assert p.stripe(Tuple.point(-0.1, 0, 0)) == p.c2
    assert p.stripe(Tuple.point(-1, 0, 0)) == p.c2
    assert p.stripe(Tuple.point(1, 0, 0)) == p.c2
    assert p.stripe(Tuple.point(-1.1, 0, 0)) == p.c1

# ---------------------------------------------------


def test_patternAtObject():
    s = Sphere()
    s.transform = Matrix.scaling(2, 2, 2)
    p = Pattern(Color(1, 1, 1), Color(0, 0, 0))
    assert p.patternAtObject(Tuple.point(1.5, 0, 0), s.transform) == p.c1
    s2 = Sphere()
    p.transform = Matrix.scaling(2, 2, 2)
    assert p.patternAtObject(Tuple.point(1.5, 0, 0), s2.transform) == p.c1
    p.transform = Matrix.translation(0.5, 0, 0)
    assert p.patternAtObject(Tuple.point(1.5, 0, 0), s.transform) == p.c1
    p2 = Pattern(Color(1, 1, 1), Color(0, 0, 0), patternType="")
    assert p2.patternAtObject(Tuple.point(
        2, 3, 4), s.transform) == Color(1, 1.5, 2)
    p2.transform = Matrix.scaling(2, 2, 2)
    assert p2.patternAtObject(Tuple.point(
        2, 3, 4), s2.transform) == Color(1, 1.5, 2)
    p2.transform = Matrix.translation(0.5, 1, 1.5)
    assert p2.patternAtObject(Tuple.point(
        2.5, 3, 3.5), s.transform) == Color(0.75, 0.5, 0.25)

# ---------------------------------------------------


def test_gradient():
    p = Pattern(white, black)

    assert p.gradient(Tuple.point(0, 0, 0)) == white
    assert p.gradient(Tuple.point(0.25, 0, 0)) == Color(0.75, 0.75, 0.75)
    assert p.gradient(Tuple.point(0.5, 0, 0)) == Color(0.5, 0.5, 0.5)
    assert p.gradient(Tuple.point(0.75, 0, 0)) == Color(0.25, 0.25, 0.25)

# ---------------------------------------------------


def test_ring():
    p = Pattern(white, black)

    assert p.ring(Tuple.point(0, 0, 0)) == white
    assert p.ring(Tuple.point(1, 0, 0)) == black
    assert p.ring(Tuple.point(0, 0, 1)) == black
    assert p.ring(Tuple.point(0.708, 0, 0.708)) == black

# ---------------------------------------------------


def test_checker():
    p = Pattern(white, black)

    assert p.checker(Tuple.point(0, 0, 0)) == white
    assert p.checker(Tuple.point(0.99, 0, 0)) == white
    assert p.checker(Tuple.point(1.01, 0, 0)) == black
    assert p.checker(Tuple.point(0, 0.99, 0)) == white
    assert p.checker(Tuple.point(0, 1.01, 0)) == black
    assert p.checker(Tuple.point(0, 0, 0.99)) == white
    assert p.checker(Tuple.point(0, 0, 1.01)) == black
