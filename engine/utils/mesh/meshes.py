from utils.mesh.base import Mesh
from utils.triangle import Triangle
from utils.vector import Vector3, Vector2
from math import sin, cos, pi

def translate(value, min1, max1, min2, max2):
    return min2 + (max2 - min2) * ((value-min1)/(max1-min1))

def CubeTriangles(color, position=Vector3(), scale=1):
    return [
    Triangle( Vector3(-1.0, -1.0, -1.0) * scale + position, Vector3(-1.0, 1.0, -1.0) * scale + position, Vector3(1.0, 1.0, -1.0) * scale + position, color),
    Triangle( Vector3(-1.0, -1.0, -1.0) * scale + position, Vector3(1.0, 1.0, -1.0) * scale + position, Vector3(1.0, -1.0, -1.0) * scale + position, color),

    Triangle( Vector3(1.0, -1.0, -1.0) * scale + position, Vector3(1.0, 1.0, -1.0) * scale + position, Vector3(1.0, 1.0, 1.0) * scale + position, color),
    Triangle( Vector3(1.0, -1.0, -1.0) * scale + position, Vector3(1.0, 1.0, 1.0) * scale + position, Vector3(1.0, -1.0, 1.0) * scale + position, color),

    Triangle( Vector3(1.0, -1.0, 1.0) * scale + position, Vector3(1.0, 1.0, 1.0) * scale + position, Vector3(-1.0, 1.0, 1.0) * scale + position, color),
    Triangle( Vector3(1.0, -1.0, 1.0) * scale + position, Vector3(-1.0, 1.0, 1.0) * scale + position, Vector3(-1.0, -1.0, 1.0) * scale + position, color),

    Triangle( Vector3(-1.0, -1.0, 1.0) * scale + position, Vector3(-1.0, 1.0, 1.0) * scale + position, Vector3(-1.0, 1.0, -1.0) * scale + position, color),
    Triangle( Vector3(-1.0, -1.0, 1.0) * scale + position, Vector3(-1.0, 1.0, -1.0) * scale + position, Vector3(-1.0, -1.0, -1.0) * scale + position, color),

    Triangle( Vector3(-1.0, 1.0, -1.0) * scale + position, Vector3(-1.0, 1.0, 1.0) * scale + position, Vector3(1.0, 1.0, 1.0) * scale + position, color),
    Triangle( Vector3(-1.0, 1.0, -1.0) * scale + position, Vector3(1.0, 1.0, 1.0) * scale + position, Vector3(1.0, 1.0, -1.0) * scale + position, color),

    Triangle( Vector3(1.0, -1.0, 1.0) * scale + position, Vector3(-1.0, -1.0, 1.0) * scale + position, Vector3(-1.0, -1.0, -1.0) * scale + position, color),
    Triangle( Vector3(1.0, -1.0, 1.0) * scale + position, Vector3(-1.0, -1.0, -1.0) * scale + position, Vector3(1.0, -1.0, -1.0) * scale + position, color),
]



def QuadTriangles(color=(255, 255, 255), size=5):
    vertices = [
        Vector3(-size, -size, -size),
        Vector3(-size, size, -size),
        Vector3(size, size, -size),
        Vector3(size, -size, -size)
    ]

    return [
        Triangle(vertices[0], vertices[1], vertices[2], color),
        Triangle(vertices[0], vertices[2], vertices[3], color)
    ]

def PlaneTriangles(color=(255, 255, 255), resolution=10, size=2):
    meshData = []
    vertices = [[None for i in range(resolution)] for j in range(resolution)]

    for i in range(resolution):
        for j in range(resolution):
            x = translate(i, 0, resolution, -size, size)
            y = translate(j, 0, resolution, -size, size)
            vertices[i][j] = Vector3(x, 0, y)

    for i in range(resolution):
        for j in range(resolution):
            if i + 1 < resolution and j + 1 < resolution:
                v1 = vertices[i][j]
                v2 = vertices[i+1][j]
                v3 = vertices[i][j+1]
                v4 = vertices [i+1][j+1]
                meshData.append(Triangle(v1, v2, v3, color))
                meshData.append(Triangle(v4, v3, v2, color))


    return meshData
