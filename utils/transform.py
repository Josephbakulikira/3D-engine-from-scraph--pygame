from math import cos, sin
import constants
import utils.vector as vector
import utils.matrix as matrix
from utils.camera import Camera


# TODO: move in matrix.Matrix class
def ProjectionMatrix(camera: Camera) -> matrix.Matrix:
    m = matrix.Matrix()
    m.val = [
        [constants.aspect * camera.tangent, 0.0, 0.0, 0.0],
        [0.0, camera.tangent, 0.0, 0.0],
        [0.0, 0.0, camera.far / (camera.far - camera.near), 1],
        [0.0, 0.0, (-camera.far * camera.near) / (camera.far - camera.near), 0.0],
    ]
    return m


# TODO: what are the types of these args ? Vector3 or floats ?
def PointAt(current, next, up) -> matrix.Matrix:
    f = (next - current).norm()  # forward vector
    u = (up - f * up.dot(f)).norm()  # up vector
    r = u.cross(f)  # right vector
    m = matrix.Matrix()
    m.val = [
        [r.x, r.y, r.z, 0.0],
        [u.x, u.y, u.z, 0.0],
        [f.x, f.y, f.z, 0.0],
        [current.x, current.y, current.z, 1.0],
    ]
    return m


# TODO: move in matrix.Matrix class
def RotationX(angle: float) -> matrix.Matrix:
    m = matrix.Matrix()
    m.val = [
        [1, 0.0, 0.0, 0.0],
        [0.0, cos(angle), sin(angle), 0.0],
        [0.0, -sin(angle), cos(angle), 0.0],
        [0.0, 0.0, 0.0, 1],
    ]
    return m


# TODO: move in matrix.Matrix class
def RotationY(angle: float) -> matrix.Matrix:
    m = matrix.Matrix()
    m.val = [
        [cos(angle), 0.0, -sin(angle), 0.0],
        [0.0, 1, 0.0, 0.0],
        [sin(angle), 0.0, cos(angle), 0.0],
        [0.0, 0.0, 0.0, 1],
    ]
    return m


# TODO: move into matrix.Matrix class
def RotationZ(angle: float) -> matrix.Matrix:
    m = matrix.Matrix()
    m.val = [
        [cos(angle), sin(angle), 0.0, 0.0],
        [-sin(angle), cos(angle), 0.0, 0.0],
        [0.0, 0.0, 1, 0.0],
        [0.0, 0.0, 0.0, 1],
    ]
    return m


# TODO: move into matrix.Matrix class
def ScalingMatrix(scale: float) -> matrix.Matrix:
    m = matrix.Matrix()
    m.val = [
        [scale, 0.0, 0.0, 0.0],
        [0.0, scale, 0.0, 0.0],
        [0.0, 0.0, scale, 0.0],
        [0.0, 0.0, 0.0, 1],
    ]
    return m


# TODO: move into matrix.Matrix class
# TODO: take in size as arg
def identityMatrix() -> matrix.Matrix:
    m = matrix.Matrix()
    m.val = [
        [1, 0.0, 0.0, 0.0],
        [0.0, 1, 0.0, 0.0],
        [0.0, 0.0, 1, 0.0],
        [0.0, 0.0, 0.0, 1],
    ]
    return m


# TODO: should move in matrix.Matrix class
def translateMatrix(pos: vector.Vector3) -> matrix.Matrix:
    m = matrix.Matrix()
    m.val = [
        [1, 0.0, 0.0, pos.x],
        [0.0, 1, 0.0, pos.y],
        [0.0, 0.0, 1, pos.z],
        [0.0, 0.0, 0.0, 1],
    ]
    return m


# TODO: perhaps this function should take in a Matrix as arg
# TODO: should move into matrix.Matrix class
def Shearing(
    xy: float, xz: float, yx: float, yz: float, zx: float, zy: float
) -> matrix.Matrix:
    m = matrix.Matrix()
    m.val = [
        [1, xy, xz, 0.0],
        [yx, 1, yz, 0.0],
        [zx, zy, 1, 0.0],
        [0.0, 0.0, 0.0, 1],
    ]
    return m
