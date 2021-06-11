from utils.tools import *
from utils.vector import *
class Scene:
    def __init__(self, world=[]):
        self.world = world

    def update(self, dt, camera, light, screen,
               fill=True, wireframe=False, vertices=False, depth=True,showNormals=False,
               radius=8, verticeColor=False,
               wireframeColor=(255, 255, 255), lineWidth=1):
        triangles = []
        origins = []
        for ob in self.world:
            triangles += ob.update(screen,fill, wireframe, dt, camera, light, depth)

        def Zsort(val):
            return (val.vertex1.z + val.vertex2.z + val.vertex3.z) / 3.0

        triangles.sort(key=Zsort)
        normals_length = 80
        normals = []
        for projected in triangles:
            origin = (projected.vertex1+projected.vertex2+projected.vertex3)/3

            line1 = projected.vertex2 - projected.vertex1
            line2 = projected.vertex3 - projected.vertex1
            normal = crossProduct(line1, line2) * normals_length
            DrawTriangle(screen, projected, fill, wireframe,vertices, radius, verticeColor, wireframeColor, lineWidth)
            origins.append(origin)
            normals.append(normal)

        if showNormals == True: #---to fix later
            # get the normal vector
            for i, n in enumerate(normals):
                endPoint = origins[i] + (n)
                #pygame.draw.circle(screen, (0,255, 0), endPoint.GetTuple(), 10)
                pygame.draw.line(screen, (0, 255, 0), origins[i].GetTuple(), endPoint.GetTuple(), 2)
