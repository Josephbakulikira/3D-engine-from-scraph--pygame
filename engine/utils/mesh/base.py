from __future__ import annotations
from typing import Optional
from os import PathLike
import pygame
import utils.matrix as matrix
from utils.vector import Vector3, Normalize, dotProduct, crossProduct
from utils.triangle import Triangle
from utils.tools import DrawTriangle, TriangleClipped, hsv2rgb
from constants import Width, Height, Zoffset, clipping, dim
import pygame

class Mesh:
    def __init__(self, position=Vector3(), scale=1):
        self.triangles = []
        self.position = position
        self.color = (255, 255, 255)
        self.transform = matrix.Matrix.identity()
        self.translate = matrix.Matrix.identity()
        self.scale = scale
    @classmethod
    def from_file(
        cls,
        fname: PathLike,
        color: tuple[int, int, int],
        position: Optional[Vector3] = None,
    ) -> Mesh:
        triangles = LoadMesh(fname, color)
        return cls(triangles, position)

    @classmethod
    def cube(
        cls, color: tuple[int, int, int], position: Optional[Vector3] = None, scale: optional[float] = 1
    ) -> Mesh:
        print(scale)
        tris = meshes.CubeTriangles(size, color)
        return cls(tris, position, scale)

    @classmethod
    def icosphere(
        cls,
        color: tuple[int, int, int],
        subdivision=0,
        radius=1,
        position: Optional[Vector3] = None,
    ) -> Mesh:
        tris = spheres.IcosphereTriangles(color, subdivision, radius)
        return cls(tris, position)

    # TODO: refactor this method, its way too long
    def update(
        self, screen, fill, wireframe, dt, camera, light, depth, clippingDebug, hue=0
    ):
        tris = []
        normals = []

        for index, triangle in enumerate(self.triangles):
            projected = Triangle()
            projected.verticeColor = triangle.verticeColor
            transformed = Triangle()

            transformed.vertex1 = matrix.multiplyMatrixVector(triangle.vertex1+self.position , self.transform)
            transformed.vertex2 = matrix.multiplyMatrixVector(triangle.vertex2+self.position , self.transform)
            transformed.vertex3 = matrix.multiplyMatrixVector(triangle.vertex3+self.position , self.transform)

            transformed.vertex1 += Vector3(0, 0, Zoffset)
            transformed.vertex2 += Vector3(0, 0, Zoffset)
            transformed.vertex3 += Vector3(0, 0, Zoffset)

            # get the normal vector
            line1 = transformed.vertex2 - transformed.vertex1
            line2 = transformed.vertex3 - transformed.vertex1
            normal = Normalize( crossProduct(line1, line2) )

            temp = transformed.vertex1 - camera.position
            d = dotProduct( temp, normal)
            if d < 0.0 or depth == False:
                if hue != 0:
                    triangle.color = hsv2rgb(hue, 1, 1)

                # print(normal)

                # directional light -> illumination
                # dim = 0.0001
                _light = max(dim, dotProduct(light.direction, normal) ) if light != None else 1
                transformed.color = triangle.Shade(_light)

                transformed.vertex1 = matrix.multiplyMatrixVector(transformed.vertex1, camera.viewMatrix )
                transformed.vertex2 = matrix.multiplyMatrixVector(transformed.vertex2, camera.viewMatrix )
                transformed.vertex3 = matrix.multiplyMatrixVector(transformed.vertex3, camera.viewMatrix )

                clipped = 0
                clippedTriangles = [Triangle() for _ in range(2)]
                clipped = TriangleClipped(Vector3(0, 0, clipping), Vector3(0, 0, 1), transformed, clippedTriangles, clippingDebug)

                for i in range(clipped):
                    #print(clippedTriangles)
                    # project to 2D screen
                    projected.vertex1 = matrix.multiplyMatrixVector(clippedTriangles[i].vertex1, camera.projection())
                    projected.vertex2 = matrix.multiplyMatrixVector(clippedTriangles[i].vertex2, camera.projection())
                    projected.vertex3 = matrix.multiplyMatrixVector(clippedTriangles[i].vertex3, camera.projection())


                    projected.color = clippedTriangles[i].color
                    # fix the inverted x
                    projected.vertex1 *= Vector3(1, -1, 1)
                    projected.vertex2 *= Vector3(1, -1, 1)
                    projected.vertex3 *= Vector3(1, -1, 1)

                    offsetView = Vector3(1, 1, 0)
                    projected.vertex1 = projected.vertex1 + offsetView
                    projected.vertex2 = projected.vertex2 + offsetView
                    projected.vertex3 = projected.vertex3 + offsetView

                    # half_v1 = projected.vertex1 / 2
                    # half_v2 = projected.vertex2 / 2
                    # half_v3 = projected.vertex3 / 2

                    projected.vertex1 *= Vector3(Width, Height, 1) * 0.5
                    projected.vertex2 *= Vector3(Width, Height, 1) * 0.5
                    projected.vertex3 *= Vector3(Width, Height, 1) * 0.5
                    if i == 0 and wireframe == True:
                        pygame.draw.line(screen, (255, 255,255), projected.vertex1.GetTuple(), projected.vertex2.GetTuple(), 1)
                        pygame.draw.line(screen, (255, 255,255), projected.vertex2.GetTuple(), projected.vertex3.GetTuple(), 1)
                        pygame.draw.line(screen, (255, 255,255), projected.vertex3.GetTuple(), projected.vertex1.GetTuple(), 1)
                        #pygame.draw.polygon(screen, projected.color, projected.GetPolygons())
                    if i == 0 and fill==True:
                        # have to fix this part
                        pygame.draw.polygon(screen, projected.color, projected.GetPolygons())

                    tris.append(projected)
                    #DrawTriangle(screen, projected, Fill, wireframe, wireframeColor)

        return tris
