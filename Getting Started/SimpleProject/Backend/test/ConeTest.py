import numpy as np
import math
from Backend.src.Cone import Cone
from Backend.src.Ray import Ray
from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix
from Backend.src.Intersection import Intersection
from Backend.src.Material import Material

# ---------------------------------------------------


def test_intersect():
    points = [
        Tuple.point(0, 0, -5),
        Tuple.point(0, 0, -5),
        Tuple.point(1, 1, -5),
        Tuple.point(0, 0, -1),
        Tuple.point(0, 0, -5),
        Tuple.point(0, 0, -0.25),
        Tuple.point(0, 0, -0.25),
    ]
    vectors = [
        Tuple.vector(0, 0, 1),
        Tuple.vector(1, 1, 1),
        Tuple.vector(-0.5, -1, 1),
        Tuple.vector(0, 1, 1),
        Tuple.vector(0, 1, 0),
        Tuple.vector(0, 1, 1),
        Tuple.vector(0, 1, 0)
    ]
    results = [
        (5, 5), (8.66025, 8.66025), (4.55006,
                                     49.44994), (1, 0.35355), (0), (2), (4)
    ]

    for i in range(len(points)):
        r = Ray(points[i], vectors[i].normalize())
        if i < 4:
            s = Cone()
            count, result = s.intersect(r)
            if i < 3:
                assert count == 2
                assert result[0].t - results[i][0] <= 0.0001
                assert result[1].t - results[i][1] <= 0.0001
            elif i == 3:
                assert count == 1
                assert result[0].t - results[i][1] <= 0.0001
        else:
            s = Cone(-0.5, 0.5, True)
            count, result = s.intersect(r)
            assert count == results[i]


def test_normal():
    points = [
        Tuple.point(0, 0, 0),
        Tuple.point(1, 1, 1),
        Tuple.point(-1, -1, 0)
    ]
    results = [
        Tuple.vector(0, 0, 0),
        Tuple.vector(1, -2**0.5, 1),
        Tuple.vector(-1, 1, 0)
    ]
    s = Cone()
    for i in range(len(results)):
        assert s.normalAt(points[i]) == results[i].normalize()
