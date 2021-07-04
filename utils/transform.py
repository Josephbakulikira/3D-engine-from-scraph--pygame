import utils.matrix as matrix

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
