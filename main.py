import pygame
from constants import *
from event import HandleEvent

from utils.vector import Vector3
from utils.camera import Camera
from utils.light import Light
from utils.mesh.base import Mesh
from utils.mesh.meshes import CubeTriangles
from utils.matrix import *

screen = pygame.display.set_mode(Size)
clock = pygame.time.Clock()
fps = 60

cube = Mesh()
cube.color = (222, 182, 25)
cube.triangles = CubeTriangles(cube.color)

# cube2 = Mesh()
# cube2.color = (12, 42, 255)
# cube2.triangles = CubeTriangles(cube2.color)
# cube2.transform = translateMatrix(Vector3(2, 5, 0))

camera = Camera(Vector3(0, 0, 0),0.1, 1000.0, 90.0)
light = Light(Vector3(0, 0, -1))

angle = 0

run = True
while run:
    screen.fill(BackgroundColor)
    clock.tick(fps)
    run = HandleEvent()

    cube.transform = matrix_multiplication(RotationY(angle), matrix_multiplication(RotationX(angle), RotationZ(angle)))
    cube.update(camera, light, screen, True, False)

    #cube2.update(camera, light, screen, True, True)
    pygame.display.flip()
    angle += 0.01
pygame.quit()
