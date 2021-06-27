import numpy as np
from Tuple import Tuple
from Color import Color
from Light import Light
from Pattern import Pattern
from Matrix import Matrix

# ---------------------
""" 
Material class describes the material of a shape based on the Phong Reflection Model
Each material contains 5 elements:
1. color: a Color, the color of the material
2. ambient: a float, describe the ambient color of the material
3. diffuse: a float, describe the diffuse color of the material
4. specular: a float, describe the specular color of the material
5. shininess: a float, describe the shineness of the material
6. pattern: a Pattern, describe the pattern of the material
7. reflective: a float, indicates the reflectivity of the material

Material class contains the following functions:
__init__
__str__
__eq__
lighting
"""
# ---------------------
"""  
    Make sure you are on ~/src
    ---------------------------------------------------
    nosetests -v ../test/MaterialTest.py
    --- OR ---- 
    python3 -m nose -v ../test/MaterialTest.py
    --- OR ---- 
    python -m nose -v ../test/MaterialTest.py
    ---------------------------------------------------
"""


class Material():

    # ---------------------
    """
    Material takes in nine parameters
    """
    # ---------------------

    def __init__(self, color: "Color" = Color(1, 1, 1), ambient: float = 0.1, diffuse: float = 0.9, specular: float = 0.9, shininess: float = 200, pattern: "Pattern" = None, reflective: float = 0, transparency: float = 0, refractiveIndex: float = 1):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess
        self.pattern = pattern
        self.reflective = reflective
        self.transparency = transparency
        self.refractiveIndex = refractiveIndex

    # ---------------------
    """
    Define the output format for Material class
    """
    # ---------------------

    def __str__(self):
        return "Color: " + str(self.color) + "\nAmbient: " + str(self.ambient) + "\nDiffuse: " + str(self.diffuse) + "\nSpecular: " + str(self.specular) + "\nShininess: " + str(self.shininess)+"\nPattern: \n"+str(self.pattern)+"\nReflective: "+str(self.reflective)+"\nTransparency: "+str(self.transparency)+"\nRefractive Index: "+str(self.refractiveIndex)

    # ---------------------
    """
    Define equivalence of two Material instances
    """
    # ---------------------

    def __eq__(self, material2: "Light"):
        return self.color == material2.color and self.ambient == material2.ambient and self.diffuse == material2.diffuse and self.specular == material2.specular and self.shininess == material2.shininess and self.pattern == material2.pattern

    # ---------------------
    """
    Get the final color when the shape is shined by a light
    ---- Inputs: --------
        * light: a Light
        * point: a Tuple, the place where we are looking at for the light and shape intersection
        * eyev: a Tuple, the position of our eye
        * normalv: a Tuple, the normal vector
        * inShadow: a bool, indicate whether there is a shadow
        * transform: a Matrix, the transform matrix of the shape, used for calculating pattern
    ---- Outputs: --------
        * count: a scalar, the number of intersections
        * results: a tuple, all intersections are listed
    """
    # ---------------------

    def lighting(self, light: "Light", point: "Tuple", eyev: "Tuple", normalv: "Tuple", inShadow: bool = False, transform: "Matrix" = Matrix(matrix=np.eye(4))):
        if self.pattern is not None:
            self.color = self.pattern.patternAtObject(point, transform)
        effectiveColor = self.color * light.intensity
        lightV = (light.position-point).normalize()
        ambient = effectiveColor * self.ambient
        if inShadow:
            return ambient
        lightDotNormal = lightV.dot(normalv)
        # calculate diffuse and specular
        if lightDotNormal < 0:
            diffuse = Color(0, 0, 0)
            specular = Color(0, 0, 0)
        else:
            diffuse = effectiveColor * self.diffuse * lightDotNormal
            reflect = ~lightV.reflectV(normalv)
            reflectDotEye = reflect.dot(eyev)
            if reflectDotEye == 0:
                specular = Color(0, 0, 0)
            else:
                factor = reflectDotEye**self.shininess
                specular = light.intensity * self.specular * factor
        return ambient + diffuse + specular
    # -----------------
    """  
        Make sure you are on ~/src
        ---------------------------------------------------
        nosetests -v ../test/MaterialTest.py:test_lighting
        --- OR ---- 
        python3 -m nose -v ../test/MaterialTest.py:test_lighting
        --- OR ---- 
        python -m nose -v ../test/MaterialTest.py:test_lighting
        ---------------------------------------------------
    """
