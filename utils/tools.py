import pygame
from utils.vector import *
from utils.triangle import Triangle
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
