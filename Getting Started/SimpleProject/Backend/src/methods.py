import math
from Color import Color
from Tuple import Tuple
from Canvas import Canvas
from Matrix import Matrix
from Ray import Ray
from Sphere import Sphere
from Plane import Plane
from Intersection import Intersection
from Material import Material
from Light import Light
from World import World
from Camera import Camera
from Pattern import Pattern
from Cube import Cube
from Group import Group
from Cylinder import Cylinder
from Cone import Cone


def image1():
    o = Tuple.point(0, 0, -5)
    wallZ = 10
    wallSize = 7
    canvasPixel = 100
    pixSize = wallSize/canvasPixel
    half = wallSize/2
    canv = Canvas(canvasPixel, canvasPixel)
    color = Color(1, 0, 0)
    s = Sphere()
    s.transform = Matrix.shearing(1, 0, 0, 0, 0, 0) * Matrix.scaling(0.5, 1, 1)
    for y in range(canvasPixel):
        wy = half-pixSize*y
        for x in range(canvasPixel):
            wx = pixSize*x-half
            position = Tuple.point(wx, wy, wallZ)
            r = Ray(o, (position-o).normalize())
            count, xs = s.intersect(r)
            if Intersection.hit(xs) != Intersection():
                canv.writePixel(x, y, color)
    canv.saveImage("image1")


def image2():
    o = Tuple.point(0, 0, -5)
    wallZ = 10
    wallSize = 7
    canvasPixel = 100
    pixSize = wallSize/canvasPixel
    half = wallSize/2
    canv = Canvas(canvasPixel, canvasPixel)

    # sphere
    s = Sphere()
    s.material.color = Color(1, 0.2, 1)
    s.transform = Matrix.shearing(1, 0, 0, 0, 0, 0) * Matrix.scaling(0.5, 1, 1)

    # light
    light = Light(Tuple.point(-10, 10, -10), Color(1, 1, 1))

    for y in range(canvasPixel):
        wy = half-pixSize*y
        for x in range(canvasPixel):
            wx = pixSize*x-half
            position = Tuple.point(wx, wy, wallZ)
            r = Ray(o, (position-o).normalize())
            count, xs = s.intersect(r)
            h = Intersection.hit(xs)
            if h != Intersection():
                p = r.position(h.t)
                normal = h.shape.normalAt(p)
                eye = ~r.direction
                color = h.shape.material.lighting(light, p, eye, normal)
                canv.writePixel(x, y, color)
    canv.saveImage("image2")


def image3():
    floor = Plane()
    floor.transform = Matrix.scaling(10, 0.01, 10)
    floor.material = Material(color=Color(1, 0.9, 0.9), specular=0)

    leftWall = Plane()
    leftWall.transform = Matrix.translation(
        0, 0, 5) * Matrix.rotateY(-math.pi/4) * Matrix.rotateX(math.pi/2)*Matrix.scaling(10, 0.01, 10)
    leftWall.material = Material(color=Color(1, 0.9, 0.9), specular=0)

    rightWall = Plane()
    rightWall.transform = Matrix.translation(
        0, 0, 5) * Matrix.rotateY(math.pi/4) * Matrix.rotateX(math.pi/2)*Matrix.scaling(10, 0.01, 10)
    rightWall.material = Material(color=Color(1, 0.9, 0.9), specular=0)

    mid = Sphere()
    # print(mid.material.pattern)
    mid.transform = Matrix.translation(-0.5, 1, 0.5)
    mid.material = Material(color=Color(0.1, 1, 0.5),
                            specular=0.3, diffuse=0.7)

    right = Cube()
    # print("Change Pattern")
    # print(right.pattern)
    right.transform = Matrix.translation(
        1.5, 0.5, -0.5)*Matrix.scaling(0.5, 0.5, 0.5)
    right.material = Material(color=Color(
        0.5, 1, 0.1), specular=0.3, diffuse=0.7)
    right.material.pattern = Pattern(
        Color(0, 0, 0), Color(1, 1, 1), patternType="gradient")

    left = Sphere()
    left.transform = Matrix.translation(
        -1.5, 0.33, -0.75)*Matrix.scaling(0.33, 0.33, 0.33)
    left.material = Material(color=Color(1, 0.8, 0.1),
                             specular=0.3, diffuse=0.7)

    shapes = [floor, leftWall, rightWall, mid, right, left]
    lights = [Light(Tuple.point(-10, 10, -10), Color(1, 1, 1))]

    w = World(lights, shapes)

    c = Camera(100, 50, math.pi/3)
    c.transform = Matrix.viewTransformation(
        Tuple.point(0, 1.5, -5),
        Tuple.point(0, 1, 0),
        Tuple.vector(0, 1, 0)
    )

    image = c.render(w)
    image.saveImage("image4")


def image4():
    # corner of a hexagon
    def hexCorner():
        c = Sphere()
        c.transform = Matrix.translation(
            0, 0, -1) * Matrix.scaling(0.25, 0.25, 0.25)
        return c

    # edge of a hexagon
    def hexEdge():
        e = Cylinder(0, 1)
        e.transform = Matrix.translation(
            0, 0, -1) * Matrix.rotateY(-math.pi/6) * Matrix.rotateZ(-math.pi/2) * Matrix.scaling(0.25, 1, 0.25)
        return e

    # side of a hexagon
    def hexSide():
        s = Group([hexCorner(), hexEdge()])
        return s

    hexagon = Group()
    for i in range(6):
        s = hexSide()
        s.transform = Matrix.rotateY(i*math.pi/3)
        hexagon.addChild(s)

    shapes = [hexagon]
    lights = [Light(Tuple.point(-10, 10, -10), Color(1, 1, 1))]

    w = World(lights, shapes)

    c = Camera(100, 50, math.pi/3)
    c.transform = Matrix.viewTransformation(
        Tuple.point(0, 1.5, -5),
        Tuple.point(0, 1, 0),
        Tuple.vector(0, 1, 0)
    )

    image = c.render(w)
    image.saveImage("image5")
