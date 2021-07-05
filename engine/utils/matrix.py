"""Contains class representing a mathematical Matrix and its standard defined
standard operations, as well as other utility functions.
"""
from __future__ import annotations
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

    def inv(self) -> Matrix:
        """Calculate the inverse matrix of self.
        Defined for matrix A as A^-1, such that A @ A^-1 = A^-1 @ A = I.
        Raises:
            ValueError - If the matrix doesn't have an inverse.
        Returns:
            Matrix - self's inverse matrix.
        """
        d = self.det()
        if not d:
            raise ValueError("Matrix not invertible, must have non-zero determinant.")

        new = Matrix(self.row, self.col)
        for x in range(self.row):
            for y in range(self.col):
                new.val[x][y] = round(self.cofactor(x, y) / d, 6)
        return new.transpose()

    # TODO: probably should remove this method and have just one inv method
    def quick_inv(self) -> Matrix:
        """Quickly compute and return the inverse of self.
        Returns:
            Matrix - self's inverse matrix.
        """
        m = self
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

    def minor(self, row: int, col: int) -> float:
        """Compute the minor of self for row, col. Defined as the determinant
        of the submatrix of self, formed when removing row and col.
        Returns:
            float - the determinant of submatrix(row, col) of self.
        """
        return self.submatrix(row, col).det()

    def cofactor(self, row: int, col: int) -> float:
        """Compute the cofactor of self for row, col. Defined as self's row, col minor
        multiplied by (-1)^(row + col).
        Returns:
            float - the cofactor of minor(row, col) of self.
        """
        minor = self.minor(row, col)
        if not (row + col) % 2:
            return minor
        return -minor


# TODO: refactor into Matrix class and add documentation
def multiplyMatrixVector(vec: Vector3, mat: Matrix) -> Vector3:
    temp = Matrix.from_vector(vec)
    m = temp @ mat
    v = Vector3.from_matrix(m)
    if m.val[0][3] != 0:
        v = v / m.val[0][3]
    return v
