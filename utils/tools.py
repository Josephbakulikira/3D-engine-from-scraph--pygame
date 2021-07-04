import pygame
import utils.vector as vector
from utils.triangle import Triangle
import constants
import utils.mesh.point as point
import colorsys
from os import PathLike


def hsv_to_rgb(h, s, v) -> tuple[int, int, int]:
    rgb = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

    # awkward return statement expression due to mypy appeasement, should revisit
    return (rgb[0], rgb[1], rgb[2])


def DrawTriangle(
    screen,
    triangle,
    fill,
    wireframe,
    vertices,
    radius,
    verticeColor,
    wireframeColor,
    lineWidth,
):

    if fill:
        pygame.draw.polygon(screen, triangle.color, triangle.GetPolygons())

    if wireframe:
        pygame.draw.line(
            screen,
            wireframeColor,
            triangle.vertex1.GetTuple(),
            triangle.vertex2.GetTuple(),
            lineWidth,
        )
        pygame.draw.line(
            screen,
            wireframeColor,
            triangle.vertex2.GetTuple(),
            triangle.vertex3.GetTuple(),
            lineWidth,
        )
        pygame.draw.line(
            screen,
            wireframeColor,
            triangle.vertex3.GetTuple(),
            triangle.vertex1.GetTuple(),
            lineWidth,
        )

    if vertices:
        color = (255, 255, 255) if not verticeColor else triangle.verticeColor

        pygame.draw.circle(screen, color, triangle.vertex1.GetTuple(), radius)
        pygame.draw.circle(screen, color, triangle.vertex2.GetTuple(), radius)
        pygame.draw.circle(screen, color, triangle.vertex3.GetTuple(), radius)


def LoadMesh(
    objectPath: PathLike, color: tuple[int, int, int] = (255, 255, 255)
) -> list[Triangle]:
    vert_data = []
    triangle_indices = []
    data = None
    meshData = []

    # read and close file
    with open(objectPath, "r") as objectFile:
        data = objectFile.readlines()

    # get data
    for _line in data:
        line = _line.split(" ")
        if line[0] == "v":
            vert_data.append(
                vector.Vector3(float(line[1]), float(line[2]), float(line[3]))
            )
        elif line[0] == "f":
            temp = line[1:]
            line_indices = []
            for el in temp:
                indexList = el.split("/")
                line_indices.append(int(indexList[0]))

            triangle_indices.append(line_indices)

    for t in triangle_indices:
        triangle = Triangle(
            vert_data[t[0] - 1], vert_data[t[1] - 1], vert_data[t[2] - 1], color
        )
        meshData.append(triangle)
    return meshData


def translateValue(value, min1, max1, min2, max2):
    return min2 + (max2 - min2) * ((value - min1) / (max1 - min1))


def SignedDist(pos, normal, p):
    return (
        normal.x * pos.x
        + normal.y * pos.y
        + normal.z * pos.z
        - vector.dotProduct(normal, p)
    )


# TODO: there is way too much going on in this function, needs to be refactored
def TriangleClipped(pos, normal, triangle, outTriangle, clippingDebug=False):
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
        outTriangle[0].color = triangle.color if not clippingDebug else constants.red

        outTriangle[0].vertex1 = insidePoints[0]
        outTriangle[0].vertex2 = vector.PlaneLineIntersection(
            pos, normal, insidePoints[0], outsidePoints[0]
        )
        outTriangle[0].vertex3 = vector.PlaneLineIntersection(
            pos, normal, insidePoints[0], outsidePoints[1]
        )
        return 1

    if insideCount == 2 and outsideCount == 1:
        outTriangle[0].color = triangle.color if not clippingDebug else constants.blue
        outTriangle[1].color = triangle.color if not clippingDebug else constants.green
        outTriangle[0].vertex1 = insidePoints[1]
        outTriangle[0].vertex2 = insidePoints[0]
        outTriangle[0].vertex3 = vector.PlaneLineIntersection(
            pos, normal, insidePoints[0], outsidePoints[0]
        )

        outTriangle[1].vertex1 = insidePoints[1]
        outTriangle[1].vertex2 = outTriangle[0].vertex3
        outTriangle[1].vertex3 = vector.PlaneLineIntersection(
            pos, normal, insidePoints[1], outsidePoints[0]
        )

        return 2


def DrawAxis(
    screen,
    camera,
    scale=3,
    center=None,
    Xaxis=True,
    Yaxis=True,
    Zaxis=True,
    stroke=5,
    alpha=100,
):
    if center is None:
        center = point.Point(vector.Vector3(0, 0, 0))

    X = point.Point(vector.Vector3(scale, 0, 0), (255, 0, 0))
    Y = point.Point(vector.Vector3(0, scale, 0), (0, 255, 0))
    Z = point.Point(vector.Vector3(0, 0, scale), (0, 0, 255))
    origin = center.update(screen, camera)

    if Xaxis:
        x_axis = X.update(screen, camera, True)
        pygame.draw.line(screen, X.color, origin.GetTuple(), x_axis.GetTuple(), stroke)
    if Zaxis:
        z_axis = Z.update(screen, camera, True)
        pygame.draw.line(screen, Z.color, origin.GetTuple(), z_axis.GetTuple(), stroke)
    if Yaxis:
        y_axis = Y.update(screen, camera, True)
        pygame.draw.line(screen, Y.color, origin.GetTuple(), y_axis.GetTuple(), stroke)
