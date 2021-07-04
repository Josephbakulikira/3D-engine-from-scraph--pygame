from __future__ import annotations
from math import sqrt
from typing import Union


class Vector3:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z
        self.w = 1

    def __repr__(self) -> str:
        return f" vec3-> ({self.x}, {self.y}, {self.z})"

    def __add__(self, other: Union[Vector3, float]) -> Vector3:
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        return Vector3(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other: Union[Vector3, float]) -> Vector3:
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        return Vector3(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other: Union[Vector3, float]) -> Vector3:
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: Union[Vector3, float]) -> Vector3:
        if isinstance(other, Vector3):
            return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)
        return Vector3(self.x / other, self.y / other, self.z / other)

    def toMatrix(self) -> list[list[float]]:
        return [[self.x, self.y, self.z, self.w]]

    def GetTuple(self) -> tuple[int, int]:
        return (int(self.x), int(self.y))

    def cross(self, other: Vector3) -> Vector3:
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3(x, y, z)

    def dot(self, other: Vector3) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def mag(self) -> float:
        return sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    def norm(self) -> Vector3:
        mg = self.mag()
        if mg:
            return Vector3(self.x / mg, self.y / mg, self.z / mg)
        return Vector3()


class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"vec2-> ({self.x}, {self.y})"

    def __add__(self, other: Union[Vector2, float]) -> Vector2:
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        return Vector2(self.x + other, self.y + other)

    def __sub__(self, other: Union[Vector2, float]) -> Vector2:
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        return Vector2(self.x - other, self.y - other)

    def __mul__(self, other: Union[Vector2, float]) -> Vector2:
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other: Union[Vector2, float]) -> Vector2:
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        return Vector2(self.x / other, self.y / other)

    def mag(self) -> float:
        return sqrt((self.x ** 2) + (self.y ** 2))


def toVector3(matrix) -> Vector3:
    return Vector3(matrix.val[0][0], matrix.val[0][1], matrix.val[0][2])


def crossProduct(a: Vector3, b: Vector3) -> Vector3:
    return a.cross(b)


def dotProduct(a: Vector3, b: Vector3) -> float:
    return a.dot(b)


def GetMagnitude(a: Vector3) -> float:
    return a.mag()


def Normalize(a: Vector3) -> Vector3:
    return a.norm()


def PlaneLineIntersection(pos, normal, lineStart, lineEnd):
    normal = Normalize(normal)
    p = -dotProduct(normal, pos)
    ad = dotProduct(lineStart, normal)
    bd = dotProduct(lineEnd, normal)
    t = (-p - ad) / (bd - ad)
    lineStartEnd = lineEnd - lineStart
    lineTointersect = lineStartEnd * t
    return lineStart + lineTointersect
