import utils.tools as tools
import utils.vector as vector
import utils.transform as transform
import utils.matrix as matrix
import pygame


class Scene:
    def __init__(self, world=[]):
        self.world = world

    def update(
        self,
        dt,
        camera,
        light,
        screen,
        showAxis=False,
        fill=True,
        wireframe=False,
        vertices=False,
        depth=True,
        clippingDebug=False,
        showNormals=False,
        radius=8,
        verticeColor=False,
        wireframeColor=(255, 255, 255),
        ChangingColor=0,
        lineWidth=1,
    ):
        camera.HandleInput(dt)

        camera.direction = vector.Vector3(0, 0, 1)
        camera.up = vector.Vector3(0, 1, 0)
        camera.target = vector.Vector3(0, 0, 1)
        camera.rotation = transform.RotationY(camera.yaw)
        camera.direction = matrix.multiplyMatrixVector(camera.target, camera.rotation)
        camera.target = camera.position + camera.direction
        lookAtMatrix = transform.PointAt(camera.position, camera.target, camera.up)
        camera.viewMatrix = matrix.QuickInverse(lookAtMatrix)
        camera.target = vector.Vector3(0, 0, 1)

        triangles = []
        origins = []
        for ob in self.world:
            triangles += ob.update(
                screen,
                fill,
                wireframe,
                dt,
                camera,
                light,
                depth,
                clippingDebug,
                ChangingColor,
            )

        def Zsort(val):
            return (val.vertex1.z + val.vertex2.z + val.vertex3.z) / 3.0

        triangles.sort(key=Zsort)
        normals_length = 250
        normals = []

        for projected in reversed(triangles):
            origin = (projected.vertex1 + projected.vertex2 + projected.vertex3) / 3
            line1 = projected.vertex2 - projected.vertex1
            line2 = projected.vertex3 - projected.vertex1
            normal = line1.cross(line2) * normals_length
            tools.DrawTriangle(
                screen,
                projected,
                fill,
                wireframe,
                vertices,
                radius,
                verticeColor,
                wireframeColor,
                lineWidth,
            )
            origins.append(origin)
            normals.append(normal)

        if showAxis:
            tools.DrawAxis(screen, camera)

        if showNormals:  # ---to fix later
            # get the normal vector
            for i, n in enumerate(normals):
                endPoint = origins[i] + (n)
                # pygame.draw.circle(screen, (0,255, 0), endPoint.GetTuple(), 10)
                pygame.draw.line(
                    screen, (0, 255, 0), origins[i].GetTuple(), endPoint.GetTuple(), 2
                )
