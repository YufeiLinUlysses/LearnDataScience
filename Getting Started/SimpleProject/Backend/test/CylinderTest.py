import numpy as np
import math
from Backend.src.Cylinder import Cylinder
from Backend.src.Ray import Ray
from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix
from Backend.src.Intersection import Intersection
from Backend.src.Material import Material

# ---------------------------------------------------


def test_intersect():
    points = [
        Tuple.point(1, 0, 0),
        Tuple.point(0, 0, 0),
        Tuple.point(0, 0, -5),
        Tuple.point(1, 0, -5),
        Tuple.point(0, 0, -5),
        Tuple.point(0.5, 0, -5),
        Tuple.point(0, 1.5, 0),
        Tuple.point(0, 3, -5),
        Tuple.point(0, 0, -5),
        Tuple.point(0, 2, -5),
        Tuple.point(0, 1, -5),
        Tuple.point(0, 1.5, -2),
        Tuple.point(0, 3, 0),
        Tuple.point(0, 3, -2),
        Tuple.point(0, 4, -2),
        Tuple.point(0, 0, -2),
        Tuple.point(0, -1, -2),

    ]
    vectors = [
        Tuple.vector(0, 1, 0),
        Tuple.vector(0, 1, 0),
        Tuple.vector(1, 1, 1),
        Tuple.vector(0, 0, 1),
        Tuple.vector(0, 0, 1),
        Tuple.vector(0.1, 1, 1),
        Tuple.vector(0.1, 1, 0),
        Tuple.vector(0, 0, 1),
        Tuple.vector(0, 0, 1),
        Tuple.vector(0, 0, 1),
        Tuple.vector(0, 0, 1),
        Tuple.vector(0, 0, 1),
        Tuple.vector(0, -1, 0),
        Tuple.vector(0, -1, 2),
        Tuple.vector(0, -1, 1),
        Tuple.vector(0, 1, 2),
        Tuple.vector(0, 1, 1)
    ]
    results = [
        (5, 5), (4, 6), (6.80798, 7.08872)
    ]

    for i in range(len(points)):
        r = Ray(points[i], vectors[i].normalize())
        if i < 6:
            s = Cylinder()
            count, result = s.intersect(r)
            if i < 3:
                assert count == 0
            elif i == 3:
                assert result[0].t - 5 <= 0.0001
                assert result[1].t - 5 <= 0.0001
            elif i == 4:
                assert result[0].t - 4 <= 0.0001
                assert result[1].t - 6 <= 0.0001
            elif i == 5:
                assert result[0].t - 6.80798 <= 0.0001
                assert result[1].t - 7.08872 <= 0.0001
        elif i < 12:
            s = Cylinder(1, 2)
            count, result = s.intersect(r)
            if i == 11:
                assert count == 2
            else:
                assert count == 0
        else:
            s = Cylinder(1, 2, True)
            count, result = s.intersect(r)
            assert count == 2


def test_normal():
    points = [
        Tuple.point(1, 0, 0),
        Tuple.point(0, 5, -1),
        Tuple.point(0, -2, 1),
        Tuple.point(-1, 1, 0),
        Tuple.point(0, 1, 0),
        Tuple.point(0.5, 1, 0),
        Tuple.point(0, 1, 0.5),
        Tuple.point(0, 2, 0),
        Tuple.point(0.5, 2, 0),
        Tuple.point(0, 2, 0.5),

    ]
    results = [
        Tuple.vector(1, 0, 0),
        Tuple.vector(0, 0, -1),
        Tuple.vector(0, 0, 1),
        Tuple.vector(-1, 0, 0),
        Tuple.vector(0, -1, 0),
        Tuple.vector(0, -1, 0),
        Tuple.vector(0, -1, 0),
        Tuple.vector(0, 1, 0),
        Tuple.vector(0, 1, 0),
        Tuple.vector(0, 1, 0),
    ]

    for i in range(len(results)):
        if i < 4:
            s = Cylinder()
            assert s.normalAt(points[i]) == results[i]
        else:
            s = Cylinder(1, 2, True)
            assert s.normalAt(points[i]) == results[i]
