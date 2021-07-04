from __future__ import annotations
from typing import Optional
from os import PathLike
import pygame
import utils.matrix as matrix
import utils.transform as transform
from utils.vector import Vector3
from utils.triangle import Triangle
from utils.tools import TriangleClipped, hsv_to_rgb, LoadMesh
from constants import Width, Height, Zoffset, clipping, dim
import utils.mesh.meshes as meshes
import utils.mesh.spheres as spheres


class Mesh:
    def __init__(self, triangles: list[Triangle], position: Optional[Vector3] = None):
        self.triangles = triangles
        self.position = position if position is not None else Vector3()
        self.color = (255, 255, 255)
        self.transform = transform.identityMatrix()
        self.translate = transform.identityMatrix()

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
        cls, color: tuple[int, int, int], position: Optional[Vector3] = None
    ) -> Mesh:
        tris = meshes.CubeTriangles(color)
        return cls(tris, position)

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

        for index, triangle in enumerate(self.triangles):
            projected = Triangle()
            projected.verticeColor = triangle.verticeColor
            transformed = Triangle()

            transformed.vertex1 = matrix.multiplyMatrixVector(
                triangle.vertex1 + self.position, self.transform
            )
            transformed.vertex2 = matrix.multiplyMatrixVector(
                triangle.vertex2 + self.position, self.transform
            )
            transformed.vertex3 = matrix.multiplyMatrixVector(
                triangle.vertex3 + self.position, self.transform
            )

            transformed.vertex1 += Vector3(0, 0, Zoffset)
            transformed.vertex2 += Vector3(0, 0, Zoffset)
            transformed.vertex3 += Vector3(0, 0, Zoffset)

            # get the normal vector
            line1 = transformed.vertex2 - transformed.vertex1
            line2 = transformed.vertex3 - transformed.vertex1
            normal = line1.cross(line2).norm()

            temp = transformed.vertex1 - camera.position
            d = temp.dot(normal)
            if d < 0.0 or not depth:
                if hue != 0:
                    triangle.color = hsv_to_rgb(hue, 1, 1)

                # directional light -> illumination
                _light = (
                    max(dim, light.direction.dot(normal)) if light is not None else 1
                )
                transformed.color = triangle.Shade(_light)

                transformed.vertex1 = matrix.multiplyMatrixVector(
                    transformed.vertex1, camera.viewMatrix
                )
                transformed.vertex2 = matrix.multiplyMatrixVector(
                    transformed.vertex2, camera.viewMatrix
                )
                transformed.vertex3 = matrix.multiplyMatrixVector(
                    transformed.vertex3, camera.viewMatrix
                )

                clipped = 0
                clippedTriangles = [Triangle() for _ in range(2)]
                clipped = TriangleClipped(
                    Vector3(0, 0, clipping),
                    Vector3(0, 0, 1),
                    transformed,
                    clippedTriangles,
                    clippingDebug,
                )

                for i in range(clipped):
                    # project to 2D screen
                    projected.vertex1 = matrix.multiplyMatrixVector(
                        clippedTriangles[i].vertex1, camera.projection()
                    )
                    projected.vertex2 = matrix.multiplyMatrixVector(
                        clippedTriangles[i].vertex2, camera.projection()
                    )
                    projected.vertex3 = matrix.multiplyMatrixVector(
                        clippedTriangles[i].vertex3, camera.projection()
                    )

                    projected.color = clippedTriangles[i].color
                    # fix the inverted x
                    projected.vertex1 *= Vector3(1, -1, 1)
                    projected.vertex2 *= Vector3(1, -1, 1)
                    projected.vertex3 *= Vector3(1, -1, 1)

                    offsetView = Vector3(1, 1, 0)
                    projected.vertex1 = projected.vertex1 + offsetView
                    projected.vertex2 = projected.vertex2 + offsetView
                    projected.vertex3 = projected.vertex3 + offsetView

                    projected.vertex1 *= Vector3(Width, Height, 1) * 0.5
                    projected.vertex2 *= Vector3(Width, Height, 1) * 0.5
                    projected.vertex3 *= Vector3(Width, Height, 1) * 0.5
                    if not i and wireframe:
                        pygame.draw.line(
                            screen,
                            (255, 255, 255),
                            projected.vertex1.GetTuple(),
                            projected.vertex2.GetTuple(),
                            1,
                        )
                        pygame.draw.line(
                            screen,
                            (255, 255, 255),
                            projected.vertex2.GetTuple(),
                            projected.vertex3.GetTuple(),
                            1,
                        )
                        pygame.draw.line(
                            screen,
                            (255, 255, 255),
                            projected.vertex3.GetTuple(),
                            projected.vertex1.GetTuple(),
                            1,
                        )
                    if not i and fill:
                        # have to fix this part
                        pygame.draw.polygon(
                            screen, projected.color, projected.GetPolygons()
                        )

                    tris.append(projected)

        return tris
