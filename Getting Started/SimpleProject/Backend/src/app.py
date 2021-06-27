from Color import Color
from Tuple import Tuple
from Canvas import Canvas
from Matrix import Matrix
from Group import Group
from Sphere import Sphere
import methods as m

from PIL import Image
import numpy as np

# w, h = 3, 3
# data = np.zeros((h, w, 3), dtype=np.uint8)
# # red patch in upper left
# data[0:3, 0:3] = np.array([255, 0, 0])
# data = np.array([[[127.343, 0, 0],
#                   [127.343, 0, 0],
#                   [127.343, 0, 0]],

#                  [[127.343, 0, 0],
#                   [127.343, 0, 0],
#                   [127.343, 0, 0]],

#                  [[127.343, 0, 0],
#                   [127.343, 0, 0],
#                   [127.343, 0, 0]]], dtype=np.uint8)

# img = Image.fromarray(data, 'RGB')
# img.save("my.png")

# print(Matrix(2,2))
# print(Matrix())
# print(Color())
# print(Tuple())

# m.image1()
m.image3()


def test1Image():
    c = Canvas(5, 3)
    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0, 1)
    c.writePixel(0, 0, c1)
    c.writePixel(2, 1, c2)
    c.writePixel(4, 2, c3)
    c.saveImage("test1")
