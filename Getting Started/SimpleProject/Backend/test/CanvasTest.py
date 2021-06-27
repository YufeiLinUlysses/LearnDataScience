import numpy as np
from Backend.src.Canvas import Canvas
from Backend.src.Color import Color

# ---------------------------------------------------


def test_writePixel():
    c1 = Canvas(10, 20)
    red = Color(1, 0, 0)
    c1.writePixel(2, 3, red)
    assert c1.pixelAt(2, 3) == red

# ---------------------------------------------------


def test_canvasToPPM():
    c = Canvas(5, 3)
    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0, 1)
    c.writePixel(0, 0, c1)
    c.writePixel(2, 1, c2)
    c.writePixel(4, 2, c3)
    result = c.canvasToPPM()
    result = "\n".join(result.split("\n")[3:])
    ans = "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 255\n"
    assert result == ans
    c = Canvas(10, 2)
    for i in range(c.height):
        for j in range(c.width):
            c.writePixel(j, i, Color(1, 0.8, 0.6))
    result = c.canvasToPPM()
    result = "\n".join(result.split("\n")[3:])
    ans = "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n153 255 204 153 255 204 153 255 204 153 255 204 153\n255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n153 255 204 153 255 204 153 255 204 153 255 204 153\n"
    assert result == ans

# ---------------------------------------------------


def test_canvasToPNG():
    c = Canvas(5, 3)
    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0, 1)
    c.writePixel(0, 0, c1)
    c.writePixel(2, 1, c2)
    c.writePixel(4, 2, c3)
    result = c.canvasToPNG()
    ans = np.array([[[255, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]],

                    [[0, 0, 0],
                     [0, 0, 0],
                     [0, 128, 0],
                     [0, 0, 0],
                     [0, 0, 0]],

                    [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 255]]], dtype=np.uint8)
    assert np.allclose(result, ans)
