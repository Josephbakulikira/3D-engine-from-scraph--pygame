from utils.matrix import *
from utils.vector import Vector3, crossProduct,dotProduct, Normalize
from utils.triangle import Triangle
from utils.tools import DrawTriangle
from constants import Width, Height, Zoffset

class Mesh:
    def __init__(self):
        self.triangles = []
        self.color = (255, 255, 255)
        self.transform = identity()

    def update(self, camera, light, depth):
        #colors = [(255, 0,0 ), (0, 255, 0), (0, 0, 255), (255,255,0), (0, 255, 255)
        #         ,(255, 0, 255), (0, 255, 0), (0, 0, 255), (255,255,0), (0, 255, 255),
        #          (255, 0, 255),  (0, 255, 0), (0, 0, 255), (255,255,0), (0, 255, 255), (255, 0, 255)]
        tris = []
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

                _light = round(dotProduct(light.direction, normal), 2) if light != None else 1
                projected.color = triangle.Shade(_light)

                # project to 2D screen
                projected.vertex1 = multiplyMatrixVector(transformed.vertex1 , ProjectionMatrix(camera))
                projected.vertex2 = multiplyMatrixVector(transformed.vertex2, ProjectionMatrix(camera))
                projected.vertex3 = multiplyMatrixVector(transformed.vertex3, ProjectionMatrix(camera))

                projected.vertex1 = projected.vertex1 + 1
                projected.vertex2 = projected.vertex2 + 1
                projected.vertex3 = projected.vertex3 + 1

                half_v1 = projected.vertex1 / 2
                half_v2 = projected.vertex2 / 2
                half_v3 = projected.vertex3 / 2

                projected.vertex1 = half_v1 * Vector3(Width, Height, 1)
                projected.vertex2 = half_v2 * Vector3(Width, Height, 1)
                projected.vertex3 = half_v3 * Vector3(Width, Height, 1)
                tris.append(projected)
                #DrawTriangle(screen, projected, Fill, wireframe, wireframeColor)

        return tris
