import math
import numpy as np
from Backend.src.Matrix import Matrix
from Backend.src.Tuple import Tuple
# ---------------------------------------------------


def test_mul():
    A = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 8, 7, 6],
        [5, 4, 3, 2]
    ])

    A = Matrix(matrix=A)

    B = np.array([
        [-2, 1, 2, 3],
        [3, 2, 1, -1],
        [4, 3, 6, 5],
        [1, 2, 7, 8]
    ])
    B = Matrix(matrix=B)
    ans = np.array([
        [20, 22, 50, 48],
        [44, 54, 114, 108],
        [40, 58, 110, 102],
        [16, 26, 46, 42]
    ])
    ans = Matrix(matrix=ans)
    assert A*B == ans

    A = np.array([
        [1, 2, 3, 4],
        [2, 4, 4, 2],
        [8, 6, 4, 1],
        [0, 0, 0, 1]
    ])

    A = Matrix(matrix=A)
    b = Tuple.point(1, 2, 3)
    assert A*Tuple.point(1, 2, 3) == Tuple(18, 24, 33, 1)

# ---------------------------------------------------


def test_identity():
    A = np.array([
        [0, 1, 2, 4],
        [1, 2, 4, 8],
        [2, 4, 8, 16],
        [4, 8, 16, 32]
    ])

    A = Matrix(matrix=A)

    assert A.identity() * A == A

    b = Tuple(1, 2, 3, 4)
    assert A.identity() * b == b

# ---------------------------------------------------


def test_transpose():
    A = np.array([
        [0, 9, 3, 0],
        [9, 8, 0, 8],
        [1, 8, 5, 3],
        [0, 0, 5, 8]
    ])

    A = Matrix(matrix=A)

    assert A.identity() == A.identity().transpose()

    ans = np.array([
        [0, 9, 1, 0],
        [9, 8, 8, 0],
        [3, 0, 5, 5],
        [0, 8, 3, 8]
    ])

    ans = Matrix(matrix=ans)
    assert A.transpose() == ans

# ---------------------------------------------------


def test_deter():
    A = np.array([
        [6, 4, 4, 4],
        [5, 5, 7, 6],
        [4, -9, 3, -7],
        [9, 1, 7, -6]
    ])

    A = Matrix(matrix=A)
    assert A.determinant()+2120 < 0.0001

    A = np.array([
        [-4, 2, -2, -3],
        [9, 6, 2, 6],
        [0, -5, 1, -5],
        [0, 0, 0, 0]
    ])

    A = Matrix(matrix=A)

    assert A.determinant() < 0.0001

# ---------------------------------------------------


def test_inverse():
    A = np.array([
        [-5, 2, 6, -8],
        [1, -5, 1, 8],
        [7, 7, -6, -7],
        [1, -3, 7, 4]
    ])

    A = Matrix(matrix=A)

    ans = np.array([
        [0.21805, 0.45113, 0.24060, -0.04511],
        [-0.80827, -1.45677, -0.44361, 0.52068],
        [-0.07895, -0.22368, -0.05263, 0.19737],
        [-0.52256, -0.81391, -0.30075, 0.30639]
    ])

    ans = Matrix(matrix=ans)

    assert A.determinant()-532 < 0.0001
    assert ~A == ans

    A = np.array([
        [-5, 2, 6, -8],
        [1, -5, 1, 8],
        [7, 7, -6, -7],
        [1, -3, 7, 4]
    ])

    A = Matrix(matrix=A)

    B = np.array([
        [6, 4, 4, 4],
        [5, 5, 7, 6],
        [4, -9, 3, -7],
        [9, 1, 7, -6]
    ])

    B = Matrix(matrix=B)
    assert A*B*~B == A

# ---------------------------------------------------


def test_translation():
    t1 = Matrix.translation(5, -3, 2)
    p = Tuple.point(-3, 4, 5)
    assert t1*p == Tuple.point(2, 1, 7)
    # inverse means working on the opposite direction
    assert ~t1 * p == Tuple.point(-8, 7, 3)
    assert t1 * Tuple.vector(-3, 4, 5) == Tuple.vector(-3, 4, 5)

# ---------------------------------------------------


