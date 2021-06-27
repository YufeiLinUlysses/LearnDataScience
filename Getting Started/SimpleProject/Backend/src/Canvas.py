import os
import numpy as np
from PIL import Image
from Color import Color
# ---------------------
""" 
Canvas class helps to describe a set of pixel in grids that help generate images.
Each canvas contains 2 elements: weight ,height
width, height are all float value
width: defining the number of columns, height: defining the number of rows

Canvas class contains the following functions:
__init__
__eq__
pixelAt
writePixel
canvasToPPM
canvasToPNG
saveImage
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/CanvasTest.py
    --- OR ---- 
    python3 -m nose -v ../test/CanvasTest.py
    --- OR ---- 
    python -m nose -v ../test/CanvasTest.py
    ---------------------------------------------------
"""


class Canvas():
    # ---------------------
    """
    Canvas class takes in two numbers
    w is width, h is height
    """
    # ---------------------

    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h
        self.canv = [[Color() for _ in range(w)] for _ in range(h)]

    # ---------------------
    """
    Define equivalence of two Canvas instances
    """
    # ---------------------

    def __eq__(self, canvas2: "Canvas"):
        if self.width == canvas2.width and self.height == canvas2.height:
            for i in range(self.height):
                for j in range(self.width):
                    if self.canv[i][j] != canvas2.canv[i][j]:
                        return False
            return True
        return False

    # ---------------------
    """
    Get the color of a given pixel
    ---- Inputs: --------
        * cl: A float indicating the column number of where the pixel is at
        * rw: A float indicating the row number of where the pixel is at
    ---- Outputs: --------
        * Color: the color at the pixel
    
    """
    # ---------------------

    def pixelAt(self, cl: int, rw: int):
        return self.canv[rw][cl]

    # ---------------------
    """
    Change the color of a given pixel
    ---- Inputs: --------
        * cl: A float indicating the column number of where the pixel is at
        * rw: A float indicating the row number of where the pixel is at
        * color: A Color wanted to be at the pixel
    
    """
    # ---------------------

    def writePixel(self, cl: int, rw: int, color: "Color"):
        self.canv[rw][cl] = color
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/CanvasTest.py:test_writePixel
        --- OR ---- 
        python3 -m nose -v ../test/CanvasTest.py:test_writePixel
        --- OR ---- 
        python -m nose -v ../test/CanvasTest.py:test_writePixel
        ---------------------------------------------------
    """

    # ---------------------
    """
    Convert the canvas to ppm formatted images
    Generally existing PPM softwares accept a line more than 70 characters, 
    but there are some needs to have each line having less than or equal to 70 characters
    We also need a new line at the end of the string
    ---- Outputs: --------
        * result: A string containing the final ppm file
    """
    # ---------------------

    def canvasToPPM(self):
        result = "P3\n"+str(self.width) + " " + str(self.height) + "\n255\n"
        for row in self.canv:
            temp = ""
            for pix in row:
                # providing a conversion from 0 to 1 to 255 scale
                # if greater than 1, we read it as 1
                # if smaller than 0, we read it as 0
                def setColor(color):
                    if color >= 1:
                        return 255
                    elif color <= 0:
                        return 0
                    else:
                        return int(round(color * 255, 0))
                red = str(setColor(pix.r))
                green = str(setColor(pix.g))
                blue = str(setColor(pix.b))
                # for each color, if the existing line adding 1 to 3 characters
                # we cut it off and strip the last space and add a new line
                # so that we fulfill the 70 character requirment and do not cut off a color
                if len(temp) + len(red) > 70:
                    result += temp[:-1] + "\n"
                    temp = ""
                temp += red + " "
                if len(temp) + len(green) > 70:
                    result += temp[:-1] + "\n"
                    temp = ""
                temp += green + " "
                if len(temp) + len(blue) > 70:
                    result += temp[:-1] + "\n"
                    temp = ""
                temp += blue + " "
            temp = temp[:-1] + "\n"
            result += temp
        return result
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/CanvasTest.py:test_canvasToPPM
        --- OR ---- 
        python3 -m nose -v ../test/CanvasTest.py:test_canvasToPPM
        --- OR ---- 
        python -m nose -v ../test/CanvasTest.py:test_canvasToPPM
        ---------------------------------------------------
    """

    # ---------------------
    """
    Convert the canvas to a numpy array in order to call PIL.image to convert it to png image
    ---- Outputs: --------
        * result: A numpy array of size (h,w,3)
    """
    # ---------------------

    def canvasToPNG(self):
        result = []
        for rw in range(self.height):
            row = []
            for cl in range(self.width):
                cur = np.rint(self.pixelAt(cl, rw).arr*255)
                if cur[0] > 255:
                    cur[0] = 255
                elif cur[0] < 0:
                    cur[0] = 0
                if cur[1] > 255:
                    cur[1] = 255
                elif cur[1] < 0:
                    cur[1] = 0
                if cur[2] > 255:
                    cur[2] = 255
                elif cur[2] < 0:
                    cur[2] = 0
                row.append(cur)
            result.append(row)
        result = np.array(result)
        result = result.astype(np.uint8)
        return result
    # -----------------
    """
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/CanvasTest.py:test_canvasToPNG
        --- OR ---- 
        python3 -m nose -v ../test/CanvasTest.py:test_canvasToPNG
        --- OR ---- 
        python -m nose -v ../test/CanvasTest.py:test_canvasToPNG
        ---------------------------------------------------
    """

    # ---------------------
    """
    Save the result string from canvasToPPM to ppm file
    ---- Inputs: --------
        * filename: A string indicating the file name you want for the image
        * directory: default is the images folder, or a specefic one of your choice    
    """
    # ---------------------

    def saveImage(self, filename: str, directory: str = "../images/", fileType="png"):
        if not os.path.isdir(directory):
            os.mkdir(directory)
        path = directory + filename + "." + fileType
        if fileType == "ppm":
            result = self.canvasToPPM()
            f = open(path, "w")
            f.write(result)
            f.close()
        else:
            result = self.canvasToPNG()
            img = Image.fromarray(result, 'RGB')
            img.save(path)
        print(
            filename + " written successfully, please take a look at folder " + directory)

    # -----------------
    """
        Go to your chosen folder to see whether the image is what you want!
    """
