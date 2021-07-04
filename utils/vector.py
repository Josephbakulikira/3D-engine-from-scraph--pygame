"""Contains classes representing 2D and 3D vectors, each with defined
standard operations, as well as other utility functions.
"""

from __future__ import annotations
from math import sqrt
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from utils.matrix import Matrix

# TODO: Use shared based class to reduce duplicated code between Vector2 and Vector3


class Vector3:
    """Represents a vector in 3-D space with standard operation support."""

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        """Initialize new Vector3 with entries x, y, z. Sets w to 1."""
        self.x = x
        self.y = y
        self.z = z
        self.w = 1

    def __repr__(self) -> str:
        """repr(self)"""
        return f" vec3-> ({self.x}, {self.y}, {self.z})"

    @classmethod
    def from_matrix(cls, matrix: Matrix) -> Vector3:
        """Construct a Vector3 fro an existing Matrix. Uses first 3 columns
        of first row of Matrix to fill Vector3's x, y, z. Sets w = 1.
        Arguments:
            matrix - Matrix to form Vector3 from.
        Returns:
            Vector3 - formed from matrix.
        """
        return cls(matrix.val[0][0], matrix.val[0][1], matrix.val[0][2])

    def __add__(self, other: Union[Vector3, float]) -> Vector3:
        """Support for self + other, defined as elementwise addition if other is
        a Vector3, or scalar addition if other is numeric (strictly int or float.)
        Arguments:
            other - float, int, or Vector3 to perform addition with
        Returns:
            Vector3 - formed from either element-wise or scalar-addition.
        """
        if not isinstance(other, (int, float, Vector3)):
            return NotImplemented

        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        return Vector3(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other: Union[Vector3, float]) -> Vector3:
        """Support for self - other, defined as elementwise subtraction if other is
        a Vector3, or scalar subtraction if other is numeric (strictly int or float.)
        Arguments:
            other - float, int, or Vector3 to perform subtraction with
        Returns:
            Vector3 - formed from either element-wise or scalar-subtraction.
        """
        if not isinstance(other, (int, float, Vector3)):
            return NotImplemented

        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        return Vector3(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other: Union[Vector3, float]) -> Vector3:
        """Support for self * other, defined as elementwise multiplication if other is
        a Vector3, or scalar multiplication if other is numeric (strictly int or float.)
        Arguments:
            other - float, int, or Vector3 to perform multiplication with
        Returns:
            Vector3 - formed from either element-wise or scalar-multiplication.
        """
        if not isinstance(other, (int, float, Vector3)):
            return NotImplemented

        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: Union[Vector3, float]) -> Vector3:
        """Support for self / other, defined as elementwise division if other is
        a Vector3, or scalar division if other is numeric (strictly int or float.)
        Arguments:
            other - float, int, or Vector3 to perform division with
        Returns:
            Vector3 - formed from either element-wise or scalar-division.
        """
        if not isinstance(other, (int, float, Vector3)):
            return NotImplemented

        if isinstance(other, Vector3):
            return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)
        return Vector3(self.x / other, self.y / other, self.z / other)

    # TODO: rename to get_tuple (more Pythonic naming conventions)
    def GetTuple(self) -> tuple[int, int]:
        """Get a tuple representation of self, defined as the int-cast x and y
        attributes in 2-tuple.
        Returns:
            tuple[int, int] - the int-cast x and y attributes.
        """
        return (int(self.x), int(self.y))

    def cross(self, other: Vector3) -> Vector3:
        """Compute the cross product of self and other, defined as the mutually
        orthogonal vector to both self and other.
        Non-commutative, strictly self cross other.
        Arguments:
            other - Vector3 to cross with self.
        Returns:
            Vector3 - the cross of self and other.
        """
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3(x, y, z)

    def dot(self, other: Vector3) -> float:
        """Compute the dot product of self and other, defined as the sum of
        corresponding element products. Commutative.
        Arguments:
            other - Vector3 to dot with self.
        Returns:
            float - the dot product of self and other
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def mag(self) -> float:
        """Compute the magnitude of self, defined as the root mean square of
        self's elements.
        Returns:
            float - the length of self.
        """
        return sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    def norm(self) -> Vector3:
        """Compute the norm of self, defined as the vector in the direction of self
        with magnitude 1.
        Returns:
            Vector3 - the norm of vector self.
        """
        mg = self.mag()
        if mg:
            return Vector3(self.x / mg, self.y / mg, self.z / mg)
        return Vector3()


class Vector2:
    """Represents a vector in 2-D space with standard operation support."""

    def __init__(self, x: float = 0, y: float = 0):
        """Initialize new Vector2 with entries x and y."""
        self.x, self.y = x, y

    def __repr__(self) -> str:
        """repr(self)"""
        return f"vec2-> ({self.x}, {self.y})"

    def __add__(self, other: Union[Vector2, float]) -> Vector2:
        """Support for self + other, defined as elementwise addition if other is
        a Vector2, or scalar addition if other is numeric (strictly int or float.)
        Arguments:
            other - float, int, or Vector3 to perform addition with
        Returns:
            Vector2 - formed from either element-wise or scalar-addition.
        """
        if not isinstance(other, (int, float, Vector3)):
            return NotImplemented

        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        return Vector2(self.x + other, self.y + other)

    def __sub__(self, other: Union[Vector2, float]) -> Vector2:
        """Support for self - other, defined as elementwise subtraction if other is
        a Vector2, or scalar subtraction if other is numeric (strictly int or float.)
        Arguments:
            other - float, int, or Vector3 to perform subtraction with
        Returns:
            Vector2 - formed from either element-wise or scalar-subtraction.
        """
        if not isinstance(other, (int, float, Vector3)):
            return NotImplemented

        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        return Vector2(self.x - other, self.y - other)

    def __mul__(self, other: Union[Vector2, float]) -> Vector2:
        """Support for self * other, defined as elementwise multiplication if other is
        a Vector2, or scalar multiplication if other is numeric (strictly int or float.)
        Arguments:
            other - float, int, or Vector3 to perform multiplication with
        Returns:
            Vector2 - formed from either element-wise or scalar-multiplication.
        """
        if not isinstance(other, (int, float, Vector3)):
            return NotImplemented

        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other: Union[Vector2, float]) -> Vector2:
        """Support for self / other, defined as elementwise division if other is
        a Vector2, or scalar division if other is numeric (strictly int or float.)
        Arguments:
            other - float, int, or Vector3 to perform division with
        Returns:
            Vector2 - formed from either element-wise or scalar-division.
        """
        if not isinstance(other, (int, float, Vector3)):
            return NotImplemented

        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        return Vector2(self.x / other, self.y / other)

    def mag(self) -> float:
        """Compute the magnitude of self, defined as the root mean square of
        self's elements.
        Returns:
            float - the length of self.
        """
        return sqrt((self.x ** 2) + (self.y ** 2))

    def norm(self) -> Vector2:
        """Compute the norm of self, defined as the vector in the direction of self
        with magnitude 1.
        Returns:
            Vector2 - the norm of vector self.
        """
        mg = self.mag()
        if mg:
            return Vector2(self.x / mg, self.y / mg)
        return Vector2()


# TODO: get types and add documentation
def PlaneLineIntersection(pos, normal, lineStart, lineEnd):
    normal = normal.norm()
    p = -normal.dot(pos)
    ad = lineStart.dot(normal)
    bd = lineEnd.dot(normal)
    t = (-p - ad) / (bd - ad)
    lineStartEnd = lineEnd - lineStart
    lineTointersect = lineStartEnd * t
    return lineStart + lineTointersect
