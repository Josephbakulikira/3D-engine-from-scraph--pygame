from utils.matrix import *
from utils.transform import *
from utils.vector import Vector3, crossProduct,dotProduct, Normalize
from utils.triangle import Triangle
from utils.tools import DrawTriangle, TriangleClipped
from constants import Width, Height, Zoffset, clipping
import pygame
class Mesh:
    def __init__(self):
        self.triangles = []
        self.color = (255, 255, 255)
        self.transform = identityMatrix()

    def update(self,screen,fill, wireframe, dt, camera, light, depth):
        tris = []
        camera.HandleInput(dt)

        camera.direction = Vector3(0, 0, 1)
        camera.up = Vector3(0, 1, 0)
        camera.target = Vector3(0, 0, 1)
        camera.rotation = RotationY(camera.yaw)
        camera.direction = multiplyMatrixVector(camera.target , camera.rotation)
        camera.target = camera.position + camera.direction
        lookAtMatrix = PointAt(camera.position, camera.target, camera.up)
        camera.viewMatrix = QuickInverse(lookAtMatrix)
        camera.target= Vector3(0, 0, 1)

        for index, triangle in enumerate(self.triangles):
            projected = Triangle()
            projected.verticeColor = triangle.verticeColor
            transformed = Triangle()

            transformed.vertex1 = multiplyMatrixVector(triangle.vertex1 , self.transform)
            transformed.vertex2 = multiplyMatrixVector(triangle.vertex2 , self.transform)
            transformed.vertex3 = multiplyMatrixVector(triangle.vertex3 , self.transform)

            transformed.vertex1 = transformed.vertex1 + Vector3(0, 0, Zoffset)
            transformed.vertex2 = transformed.vertex2 + Vector3(0, 0, Zoffset)
            transformed.vertex3 = transformed.vertex3 + Vector3(0, 0, Zoffset)

            # get the normal vector
            line1 = transformed.vertex2 - transformed.vertex1
            line2 = transformed.vertex3 - transformed.vertex1
            normal = Normalize( crossProduct(line1, line2) )

            temp = transformed.vertex1 - camera.position

            d = dotProduct( temp, normal)
            if d < 0.0 or depth == False:
                # directional light -> illumination

                _light = max(0.01, dotProduct(light.direction, normal) ) if light != None else 1
                transformed.color = triangle.Shade(_light)

                transformed.vertex1 = multiplyMatrixVector(transformed.vertex1, camera.viewMatrix )
                transformed.vertex2 = multiplyMatrixVector(transformed.vertex2, camera.viewMatrix )
                transformed.vertex3 = multiplyMatrixVector(transformed.vertex3, camera.viewMatrix )

                clipped = 0
                clippedTriangles = [Triangle() for _ in range(2)]
                clipped = TriangleClipped(Vector3(0, 0, clipping), Vector3(0, 0, 1), transformed, clippedTriangles)

                for i in range(clipped):
                    #print(clippedTriangles)
                    # project to 2D screen
                    projected.vertex1 = multiplyMatrixVector(clippedTriangles[i].vertex1, ProjectionMatrix(camera))
                    projected.vertex2 = multiplyMatrixVector(clippedTriangles[i].vertex2, ProjectionMatrix(camera))
                    projected.vertex3 = multiplyMatrixVector(clippedTriangles[i].vertex3, ProjectionMatrix(camera))

                    projected.color = clippedTriangles[i].color
                    offsetView = Vector3(1, 1, 0)
                    projected.vertex1 = projected.vertex1 + offsetView
                    projected.vertex2 = projected.vertex2 + offsetView
                    projected.vertex3 = projected.vertex3 + offsetView

                    half_v1 = projected.vertex1 / 2
                    half_v2 = projected.vertex2 / 2
                    half_v3 = projected.vertex3 / 2

                    projected.vertex1 = half_v1 * Vector3(Width, Height, 1)
                    projected.vertex2 = half_v2 * Vector3(Width, Height, 1)
                    projected.vertex3 = half_v3 * Vector3(Width, Height, 1)
                    # if i == 0:
                    #     pygame.draw.line(screen, projected.color, projected.vertex1.GetTuple(), projected.vertex2.GetTuple(), 4)
                    #     pygame.draw.line(screen, projected.color, projected.vertex2.GetTuple(), projected.vertex3.GetTuple(), 4)
                    #     pygame.draw.line(screen, projected.color, projected.vertex3.GetTuple(), projected.vertex1.GetTuple(), 4)
                    #     pygame.draw.polygon(screen, projected.color, projected.GetPolygons())
                    if i == 0 and fill==True:
                        # have to fix this part
                        pygame.draw.polygon(screen, projected.color, projected.GetPolygons())
                    tris.append(projected)
                    #DrawTriangle(screen, projected, Fill, wireframe, wireframeColor)

        return tris
