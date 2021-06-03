from utils.mesh.base import Mesh
from utils.triangle import Triangle
from utils.vector import Vector3, Vector2


def CubeTriangles(color):
    return [
    Triangle( Vector3(0.0, 0.0, 0.0,), Vector3(0.0, 1.0, 0.0), Vector3(1.0, 1.0, 0.0), color),
    Triangle( Vector3(0.0, 0.0, 0.0,), Vector3(1.0, 1.0, 0.0), Vector3(1.0, 0.0, 0.0), color),

    Triangle( Vector3(1.0, 0.0, 0.0), Vector3(1.0, 1.0, 0.0), Vector3(1.0, 1.0, 1.0), color),
    Triangle( Vector3(1.0, 0.0, 0.0), Vector3(1.0, 1.0, 1.0), Vector3(1.0, 0.0, 1.0), color),

    Triangle( Vector3(1.0, 0.0, 1.0), Vector3(1.0, 1.0, 1.0), Vector3(0.0, 1.0, 1.0), color),
    Triangle( Vector3(1.0, 0.0, 1.0), Vector3(0.0, 1.0, 1.0), Vector3(0.0, 0.0, 1.0), color),

    Triangle( Vector3(0.0, 0.0, 1.0), Vector3(0.0, 1.0, 1.0), Vector3(0.0, 1.0, 0.0), color),
    Triangle( Vector3(0.0, 0.0, 1.0), Vector3(0.0, 1.0, 0.0), Vector3(0.0, 0.0, 0.0), color),

    Triangle( Vector3(0.0, 1.0, 0.0), Vector3(0.0, 1.0, 1.0), Vector3(1.0, 1.0, 1.0), color),
    Triangle( Vector3(0.0, 1.0, 0.0), Vector3(1.0, 1.0, 1.0), Vector3(1.0, 1.0, 0.0), color),

    Triangle( Vector3(1.0, 0.0, 1.0), Vector3(0.0, 0.0, 1.0), Vector3(0.0, 0.0, 0.0), color),
    Triangle( Vector3(1.0, 0.0, 1.0), Vector3(0.0, 0.0, 0.0), Vector3(1.0, 0.0, 0.0), color),
]


# def Cube:
#     mesh = Mesh()
#     mesh.triangles = np.array([
#         [ 0.0, 0.0, 0.0,    0.0, 1.0, 0.0,    1.0, 1.0, 0.0 ],
#         [ 0.0, 0.0, 0.0,    1.0, 1.0, 0.0,    1.0, 0.0, 0.0 ],
#
#         [ 1.0, 0.0, 0.0,    1.0, 1.0, 0.0,    1.0, 1.0, 1.0 ],
#         [ 1.0, 0.0, 0.0,    1.0, 1.0, 1.0,    1.0, 0.0, 1.0 ],
#
#         [ 1.0, 0.0, 1.0,    1.0, 1.0, 1.0,    0.0, 1.0, 1.0 ],
#         [ 1.0, 0.0, 1.0,    0.0, 1.0, 1.0,    0.0, 0.0, 1.0 ],
#
#         [ 0.0, 0.0, 1.0,    0.0, 1.0, 1.0,    0.0, 1.0, 0.0 ],
#         [ 0.0, 0.0, 1.0,    0.0, 1.0, 0.0,    0.0, 0.0, 0.0 ],
#
#         [ 0.0, 1.0, 0.0,    0.0, 1.0, 1.0,    1.0, 1.0, 1.0 ],
#         [ 0.0, 1.0, 0.0,    1.0, 1.0, 1.0,    1.0, 1.0, 0.0 ],
#
#         [ 1.0, 0.0, 1.0,    0.0, 0.0, 1.0,    0.0, 0.0, 0.0 ],
#         [ 1.0, 0.0, 1.0,    0.0, 0.0, 0.0,    1.0, 0.0, 0.0 ],
# 		])
