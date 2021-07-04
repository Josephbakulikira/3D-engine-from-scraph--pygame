from __future__ import annotations
import utils.vector as vector
from copy import deepcopy


class Matrix:
    def __init__(self, r: int = 4, c: int = 4):
        self.val = [[0.0 for _ in range(c)] for _ in range(r)]

    def __repr__(self) -> str:
        return f"matrix->{self.val}"

    @property
    def row(self) -> int:
        return len(self.val)

    @property
    def col(self) -> int:
        return len(self.val[0])

    def transpose(self) -> None:
        temp = [[0.0 for i in range(self.col)] for j in range(self.row)]
        for x in range(self.row):
            for y in range(self.col):
                temp[x][y] = self.val[y][x]
        self.val = temp

    def __matmul__(self, other: Matrix) -> Matrix:
        rv = Matrix(self.row, other.col)

        if self.col != other.row:
            raise TypeError(
                "Matrices incompatible for multiplication, got: "
                f"{(self.row, self.col)}, {(other.row, other.col)}"
            )

        for x in range(self.row):
            for y in range(other.col):
                _sum = 0.0
                for z in range(self.col):
                    _sum += self.val[x][z] * other.val[z][y]
                rv.val[x][y] = round(_sum, 5)

        return rv

    def submatrix(self, row: int, col: int) -> Matrix:
        temp = deepcopy(self)
        del temp.val[row]
        for i in range(len(temp.val)):
            del temp.val[i][col]

        return temp


def multiplyMatrix(m1: Matrix, m2: Matrix) -> Matrix:
    return m1 @ m2


def multiplyMatrixVector(vec: vector.Vector3, mat: Matrix) -> vector.Vector3:
    temp = Matrix(1, 4)
    temp.val = vec.toMatrix()
    m = temp @ mat
    v = vector.Vector3.from_matrix(m)
    if m.val[0][3] != 0:
        v = v / m.val[0][3]
    return v


def TransposeMatrix(m: Matrix) -> Matrix:
    m1 = Matrix(m.row, m.col)
    for x in range(m.row):
        for y in range(m.col):
            m1.val[x][y] = m.val[y][x]

    return m1


def Determinant2x2(matrix: Matrix) -> float:
    return matrix.val[0][0] * matrix.val[1][1] - matrix.val[0][1] * matrix.val[1][0]


def submatrix(matrix: Matrix, row: int, col: int) -> Matrix:
    return matrix.submatrix(row, col)


def Minor3x3(matrix: Matrix, row: int, col: int) -> float:
    s = matrix.submatrix(row, col)

    if len(s.val) > 2:
        return Determinant(s)
    return Determinant2x2(s)


def Cofactor3x3(matrix: Matrix, row: int, col: int) -> float:
    minor = Minor3x3(matrix, row, col)
    if not (row + col) % 2:
        return minor
    return -minor


def Determinant(matrix: Matrix) -> float:
    if matrix.row == 2:
        return Determinant2x2(matrix)

    d = 0.0
    for j in range(len(matrix.val[0])):
        c = Cofactor3x3(matrix, 0, j)

        d += c * matrix.val[0][j]
    return d


def MatrixInversion(matrix: Matrix) -> Matrix:
    d = Determinant(matrix)
    if not d:
        raise TypeError("Matrix not invertible, must have non-zero determinant.")

    new = Matrix(matrix.row, matrix.col)
    for x in range(matrix.row):
        for y in range(matrix.col):
            new.val[x][y] = round(Cofactor3x3(matrix, x, y) / d, 6)
    new.transpose()
    return new


def QuickInverse(m: Matrix) -> Matrix:
    matrix = Matrix()
    matrix.val[0][0], matrix.val[0][1], matrix.val[0][2], matrix.val[0][3] = (
        m.val[0][0],
        m.val[1][0],
        m.val[2][0],
        0.0,
    )
    matrix.val[1][0], matrix.val[1][1], matrix.val[1][2], matrix.val[1][3] = (
        m.val[0][1],
        m.val[1][1],
        m.val[2][1],
        0.0,
    )
    matrix.val[2][0], matrix.val[2][1], matrix.val[2][2], matrix.val[2][3] = (
        m.val[0][2],
        m.val[1][2],
        m.val[2][2],
        0.0,
    )
    matrix.val[3][0] = -(
        m.val[3][0] * matrix.val[0][0]
        + m.val[3][1] * matrix.val[1][0]
        + m.val[3][2] * matrix.val[2][0]
    )
    matrix.val[3][1] = -(
        m.val[3][0] * matrix.val[0][1]
        + m.val[3][1] * matrix.val[1][1]
        + m.val[3][2] * matrix.val[2][1]
    )
    matrix.val[3][2] = -(
        m.val[3][0] * matrix.val[0][2]
        + m.val[3][1] * matrix.val[1][2]
        + m.val[3][2] * matrix.val[2][2]
    )
    matrix.val[3][3] = 1.0
    return matrix
