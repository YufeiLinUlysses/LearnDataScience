import re
from Tuple import Tuple
from Group import Group
from Triangle import Triangle
# ---------------------
""" 
ObjParser class helps to parse .obj files into images and render them with triangles or smooth triangles.

It contains the following variable:
1. vertices: a list, a collection of different vertices.
2. normals: a list, a collection of different normals
3. textures: a list, a collection of different textures
4. defaultGroup: a Group, the shape that contains all triangles

Intersection class contains the following functions:
__init__
__eq__
hit
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/ObjParserTest.py
    --- OR ---- 
    python3 -m nose -v ../test/ObjParserTest.py
    --- OR ---- 
    python -m nose -v ../test/ObjParserTest.py
    ---------------------------------------------------
"""


class ObjParser():
    # ---------------------
    """
    ObjParser class takes in no input

    """
    # ---------------------

    def __init__(self):
        self.vertices = []
        self.normals = []
        self.textures = []
        self.defaultGroup = Group()
        self.cur = self.defaultGroup
        self.subGroups = {}
    # ---------------------
    """
    Define equivalence of two ObjParser instances
    """
    # ---------------------

    def __eq__(self, p2: "ObjParser"):
        if len(self.vertices) != len(p2.vertices):
            return False
        for i in range(len(self.vertices)):
            if self.vertices[i] != p2.vertices[i]:
                return False
        if len(self.normals) != len(p2.normals):
            return False
        for i in range(len(self.normals)):
            if self.normals[i] != p2.normals[i]:
                return False
        if len(self.textures) != len(p2.textures):
            return False
        for i in range(len(self.textures)):
            if self.textures[i] != p2.textures[i]:
                return False
        return self.defaultGroup == p2.defaultGroup

    # ---------------------
    """
    parse reads in the obj file and holds everything in a group.
    ---- Inputs: --------
        * path: a string, the path of the obj file
    ---- Outputs: --------
        no output, all conversion will happen within the instance
    """
    # ---------------------

    def parse(self, path: str):
        f = open(path, "r")
        lines = f.readlines()
        for l in lines:
            self.convertLine(l)
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/ObjParserTest.py:test_parse
        --- OR ---- 
        python3 -m nose -v ../test/ObjParserTest.py:test_parse
        --- OR ---- 
        python -m nose -v ../test/ObjParserTest.py:test_parse
        ---------------------------------------------------
    """

    # ---------------------
    """
    convertLine tests whether a line is qualified and converts it into the formats we want.
    ---- Inputs: --------
        * line: a string
    ---- Outputs: --------
        no output, all conversion will happen within the instance
    """
    # ---------------------

    def convertLine(self, line: str):
        # Here we use compile regex to help match the pattern of the phrases we want
        # v is vector
        # vt tecture, used in smooth triangle
        # vn normal
        rv = re.compile("(v|vn|vt) ([-+]?[0-9]+[\.]?[0-9]* ?){3}")
        # f 1 2 3
        rf1 = re.compile("f (\d+ ?){3,}")
        # the two following type of fs are for smooth triangle
        # f v1//vn1 1//2 1//3 1//4
        rf2 = re.compile("f (\d+\/\/\d+ ?){3,}")
        # f v1/vt1/vn1 1/2/3 1/3/4 1/4/5
        rf3 = re.compile("f (\d+\/\d+\/\d+ ?){3,}")
        rg = re.compile("g \w+")

        if rv.match(line):
            line = line.split(" ")
            if line[0] == "v":
                self.vertices.append(Tuple.point(
                    float(line[1]), float(line[2]), float(line[3])))
            elif line[0] == "vn":
                self.normals.append(Tuple.vector(
                    float(line[1]), float(line[2]), float(line[3])))
            elif line[0] == "vt":
                self.textures.append(Tuple.vector(
                    float(line[1]), float(line[2]), float(line[3])))
        elif rf1.match(line):
            line = line.split(" ")
            head = int(line[1])-1
            line = line[1:]
            for i in range(1, len(line)-1):
                t = Triangle(self.vertices[head],
                             self.vertices[int(line[i])-1],
                             self.vertices[int(line[i+1])-1])
                self.cur.addChild(t)
        elif rg.match(line):
            line = line.split(" ")
            groupName = line[1][:-1]
            self.subGroups[groupName] = Group()
            self.defaultGroup.addChild(self.subGroups[groupName])
            self.cur = self.subGroups[groupName]
        # ignore for now, this is for smooth triangle
        elif rf2.match(line):
            line = line.split(" ")
            line = line[1:]
            vert = []
            norm = []
            for l in line:
                l = l.split("//")
                vert.append(int(l[0])-1)
                norm.append(int(l[1])-1)
            for i in range(1, len(vert)-1):
                t = Triangle(self.vertices[int(vert[0])],
                             self.vertices[int(vert[i])],
                             self.vertices[int(vert[i+1])],
                             self.normals[int(norm[0])],
                             self.normals[int(norm[i])],
                             self.normals[int(norm[i+1])])
                self.cur.addChild(t)
        elif rf3.match(line):
            line = line.split(" ")
            line = line[1:]
            vert = []
            norm = []
            for l in line:
                l = l.split("/")
                vert.append(int(l[0])-1)
                norm.append(int(l[2])-1)
            for i in range(1, len(vert)-1):
                t = Triangle(self.vertices[int(vert[0])],
                             self.vertices[int(vert[i])],
                             self.vertices[int(vert[i+1])],
                             self.normals[int(norm[0])],
                             self.normals[int(norm[i])],
                             self.normals[int(norm[i+1])])
                self.cur.addChild(t)

    # -----------------
    """  
        Make sure you are on ~/src
        this is tested within the parser function
    """
