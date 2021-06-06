from utils.tools import *

class Scene:
    def __init__(self, world=[]):
        self.world = world

    def update(self, dt, camera, light, screen,
               fill=True, wireframe=False, vertices=False, depth=True,
               radius=8, verticeColor=False,
               wireframeColor=(255, 255, 255), lineWidth=1, ):
        triangles = []
        for ob in self.world:
            triangles += ob.update(dt, camera, light, depth)


        def Zsort(val):
            return (val.vertex1.z + val.vertex2.z + val.vertex3.z) / 3.0

        # print()
        triangles.sort(key=Zsort)
        for projected in triangles:
            DrawTriangle(screen, projected, fill, wireframe,vertices, radius, verticeColor, wireframeColor, lineWidth)
