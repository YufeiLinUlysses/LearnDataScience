from Backend.src.Ray import Ray
from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix


# ---------------------------------------------------


def test_position():
    r = Ray(Tuple.point(2, 3, 4), Tuple.vector(1, 0, 0))
    assert r.position(0) == Tuple.point(2, 3, 4)
    assert r.position(1) == Tuple.point(3, 3, 4)
    assert r.position(-1) == Tuple.point(1, 3, 4)
    assert r.position(2.5) == Tuple.point(4.5, 3, 4)

# ---------------------------------------------------


def test_transform():
    r = Ray(Tuple.point(1, 2, 3), Tuple.vector(0, 1, 0))
    m = Matrix.translation(3, 4, 5)
    assert r.transform(m) == Ray(Tuple.point(4, 6, 8), Tuple.vector(0, 1, 0))

    m = Matrix.scaling(2, 3, 4)
    assert r.transform(m) == Ray(Tuple.point(2, 6, 12), Tuple.vector(0, 3, 0))
