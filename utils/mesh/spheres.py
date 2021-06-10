from utils.mesh.base import Mesh
from utils.triangle import Triangle
from utils.vector import Vector3, Vector2
from math import sin, cos, pi

def SphereTriangles(color,n_subdivision=10, radius=1):
    #simple UV SPHERE
    meshData = []
    vertices  = []

    #adding top vertex
    vertices.append(Vector3(0, radius, 0))
    #generate vertices of the sphere
    for i in range(n_subdivision):
        phi = pi * (i+1) / n_subdivision
        for j in range(n_subdivision):
            theta = 2 * pi * j / n_subdivision
            x = radius * sin(phi) * cos(theta)
            y = radius * cos(phi)
            z = radius * sin(phi) * sin(theta)
            vertices.append(Vector3(x, y, z))
    #add bottom vertex
    vertices.append(Vector3(0, -radius, 0))

    #add top and bottom triangles
    for i in range(n_subdivision):
        i0 = i + 1
        i1 = (i+1) % n_subdivision + 1
        meshData.append(Triangle(vertices[0], vertices[i1], vertices[i0], color) )
        i0 = i + n_subdivision * (n_subdivision - 2) + 1
        i1 = (i+1) % n_subdivision + n_subdivision * (n_subdivision - 2) + 1
        meshData.append( Triangle(vertices[-1], vertices[i1], vertices[i0], color) )

    for j in range(n_subdivision-2):
        j0 = j * n_subdivision + 1
        j1 = (j+1) * n_subdivision + 1
        for i in range(n_subdivision):
            i0 = j0 + i
            i1 = j0 + (i + 1) % n_subdivision
            i2 = j1 + (i + 1) % n_subdivision
            i3 = j1 + i
            meshData.append( Triangle(vertices[i0], vertices[i1], vertices[i2], color))
            meshData.append( Triangle(vertices[i0], vertices[i2], vertices[i3], color))

    return meshData

# Not finished
# def IcosphereTriangles(color=(), subdivision=10, radius=1):
#     meshData = []
#     vertices = []
#
#     g = (1 + sqrt(5))/2
#
#     initialVertices = [
#         Vector3(-1,  g, 0),
#         Vector3( 1,  g, 0),
#         Vector3(-1, -g, 0),
#         Vector3( 1, -g, 0),
#
#         Vector3( 0, -1,  g),
#         Vector3( 0,  1,  g),
#         Vector3( 0, -1, -g),
#         Vector3( 0,  1, -g),
#
#         Vector3( g,  0,  -1),
#         Vector3( g,  0,  1),
#         Vector3( -g,  0,  -1),
#         Vector3( -g,  0,  1)
#     ]
#     initialIndices = [
#          # 5 faces around point 0
#          [0, 11, 5],
#          [0, 5, 1],
#          [0, 1, 7],
#          [0, 7, 10],
#          [0, 10, 11],
#          # Adjacent faces
#          [1, 5, 9],
#          [5, 11, 4],
#          [11, 10, 2],
#          [10, 7, 6],
#          [7, 1, 8],
#          # 5 faces around 3
#          [3, 9, 4],
#          [3, 4, 2],
#          [3, 2, 6],
#          [3, 6, 8],
#          [3, 8, 9],
#          # Adjacent faces
#          [4, 9, 5],
#          [2, 4, 11],
#          [6, 2, 10],
#          [8, 6, 7],
#          [9, 8, 1]
#     ]
