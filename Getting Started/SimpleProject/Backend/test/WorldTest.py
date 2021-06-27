import numpy as np
import math
import time
from Backend.src.World import World
from Backend.src.Matrix import Matrix
from Backend.src.Intersection import Intersection
from Backend.src.Material import Material
from Backend.src.Light import Light
from Backend.src.Color import Color
from Backend.src.Sphere import Sphere
from Backend.src.Plane import Plane
from Backend.src.Ray import Ray
from Backend.src.Tuple import Tuple
from Backend.src.Computation import Computation
from Backend.src.Pattern import Pattern


# ---------------------------------------------------


def test_intersectWorld():
    dw = World.defaultWorld()
    r = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
    count, result = dw.intersectWorld(r)
    assert count == 4
    assert result[0].t == 4
    assert result[1].t == 4.5
    assert result[2].t == 5.5
    assert result[3].t == 6

# ---------------------------------------------------


def test_defaultWorld():
    dw = World.defaultWorld()
    s0 = dw.shapes[0]
    s1 = dw.shapes[1]
    assert s0.material != s1.material

# ---------------------------------------------------


def test_shadeHit():
    dw = World.defaultWorld()
    r = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
    s = dw.shapes[0]
    i = Intersection(4, s)
    comp = Computation(i, r)
    assert dw.shadeHit(comp) == Color(0.38066, 0.47583, 0.2855)

    dw = World.defaultWorld()
    dw.lights[0] = Light(Tuple.point(0, 0.25, 0), Color(1, 1, 1))
    r = Ray(Tuple.point(0, 0, 0), Tuple.vector(0, 0, 1))
    s1 = dw.shapes[1]
    i = Intersection(0.5, s1)
    comp = Computation(i, r)

    assert dw.shadeHit(comp) == Color(0.90498, 0.90498, 0.90498)

    l = Light(Tuple.point(0, 0, -10), Color(1, 1, 1))
    s1 = Sphere()
    s2 = Sphere()
    s2.transform = Matrix.translation(0, 0, 10)
    r = Ray(Tuple.point(0, 0, 5), Tuple.vector(0, 0, 1))
    i = Intersection(4, s2)
    w = World([l], [s1, s2])
    c = Computation(i, r)
    assert w.shadeHit(c) == Color(0.1, 0.1, 0.1)

    w1 = World.defaultWorld()
    p = Plane()
    p.material = Material(reflective=0.5)
    p.transform = Matrix.translation(0, -1, 0)
    w1.shapes.append(p)
    r = Ray(Tuple.point(0, 0, -3), Tuple.vector(0, -2**0.5/2, 2**0.5/2))
    i = Intersection(2**0.5, p)
    comp = Computation(i, r)
    assert w1.shadeHit(comp) == Color(0.87677, 0.92436, 0.82918)

    w1 = World.defaultWorld()
    p = Plane()
    p.material = Material(transparency=0.5, refractiveIndex=1.5)
    p.transform = Matrix.translation(0, -1, 0)
    s = Sphere()
    s.material = Material(color=Color(1, 0, 0),
                          ambient=0.5)
    s.transform = Matrix.translation(0, -3.5, -0.5)
    w1.shapes.append(p)
    w1.shapes.append(s)
    r = Ray(Tuple.point(0, 0, -3), Tuple.vector(0, -2**0.5/2, 2**0.5/2))
    i = Intersection(2**0.5, p)
    comp = Computation(i, r, [i])
    assert w1.shadeHit(comp, 5) == Color(0.93642, 0.68642, 0.68642)

    w1 = World.defaultWorld()
    p = Plane()
    p.material = Material(
        transparency=0.5, refractiveIndex=1.5, reflective=0.5)
    p.transform = Matrix.translation(0, -1, 0)
    s = Sphere()
    s.material = Material(color=Color(1, 0, 0),
                          ambient=0.5)
    s.transform = Matrix.translation(0, -3.5, -0.5)
    w1.shapes.append(p)
    w1.shapes.append(s)
    r = Ray(Tuple.point(0, 0, -3), Tuple.vector(0, -2**0.5/2, 2**0.5/2))
    i = Intersection(2**0.5, p)
    comp = Computation(i, r, [i])
    assert w1.shadeHit(comp, 5) == Color(0.93391, 0.69643, 0.69243)


# ---------------------------------------------------