def test_scaling():
    t1 = Matrix.scaling(2, 3, 4)
    p = Tuple.point(-4, 6, 8)
    assert t1*p == Tuple.point(-8, 18, 32)
    # inverse means working on the opposite direction
    v = Tuple.vector(-4, 6, 8)
    assert t1 * v == Tuple.vector(-8, 18, 32)
    assert ~t1 * v == Tuple.vector(-2, 2, 2)
    t1 = Matrix.scaling(-1, 1, 1)
    p = Tuple.point(2, 3, 4)
    assert t1 * p == Tuple.point(-2, 3, 4)

# ---------------------------------------------------


def test_rotateX():
    p = Tuple.point(0, 1, 0)
    hq = Matrix.rotateX(math.pi/4)
    fq = Matrix.rotateX(math.pi/2)
    assert hq*p == Tuple.point(0, 2**0.5/2, 2**0.5/2)
    assert fq * p == Tuple.point(0, 0, 1)
    assert ~hq*p == Tuple.point(0, 2**0.5/2, -2**0.5/2)

# ---------------------------------------------------


def test_rotateY():
    p = Tuple.point(0, 0, 1)
    hq = Matrix.rotateY(math.pi/4)
    fq = Matrix.rotateY(math.pi/2)
    assert hq*p == Tuple.point(2**0.5/2, 0, 2**0.5/2)
    assert fq * p == Tuple.point(1, 0, 0)

# ---------------------------------------------------


def test_rotateZ():
    p = Tuple.point(0, 1, 0)
    hq = Matrix.rotateZ(math.pi/4)
    fq = Matrix.rotateZ(math.pi/2)
    assert hq*p == Tuple.point(-2**0.5/2, 2**0.5/2, 0)
    assert fq * p == Tuple.point(-1, 0, 0)

# ---------------------------------------------------


def test_shearing():
    p = Tuple.point(2, 3, 4)
    s0 = Matrix.shearing(1, 0, 0, 0, 0, 0)
    s1 = Matrix.shearing(0, 1, 0, 0, 0, 0)
    s2 = Matrix.shearing(0, 0, 1, 0, 0, 0)
    s3 = Matrix.shearing(0, 0, 0, 1, 0, 0)
    s4 = Matrix.shearing(0, 0, 0, 0, 1, 0)
    s5 = Matrix.shearing(0, 0, 0, 0, 0, 1)

    assert s0*p == Tuple.point(5, 3, 4)
    assert s1*p == Tuple.point(6, 3, 4)
    assert s2*p == Tuple.point(2, 5, 4)
    assert s3*p == Tuple.point(2, 7, 4)
    assert s4*p == Tuple.point(2, 3, 6)
    assert s5*p == Tuple.point(2, 3, 7)

# ---------------------------------------------------


def test_chaining():
    p = Tuple.point(1, 0, 1)
    A = Matrix.rotateX(math.pi/2)
    B = Matrix.scaling(5, 5, 5)
    C = Matrix.translation(10, 5, 7)
    assert (C*B*A)*p == Tuple.point(15, 0, 7)


# ---------------------------------------------------


def test_viewTransformation():
    f = Tuple.point(0, 0, 0)
    t = Tuple.point(0, 0, -1)
    u = Tuple.vector(0, 1, 0)
    assert Matrix.viewTransformation(f, t, u) == Matrix(matrix=np.eye(4))

    f = Tuple.point(0, 0, 0)
    t = Tuple.point(0, 0, 1)
    u = Tuple.vector(0, 1, 0)
    assert Matrix.viewTransformation(f, t, u) == Matrix.scaling(-1, 1, -1)

    f = Tuple.point(0, 0, 8)
    t = Tuple.point(0, 0, 0)
    u = Tuple.vector(0, 1, 0)
    assert Matrix.viewTransformation(f, t, u) == Matrix.translation(0, 0, -8)

    f = Tuple.point(1, 3, 2)
    t = Tuple.point(4, -2, 8)
    u = Tuple.vector(1, 1, 0)
    m = np.array(
        [[-0.50709, 0.50709, 0.67612, -2.36643],
        [0.76772, 0.60609, 0.12122, -2.82843],
        [-0.35857, 0.59761, -0.71714, 0],
        [0, 0, 0, 1]]
    )
    assert Matrix.viewTransformation(f, t, u) == Matrix(matrix = m)
