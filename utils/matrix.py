from constants import *
from utils.vector import toVector3
from math import cos, sin

def matrix_multiplication(a, b):
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len(b[0])
    rows_b = len(b)

    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
    if columns_a == rows_b:
        for x in range(rows_a):
            for y in range(columns_b):
                sum = 0
                for k in range(columns_a):
                    sum += a[x][k] * b[k][y]
                result_matrix[x][y] = sum
        return result_matrix

    else:
        print("columns of the first matrix must be equal to the rows of the second matrix")
        return None

def multiplyMatrixVector(vec, mat):
    m = matrix_multiplication(vec.toMatrix(), mat)
    v = toVector3(m)
    if m[0][3] != 0.0:
        v.x /= m[0][3]
        v.y /= m[0][3]
        v.z /= m[0][3]
    return v

def ProjectionMatrix(camera):
    return [ [aspect * camera.tangent, 0, 0, 0],
             [0, camera.tangent, 0, 0 ],
             [ 0, 0, camera.far/(camera.far - camera.near), 1],
             [ 0, 0, (-camera.far * camera.near) / (camera.far - camera.near), 0]
             ]

def RotationX(angle):
    return [[1, 0, 0, 0],
            [0, cos(angle), sin(angle), 0],
            [0,-sin(angle), cos(angle), 0],
            [0, 0, 0, 1]]

def RotationY(angle):
    return [[cos(angle), 0, -sin(angle), 0],
            [0, 1, 0, 0],
            [sin(angle), 0, cos(angle),0],
            [0, 0, 0, 1]]

def RotationZ(angle):
    return [[cos(angle), sin(angle), 0, 0],
            [-sin(angle), cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]

def ScalingMatrix(scale):
    return [[scale, 0, 0, 0],
            [0, scale, 0, 0],
            [0, 0, scale, 0],
            [0, 0, 0, 1]]

def identity():
    return [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]

def translateMatrix(pos):
    return [[1, 0, 0, pos.x],
            [0, 1, 0, pos.y],
            [0, 0, 1, pos.z],
            [0, 0, 0, 1]]