def test_colorAt():
    dw = World.defaultWorld()
    ray = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 1, 0))
    assert dw.colorAt(ray) == Color(0, 0, 0)

    ray = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
    assert dw.colorAt(ray) == Color(0.38066, 0.47583, 0.2855)

    dw.shapes[0].material.ambient = 1
    dw.shapes[1].material.ambient = 1
    ray = Ray(Tuple.point(0, 0, 0.75), Tuple.vector(0, 0, -1))
    assert dw.colorAt(ray) == dw.shapes[1].material.color

    w = World.defaultWorld()
    w.lights = [Light(Tuple.point(0, 0, 0), Color(1, 1, 1))]
    lower = Plane()
    lower.material = Material(reflective=1)
    lower.transform = Matrix.translation(0, -1, 0)
    upper = Plane()
    upper.material = Material(reflective=1)
    upper.transform = Matrix.translation(0, 1, 0)
    w.shapes.append(lower)
    w.shapes.append(upper)
    ray = Ray(Tuple.point(0, 0, 0), Tuple.vector(0, 1, 0))
    start = time.time()
    color = w.colorAt(ray)
    end = time.time()
    assert int(start-end) <= 10
# ---------------------------------------------------


def test_isShadowed():
    w = World.defaultWorld()
    l = w.lights[0]
    p = Tuple.point(0, 10, 0)
    assert not w.isShadowed(l, p)

    p = Tuple.point(10, -10, 10)
    assert w.isShadowed(l, p)

    p = Tuple.point(-20, 20, -20)
    assert not w.isShadowed(l, p)

# ---------------------------------------------------


def test_reflectedColor():
    w = World.defaultWorld()
    r = Ray(Tuple.point(0, 0, 0), Tuple.vector(0, 0, 1))
    s = w.shapes[1]
    s.material.ambient = 1
    i = Intersection(1, s)
    comp = Computation(i, r)
    assert w.reflectedColor(comp) == Color()

    w1 = World.defaultWorld()
    p = Plane()
    p.material = Material(reflective=0.5)
    p.transform = Matrix.translation(0, -1, 0)
    w1.shapes.append(p)
    r = Ray(Tuple.point(0, 0, -3), Tuple.vector(0, -2**0.5/2, 2**0.5/2))
    i = Intersection(2**0.5, p)
    comp = Computation(i, r)
    assert w1.reflectedColor(comp) == Color(0.19032, 0.2379, 0.14274)

    w1 = World.defaultWorld()
    p = Plane()
    p.material = Material(reflective=0.5)
    p.transform = Matrix.translation(0, -1, 0)
    w1.shapes.append(p)
    r = Ray(Tuple.point(0, 0, -3), Tuple.vector(0, -2**0.5/2, 2**0.5/2))
    i = Intersection(2**0.5, p)
    comp = Computation(i, r)
    assert w1.reflectedColor(comp, 0) == Color()

# ---------------------------------------------------


def test_refractedColor():
    w = World.defaultWorld()
    s = w.shapes[0]
    ray = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
    xs = [Intersection(4, s), Intersection(6, s)]
    comps = Computation(xs[0], ray, xs)
    assert w.refractedColor(comps, 5) == Color()

    s.material.transparency = 1
    s.material.refractiveIndex = 1.5
    xs = [Intersection(4, s), Intersection(6, s)]
    comps = Computation(xs[0], ray, xs)
    assert w.refractedColor(comps, 0) == Color()

    s.material.transparency = 1
    s.material.refractiveIndex = 1.5
    ray2 = Ray(Tuple.point(0, 0, 2**0.5/2), Tuple.vector(0, 1, 0))
    xs = [Intersection(-2**0.5/2, s), Intersection(2**0.5/2, s)]
    comps = Computation(xs[1], ray2, xs)
    assert w.refractedColor(comps, 0) == Color()

    s.material.ambient = 1
    s.material.transparency = 0
    s.material.refractiveIndex = 1
    s.material.pattern = Pattern(Color(), Color(1, 1, 1), patternType="")
    s2 = w.shapes[1]
    s2.material.transparency = 1
    s2.material.refractiveIndex = 1.5
    ray2 = Ray(Tuple.point(0, 0, 0.1), Tuple.vector(0, 1, 0))
    xs = [Intersection(-0.9899, s), Intersection(-0.4899, s2),
          Intersection(0.4899, s2), Intersection(0.9899, s)]
    comps = Computation(xs[2], ray2, xs)
    assert w.refractedColor(comps, 5) == Color(0, 0.9988, 0.04725)
