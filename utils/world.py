from utils.tools import *

class Scene:
    def __init__(self, world=[]):
        self.world = world

    def update(self, dt, camera, light, screen,
               fill=True, wireframe=False, vertices=False, depth=True,showNormals=False,
               radius=8, verticeColor=False,
               wireframeColor=(255, 255, 255), lineWidth=1):
        triangles = []
        normals = []
        origins = []
        for ob in self.world:
            tris, nors = ob.update(screen,fill, wireframe, dt, camera, light, depth)
            triangles += tris
            normals += nors

        def Zsort(val):
            return (val.vertex1.z + val.vertex2.z + val.vertex3.z) / 3.0

        # print()
        triangles.sort(key=Zsort)
        for projected in triangles:
            origin = (projected.vertex1+projected.vertex2+projected.vertex3)/3
            DrawTriangle(screen, projected, fill, wireframe,vertices, radius, verticeColor, wireframeColor, lineWidth)
            origins.append(origin)

        if showNormals == True:
            for i,n in enumerate(normals):
                dest = origins[i]- (n * 50)
                pygame.draw.line(screen, (0, 255, 0), origins[i].GetTuple(), dest.GetTuple(), 2)
