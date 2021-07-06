import pygame
from utils.vector import *
from utils.triangle import Triangle
from constants import *
from utils.mesh.point import *
import colorsys

def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def DrawTriangle(screen, triangle, fill, wireframe, vertices, radius, verticeColor, wireframeColor, lineWidth):

    if fill == True:
        #print(triangle.color)
        pygame.draw.polygon(screen, triangle.color, triangle.GetPolygons())

    if wireframe == True:
        pygame.draw.line(screen, wireframeColor, triangle.vertex1.GetTuple(), triangle.vertex2.GetTuple(), lineWidth)
        pygame.draw.line(screen, wireframeColor, triangle.vertex2.GetTuple(), triangle.vertex3.GetTuple(), lineWidth)
        pygame.draw.line(screen, wireframeColor, triangle.vertex3.GetTuple(), triangle.vertex1.GetTuple(), lineWidth)

    if vertices == True:
        color = (255, 255 ,255) if verticeColor==False else triangle.verticeColor

        pygame.draw.circle(screen, color, triangle.vertex1.GetTuple(), radius)
        pygame.draw.circle(screen, color, triangle.vertex2.GetTuple(), radius)
        pygame.draw.circle(screen, color, triangle.vertex3.GetTuple(), radius)

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def LoadMesh(objectPath, color=(255, 255, 255)):
    vert_data = []
    triangle_indices = []
    data = None
    meshData = []

    #read and close file
    with open(objectPath, 'r') as objectFile:
        data = objectFile.readlines()

    # get data
    for _line in data:
        _line = _line.split(" ")
        if _line[0] == 'v':
            vert_data.append(Vector3(float(_line[1]), float(_line[2]), float(_line[3])))
        elif _line[0] == 'f':
            temp = _line[1:]
            line_indices = []
            for el in temp:
                indexList = el.split('/')
                line_indices.append(int(indexList[0]) )

            triangle_indices.append(line_indices)

    for t in triangle_indices:
        triangle = Triangle( vert_data[t[0]-1], vert_data[t[1]-1],vert_data[t[2]-1], color)
        meshData.append(triangle)
    return meshData

def translateValue(value, min1, max1, min2, max2):
    return min2 + (max2 - min2)* ((value-min1)/(max1-min1))

def SignedDist(pos, normal, p):
    n = Normalize(pos)
    return (normal.x * pos.x + normal.y * pos.y + normal.z * pos.z - dotProduct(normal, p))

def TriangleClipped(pos, normal, triangle, outTriangle, clippingDebug=False):
    #normal = Normalize(normal)

    insidePoints, insideCount = [None for _ in range(3)], 0
    outsidePoints, outsideCount = [None for _ in range(3)], 0

    d0 = SignedDist(triangle.vertex1, normal, pos)
    d1 = SignedDist(triangle.vertex2, normal, pos)
    d2 = SignedDist(triangle.vertex3, normal, pos)

    if d0 >= 0:
        insidePoints[insideCount] = triangle.vertex1
        insideCount += 1
    else:
        outsidePoints[outsideCount] = triangle.vertex1
        outsideCount += 1

    if d1 >= 0:
        insidePoints[insideCount] = triangle.vertex2
        insideCount += 1
    else:
        outsidePoints[outsideCount] = triangle.vertex2
        outsideCount += 1

    if d2 >= 0:
        insidePoints[insideCount] = triangle.vertex3
        insideCount += 1
    else:
        outsidePoints[outsideCount] = triangle.vertex3
        outsideCount += 1

    if insideCount == 0:
        return 0
    if insideCount == 3:
        outTriangle[0] = triangle

        return 1

    if insideCount == 1 and outsideCount == 2:
        # outTriangle[0].color = (0, 255,24)
        outTriangle[0].color = triangle.color if clippingDebug==False else red

        outTriangle[0].vertex1 = insidePoints[0]
        outTriangle[0].vertex2 = PlaneLineIntersection(pos, normal, insidePoints[0], outsidePoints[0])
        outTriangle[0].vertex3 = PlaneLineIntersection(pos, normal, insidePoints[0], outsidePoints[1])
        return 1

    if insideCount == 2 and outsideCount == 1:

        # outTriangle[0].color = (55, 60, 255)
        # outTriangle[1].color = (255,51, 12)
        outTriangle[0].color = triangle.color if clippingDebug==False else blue
        outTriangle[1].color = triangle.color if clippingDebug==False else green
        outTriangle[0].vertex1 = insidePoints[1]
        outTriangle[0].vertex2 = insidePoints[0]
        outTriangle[0].vertex3 = PlaneLineIntersection(pos, normal, insidePoints[0], outsidePoints[0])

        outTriangle[1].vertex1 = insidePoints[1]
        outTriangle[1].vertex2 = outTriangle[0].vertex3
        outTriangle[1].vertex3 = PlaneLineIntersection(pos, normal, insidePoints[1], outsidePoints[0])

        return 2

def DrawAxis(screen, camera, scale=3,center=None, Xaxis=True, Yaxis=True, Zaxis=True, stroke=5):
    if center == None:
        center = Point(Vector3(0, 0, 0))

    X = Point(Vector3(scale, 0, 0), (255, 0, 0))
    Y = Point(Vector3(0, scale, 0), (0, 255, 0))
    Z = Point(Vector3(0, 0, scale), (0, 0, 255))
    origin = center.update(screen, camera)

    if Xaxis:
        x_axis = X.update(screen, camera, True)
        pygame.draw.line(screen, X.color, origin.GetTuple(),x_axis.GetTuple(), stroke)
    if Zaxis:
        z_axis = Z.update(screen, camera, True)
        pygame.draw.line(screen, Z.color, origin.GetTuple(), z_axis.GetTuple(), stroke)
    if Yaxis:
        y_axis = Y.update(screen, camera, True)
        pygame.draw.line(screen, Y.color, origin.GetTuple(), y_axis.GetTuple(), stroke)
