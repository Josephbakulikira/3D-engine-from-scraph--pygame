from constants import *
from utils.vector import *
from math import cos, sin
from copy import deepcopy

class Matrix:
    def __init__(self, r=4, c=4):
        self.row = r
        self.col = c
        self.val = [[0 for i in range(self.col)] for j in range(self.row)]

    def updateInfo(self):
        self.row = len(self.val)
        self.col = len(self.val[0])

    def transpose(self):
        temp = [[0 for i in range(self.col)] for j in range(self.row)]
        for x in range(self.row):
            for y in range(self.col):
                temp[x][y] = self.val[y][x]
        self.val = temp

    def __repr__(self):
        ## DEBUG
        return f'matrix->{self.val}'


def multiplyMatrix(m1, m2):
    m = Matrix(m1.row, m2.col)

    if m1.col != m2.row:
        print("we can't this two matricies")
        return None

    for x in range(m1.row):
        for y in range(m2.col):
            sum = 0
            for z in range(m1.col):
                sum += m1.val[x][z] * m2.val[z][y]
            m.val[x][y] = round(sum, 5)

    return m

def multiplyMatrixVector(vec, mat):
    temp = Matrix(1, 4)
    temp.val = vec.toMatrix()
    m = multiplyMatrix(temp, mat)
    v = toVector3(m)
    if m.val[0][3] != 0:
        v = v / m.val[0][3]
    return v

def TransposeMatrix(m):
    m1 = Matrix(m.row, m.col)
    for x in range(m.row):
        for y in range(m.col):
            m1.val[x][y] = m.val[y][x]

    return m1

def Determinant2x2(matrix):
    # print(matrix.val)
    return matrix.val[0][0] * matrix.val[1][1] - matrix.val[0][1] * matrix.val[1][0]

def submatrix(matrix, row, column):
    temp = deepcopy(matrix)
    del temp.val[row]
    for i in range(len(temp.val)):
        del temp.val[i][column]

    temp.updateInfo()
    # print(temp.val)
    return temp

def Minor3x3(matrix, row, column):
    s = submatrix(matrix, row, column)

    if len(s.val) > 2:
        return Determinant(s)
    else:
        return Determinant2x2(s)

def Cofactor3x3(matrix, row, column):
    minor = Minor3x3(matrix, row, column)
    if (row + column) % 2 == 0:
        return minor
    else:
        return -minor

def Determinant(matrix):
    if matrix.row == 2:
        return Determinant2x2(matrix.val)
    else:
        d = 0
        for j in range(len(matrix.val[0])):
            c = Cofactor3x3(matrix, 0, j)

            d += c * matrix.val[0][j]
        return d

def MatrixInversion(matrix):
    d = Determinant(matrix)
    if d == 0:
        print("this matrix is not invertible")
        return None

    new = Matrix(matrix.row, matrix.col)
    for x in range(matrix.row):
        for y in range(matrix.col):
            new.val[x][y] = round(Cofactor3x3(matrix, x, y) / d, 6)
    new.transpose()
    # print(new.val)
    return new

def QuickInverse(m):
    matrix = Matrix()
    matrix.val[0][0], matrix.val[0][1], matrix.val[0][2], matrix.val[0][3] = m.val[0][0], m.val[1][0], m.val[2][0], 0.0
    matrix.val[1][0], matrix.val[1][1], matrix.val[1][2], matrix.val[1][3] = m.val[0][1], m.val[1][1], m.val[2][1], 0.0
    matrix.val[2][0], matrix.val[2][1], matrix.val[2][2], matrix.val[2][3] = m.val[0][2], m.val[1][2], m.val[2][2], 0.0
    matrix.val[3][0] = -(m.val[3][0] * matrix.val[0][0] + m.val[3][1] * matrix.val[1][0] + m.val[3][2] * matrix.val[2][0])
    matrix.val[3][1] = -(m.val[3][0] * matrix.val[0][1] + m.val[3][1] * matrix.val[1][1] + m.val[3][2] * matrix.val[2][1])
    matrix.val[3][2] = -(m.val[3][0] * matrix.val[0][2] + m.val[3][1] * matrix.val[1][2] + m.val[3][2] * matrix.val[2][2])
    matrix.val[3][3] = 1.0
    return matrix;
