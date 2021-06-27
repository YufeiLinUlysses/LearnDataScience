import numpy as np
import math
from Backend.src.ObjParser import ObjParser
from Backend.src.Triangle import Triangle
from Backend.src.Ray import Ray
from Backend.src.Tuple import Tuple
from Backend.src.Matrix import Matrix
from Backend.src.Intersection import Intersection
from Backend.src.Material import Material


# ---------------------------------------------------


def test_parse():
    p = ObjParser()
    p.parse("../testFiles/ObjParserTest1.obj")
    assert p.vertices == []

    p2 = ObjParser()
    p2.parse("../testFiles/ObjParserTest2.obj")
    assert p2.vertices[0] == Tuple.point(-1, 1, 0)
    assert p2.vertices[1] == Tuple.point(-1, 0.5, 0)
    assert p2.vertices[2] == Tuple.point(1, 0, 0)
    assert p2.vertices[3] == Tuple.point(1, 1, 0)
    assert p2.defaultGroup.objects[0] == Triangle(
        p2.vertices[0], p2.vertices[1], p2.vertices[2])
    assert p2.defaultGroup.objects[1] == Triangle(
        p2.vertices[0], p2.vertices[2], p2.vertices[3])

    p3 = ObjParser()
    p3.parse("../testFiles/ObjParserTest3.obj")
    assert p3.defaultGroup.objects[0] == Triangle(
        p3.vertices[0], p3.vertices[1], p3.vertices[2])
    assert p3.defaultGroup.objects[1] == Triangle(
        p3.vertices[0], p3.vertices[2], p3.vertices[3])
    assert p3.defaultGroup.objects[2] == Triangle(
        p3.vertices[0], p3.vertices[3], p3.vertices[4])

    p4 = ObjParser()
    p4.parse("../testFiles/ObjParserTest4.obj")
    assert p4.defaultGroup.objects[0] == p4.subGroups["FirstGroup"]
    assert p4.defaultGroup.objects[0].objects[0] == Triangle(
        p4.vertices[0], p4.vertices[1], p4.vertices[2])
    assert p4.defaultGroup.objects[1] == p4.subGroups["SecondGroup"]
    assert p4.defaultGroup.objects[1].objects[0] == Triangle(
        p4.vertices[0], p4.vertices[2], p4.vertices[3])

    p5 = ObjParser()
    p5.parse("../testFiles/ObjParserTest5.obj")
    assert p5.normals[0] == Tuple.vector(0, 0, 1)
    assert p5.normals[1] == Tuple.vector(0.707, 0, -0.707)
    assert p5.normals[2] == Tuple.vector(1, 2, 3)

    p1 = Tuple.point(0, 1, 0)
    p2 = Tuple.point(-1, 0, 0)
    p3 = Tuple.point(1, 0, 0)
    n1 = Tuple.vector(0, 1, 0)
    n2 = Tuple.vector(-1, 0, 0)
    n3 = Tuple.vector(1, 0, 0)
    t = Triangle(p1, p2, p3, n1, n2, n3)
    p6 = ObjParser()
    p6.parse("../testFiles/ObjParserTest6.obj")
    assert p6.defaultGroup.objects[0] == t
    assert p6.defaultGroup.objects[1] == t
