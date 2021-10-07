from utils.vector import Normalize, crossProduct, dotProduct
import utils.matrix as matrix
import utils.vector as vector

# PointAt(vector3 cameraPosition, Vector3 cameraTarget, Vector3 cameraUpVector)
def PointAt(current, next, up) -> matrix.Matrix:
    #f = (next - current).norm()
    #u = (up - f * up.dot(f)).norm()
    #r = u.cross(f)  # right vector
    f = vector.Normalize(next - current) # forward vector
    u = (up - f * vector.dotProduct(up, f)) # up vector
    r = crossProduct(u, f) # right vector

    m = matrix.Matrix()
    m.val = [
        [r.x, r.y, r.z, 0.0],
        [u.x, u.y, u.z, 0.0],
        [f.x, f.y, f.z, 0.0],
        [current.x, current.y, current.z, 1.0],
    ]
    return m


# TODO: perhaps this function should take in a Matrix as arg
# TODO: should move into matrix.Matrix class?
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
