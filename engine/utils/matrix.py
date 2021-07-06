from __future__ import annotations
from constants import *
from utils.vector import *
from math import cos, sin
from copy import deepcopy
from math import cos, sin
from utils.vector import Vector3


class Matrix:
    """Represents a matrix with standard operation support."""

    def __init__(self, r: int = 4, c: int = 4):
        """Initialize new Matrix with r rows and c cols. Sets all values to 0.0."""
        self.val = [[0.0 for _ in range(c)] for _ in range(r)]

    def __repr__(self) -> str:
        """repr(self)"""
        return f"matrix->{self.val}"

    @property
    def row(self) -> int:
        """The number of rows in self."""
        return len(self.val)

    @property
    def col(self) -> int:
        """The number of cols in self."""
        return len(self.val[0])

    @classmethod
    def from_vector(cls, vec: Vector3) -> Matrix:
        """Construct a new Matrix formed by a Vector3.
        Returns:
            Matrix - matrix with size 1, 4 populated by vec's x, y, z, w.
        """
        rv = cls(1, 4)
        rv.val = [[vec.x, vec.y, vec.z, vec.w]]
        return rv

    @classmethod
    def rotation_x(cls, angle: float) -> Matrix:
        """Construct a matrix which performs a rotation around the x-axis by angle radians
        Arguments:
            angle - angle in radians to for xrotmat to represent.
        Returns:
            Matrix - angle rotation around x-axis Matrix
        """
        matrix = cls()
        matrix.val = [
            [1, 0.0, 0.0, 0.0],
            [0.0, cos(angle), sin(angle), 0.0],
            [0.0, -sin(angle), cos(angle), 0.0],
            [0.0, 0.0, 0.0, 1],
        ]
        return matrix

    @classmethod
    def rotation_y(cls, angle: float) -> Matrix:
        """Construct a matrix which performs a rotation around the y-axis by angle radians
        Arguments:
            angle - angle in radians to for yrotmat to represent.
        Returns:
            Matrix - angle rotation around y-axis Matrix
        """
        matrix = cls()
        matrix.val = [
            [cos(angle), 0.0, -sin(angle), 0.0],
            [0.0, 1, 0.0, 0.0],
            [sin(angle), 0.0, cos(angle), 0.0],
            [0.0, 0.0, 0.0, 1],
        ]
        return matrix

    @classmethod
    def rotation_z(cls, angle: float) -> Matrix:
        """Construct a matrix which performs a rotation around the z-axis by angle radians
        Arguments:
            angle - angle in radians to for zrotmat to represent.
        Returns:
            Matrix - angle rotation around z-axis Matrix
        """
        matrix = cls()
        matrix.val = [
            [cos(angle), sin(angle), 0.0, 0.0],
            [-sin(angle), cos(angle), 0.0, 0.0],
            [0.0, 0.0, 1, 0.0],
            [0.0, 0.0, 0.0, 1],
        ]
        return matrix

    @classmethod
    def scaling(cls, scale: float) -> Matrix:
        """Construct a scaling matrix for the given scale factor.
        Arguments:
            scale - float, the scale value for Matrix to be constructed for
        Returns:
            Matrix - the scaling Matrix
        """
        matrix = cls()
        matrix.val = [
            [scale, 0.0, 0.0, 0.0],
            [0.0, scale, 0.0, 0.0],
            [0.0, 0.0, scale, 0.0],
            [0.0, 0.0, 0.0, 1],
        ]
        return matrix

    @classmethod
    def identity(cls, size: int = 4) -> Matrix:
        """Construct an identity matrix of the given size. Defined as a square matrix
        with 1s on the main diagonal, and 0s elsewhere.
        Arguments:
            size - int, the size of the identity matrix.
        Returns:
            Matrix - the specified identity matrix.
        """
        matrix = cls()
        matrix.val = [
            [1.0 if i == j else 0.0 for j in range(size)] for i in range(size)
        ]
        return matrix

    @classmethod
    def translate(cls, position: Vector3) -> Matrix:
        """Construct a Matrix that performs a translation specified by the give
        position.
        Arguments:
            position - the Vector3 to construct translation matrix by.
        Returns:
            Matrix - the constructed translation Matrix.
        """
        matrix = cls()
        matrix.val = [
            [1, 0.0, 0.0, position.x],
            [0.0, 1, 0.0, position.y],
            [0.0, 0.0, 1, position.z],
            [0.0, 0.0, 0.0, 1],
        ]
        return matrix

    def __matmul__(self, other: Matrix) -> Matrix:
        """Support for self @ other, defined as matrix multiplication.
        Raises:
            ValueError - if self and other have incompatible dimensions.
        Returns:
            Matrix - product of self and other, size is self.row x other.col.
        """
        if not isinstance(other, Matrix):
            return NotImplemented

        if self.col != other.row:
            raise ValueError(
                "Matrices incompatible for multiplication, got: "
                f"{(self.row, self.col)}, {(other.row, other.col)}"
            )

        rv = Matrix(self.row, other.col)
        for x in range(self.row):
            for y in range(other.col):
                val = sum(self.val[x][z] * other.val[z][y] for z in range(self.col))
                rv.val[x][y] = round(val, 5)

        return rv

    def transpose(self) -> Matrix:
        """Compute the transpose of self. Defined as the matrix formed by swapping the
        rows and cols of self.
        Returns:
            Matrix - transpose of self.
        """
        rv = Matrix(self.row, self.col)
        for x in range(self.row):
            for y in range(self.col):
                rv.val[x][y] = self.val[y][x]
        return rv

    def submatrix(self, row: int, col: int) -> Matrix:
        """Form the matrix resulting from removing the specified row and col
        from self.
        Returns:
            Matrix - self without row or col.
        """
        temp = deepcopy(self)
        del temp.val[row]
        for i in range(self.row):
            del temp.val[i][col]

        return temp

    def det(self) -> float:
        """Calculate the determinant of self.
        Raises:
            ValueError - If self is not square.
        Returns:
            float - self's determinant.
        """
        if self.row != self.col:
            raise ValueError("Matrix determinant only defined for square matrices.")

        if self.row == 2:
            return self.val[0][0] * self.val[1][1] - self.val[0][1] * self.val[1][0]

        d = 0.0
        for j in range(self.col):
            c = self.cofactor(0, j)
            d += c * self.val[0][j]
        return d

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
    return matrix


