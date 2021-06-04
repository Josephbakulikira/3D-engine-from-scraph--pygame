import sys
import pygame
from constants import *
from event import HandleEvent

from utils.vector import Vector3
from utils.camera import Camera
from utils.light import Light
from utils.mesh.base import Mesh
from utils.mesh.meshes import *
from utils.matrix import *
from utils.tools import *
from utils.world import Scene
from math import pi

screen = pygame.display.set_mode(Size)
clock = pygame.time.Clock()
fps = 60

cube = Mesh()
cube.triangles = CubeTriangles((255, 23, 41))

plane = Mesh()
plane.triangles = PlaneTriangles((255, 251, 123), 10)

scene = Scene()
#add object into the world
scene.world.append(plane)

camera = Camera(Vector3(0, 0, 0),0.1, 1000.0, 90.0)
light = Light(Vector3(0, 0, -1))


angle = 0

run = True
while run:
    screen.fill(BackgroundColor)
    clock.tick(fps)
    frameRate = clock.get_fps()
    pygame.display.set_caption(str(frameRate) + " fps")

    run = HandleEvent()
    plane.transform = matrix_multiplication(RotationX(angle), ScalingMatrix(3))
    #cone.transform =  matrix_multiplication(RotationX(angle), RotationY(angle))
    #cube.transform = matrix_multiplication( matrix_multiplication(RotationX(angle), ScalingMatrix(2)), RotationY(angle) )
    # Deer.transform = translateMatrix( Vector3(0, 0, -1) )
    scene.update(camera=camera, light=light, screen=screen, fill=False, wireframe=True, vertices=True, depth=False, radius=5, verticeColor=False)

    pygame.display.flip()
    angle += 0.01

pygame.quit()
sys.exit()
