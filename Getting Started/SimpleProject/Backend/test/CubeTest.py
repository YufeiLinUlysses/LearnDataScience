import numpy as np
import math
from Backend.src.Cube import Cube
from Backend.src.Ray import Ray
from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix
from Backend.src.Intersection import Intersection
from Backend.src.Material import Material

# ---------------------------------------------------


def test_intersect():
    s = Cube()
    points = [
        Tuple.point(5, 0.5, 0),
        Tuple.point(-5, 0.5, 0),
        Tuple.point(0.5, 5, 0),
        Tuple.point(0.5, -5, 0),
        Tuple.point(0.5, 0, 5),
        Tuple.point(0.5, 0, -5),
        Tuple.point(0, 0.5, 0),
        Tuple.point(-2, 0, 0),
        Tuple.point(0, -2, 0),
        Tuple.point(0, 0, -2),
        Tuple.point(2, 0, 2),
        Tuple.point(0, 2, 2),
        Tuple.point(2, 2, 0),
    ]
    vectors = [
        Tuple.vector(-1, 0, 0),
        Tuple.vector(1, 0, 0),
        Tuple.vector(0, -1, 0),
        Tuple.vector(0, 1, 0),
        Tuple.vector(0, 0, -1),
        Tuple.vector(0, 0, 1),
        Tuple.vector(0, 0, 1),
        Tuple.vector(0.2673, 0.5345, 0.8018),
        Tuple.vector(0.8018, 0.2673, 0.5345),
        Tuple.vector(0.5345, 0.8018, 0.2673),
        Tuple.vector(0, 0, -1),
        Tuple.vector(0, -1, 0),
        Tuple.vector(-1, 0, 0)
    ]
    results = [
        (4, 6), (-1, 1),
    ]

    for i in range(len(points)):
        r = Ray(points[i], vectors[i])
        count, result = s.intersect(r)
        if i < 6:
            assert result[0].t - 4 <= 0.0001
            assert result[1].t - 6 <= 0.0001
        elif i == 6:
            assert result[0].t + 1 <= 0.0001
            assert result[1].t - 1 <= 0.0001
        else:
            assert count == 0


def test_normal():
    s = Cube()
    points = [
        Tuple.point(1, 0.5, -0.8),
        Tuple.point(-1, -0.2, 0.9),
        Tuple.point(-0.4, 1, -0.1),
        Tuple.point(0.3, -1, -0.7),
        Tuple.point(-0.6, 0.3, 1),
        Tuple.point(0.4, 0.4, -1),
        Tuple.point(1, 1, 1),
        Tuple.point(-1, -1, -1),
    ]
    results = [
        Tuple.vector(1, 0, 0),
        Tuple.vector(-1, 0, 0),
        Tuple.vector(0, 1, 0),
        Tuple.vector(0, -1, 0),
        Tuple.vector(0, 0, 1),
        Tuple.vector(0, 0, -1),
        Tuple.vector(1, 0, 0),
        Tuple.vector(-1, 0, 0)
    ]

    for i in range(len(results)):
        assert s.normalAt(points[i]) == results[i]
