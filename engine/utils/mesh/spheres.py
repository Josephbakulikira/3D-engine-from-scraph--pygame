from utils.mesh.base import Mesh
from utils.triangle import Triangle
from utils.vector import Vector3, Vector2, Normalize
from math import sin, cos, pi, sqrt, acos

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

def GetMiddlePoint(vec1, vec2, vertices, middlePointCache):
    a = vertices.index(vec1)
    b = vertices.index(vec2)

    # check if the edge is already divided to avoid duplicated vertices
    smallerIndex, greaterIndex = b, a
    if a < b:
        smallerIndex = a
        greaterIndex = b
    key = f"{smallerIndex}, {greaterIndex}"

    if key in middlePointCache:
        return middlePointCache[key]

    vertex1 = vertices[a]
    vertex2 = vertices[b]

    middle = Normalize( (vertex1+vertex2)/2 )
    vertices.append(middle)

    _index = vertices.index(middle)
    middlePointCache.update({key: _index})

    return _index

def IcosphereTriangles(color=(255, 255, 255), subdivision=0, radius=1):
    middlePointCache = {}
    g = (1 + sqrt(5))/2 #golden ratio

    vertices = [
        Normalize(Vector3(-1,  g, 0)),
        Normalize(Vector3( 1,  g, 0)),
        Normalize(Vector3(-1, -g, 0)),
        Normalize(Vector3( 1, -g, 0)),

        Normalize(Vector3( 0, -1,  g)),
        Normalize(Vector3( 0,  1,  g)),
        Normalize(Vector3( 0, -1, -g)),
        Normalize(Vector3( 0,  1, -g)),

        Normalize(Vector3( g,  0,  -1)),
        Normalize(Vector3( g,  0,  1)),
        Normalize(Vector3( -g,  0,  -1)),
        Normalize(Vector3( -g,  0,  1))
    ]
    triangles = [
         # 5 faces around point 0
         Triangle(vertices[0], vertices[11], vertices[5], color),
         Triangle(vertices[0], vertices[5], vertices[1], color),
         Triangle(vertices[0], vertices[1], vertices[7], color),
         Triangle(vertices[0], vertices[7], vertices[10], color),
         Triangle(vertices[0], vertices[10], vertices[11], color),
         # Adjacent faces
         Triangle(vertices[1], vertices[5], vertices[9], color),
         Triangle(vertices[5], vertices[11], vertices[4], color),
         Triangle(vertices[11], vertices[10], vertices[2], color),
         Triangle(vertices[10], vertices[7], vertices[6], color),
         Triangle(vertices[7], vertices[1], vertices[8], color),
         # 5 faces around 3
         Triangle(vertices[3], vertices[9], vertices[4], color),
         Triangle(vertices[3], vertices[4], vertices[2], color),
         Triangle(vertices[3], vertices[2], vertices[6], color),
         Triangle(vertices[3], vertices[6], vertices[8], color),
         Triangle(vertices[3], vertices[8], vertices[9], color),
         # Adjacent faces
         Triangle(vertices[4], vertices[9], vertices[5], color),
         Triangle(vertices[2], vertices[4], vertices[11], color),
         Triangle(vertices[6], vertices[2], vertices[10], color),
         Triangle(vertices[8], vertices[6], vertices[7], color),
         Triangle(vertices[9], vertices[8], vertices[1], color)
    ]

    # subdivision
    for i in range(subdivision):
        subdivisions = []
        for triangle in triangles:
            _i0 = GetMiddlePoint(triangle.vertex1, triangle.vertex2, vertices, middlePointCache)
            _i1 = GetMiddlePoint(triangle.vertex2, triangle.vertex3, vertices, middlePointCache)
            _i2 = GetMiddlePoint(triangle.vertex3, triangle.vertex1, vertices, middlePointCache)

            vertex1 = vertices[_i0]
            vertex2 = vertices[_i1]
            vertex3 = vertices[_i2]

            subdivisions.append(Triangle(triangle.vertex1, vertex1, vertex3, color))
            subdivisions.append(Triangle(triangle.vertex2, vertex2, vertex1, color))
            subdivisions.append(Triangle(triangle.vertex3, vertex3, vertex2, color))
            subdivisions.append(Triangle(vertex1, vertex2, vertex3, color))

        triangles = subdivisions
    #print(triangles)
    return triangles

def FibonnaciSphereTriangles(color=(255, 255, 255), n=50):
    #not finished
    triangles = []
    vertices = []
    # golden ratio in radians
    g = pi * (3 - sqrt(5))/2

    for i in range(n):
        y = 1 - (i / float(n - 1)) * 2  # y goes from 1 to -1
        radius = sqrt(1 - y * y)  # radius at y
        theta = g * i  # golden angle increment
        x = cos(theta) * radius
        z = sin(theta) * radius
        vertices.append(Vector3(x, y, z))

    for i in range(len(vertices)-3):
        vertex1 = vertices[i]
        vertex2 = vertices[i+1]
        vertex3 = vertices[i+2]
        triangles.append(Triangle(vertex1, vertex2, vertex3, color))

    print("work in progress")
    return triangles
