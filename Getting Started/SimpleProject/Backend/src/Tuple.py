import numpy as np

""" 
Tuple class describes the tuple we use to build a 3D renderer
Each tuple contain 4 elements: x,y,z,w in a numpy array
x: x-coordinate, y: y-coordinate, z: z-coordinate
w = 0 indicate a vector, w = 1 indicate a point
"""

class Tuple():
    # Tuple class takes in a numpy array
    # arr[0] is x, arr[1] is y, arr[2] is z, arr[3] is w
    def __init__(self,arr):
        self.arr = arr
    def __add___(self, tuple2):
        return Tuple(self.arr + tuple2.arr)