import sys
import pygame
from constants import *
from event import HandleEvent
from utils.transform import *
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

#mouse setup
pygame.mouse.get_rel()
pygame.mouse.set_visible(True)
a = pygame.event.set_grab(False)

cube = Mesh()
cube.triangles = CubeTriangles((255, 23, 41))

plane = Mesh()
plane.triangles = PlaneTriangles((255, 251, 123), 10)

teapot = Mesh()
teapot.triangles = LoadMesh("./assets/utahteapot.obj", (41, 120, 142))

Deer = Mesh()
Deer.triangles = LoadMesh("./assets/deer.obj", (42, 233, 42))

scene = Scene()
#add object into the world
scene.world.append(plane)

#camera setup
camera = Camera(Vector3(0, 1, 0),0.1, 1000.0, 90.0)
camera.speed = 0.5
camera.rotationSpeed = 0.8
#light setup
light = Light(Vector3(0, 1, -1))

angle = 0

run = True
while run:
    screen.fill(BackgroundColor)
    clock.tick(fps)
    dt = clock.tick(fps)/100
    frameRate = clock.get_fps()
    pygame.display.set_caption(str(frameRate) + " fps")

    run = HandleEvent(camera, dt)
    #Deer.transform = RotationX(pi)
    plane.transform = multiplyMatrix(RotationX(-pi), RotationY(pi/2))
    #plane.transform = multiplyMatrix(translateMatrix(Vector3(0, 10, 0)), RotationX(angle))
    #cone.transform =  multiplyMatrix(RotationX(angle), RotationY(angle))
    cube.transform = multiplyMatrix( multiplyMatrix(RotationX(angle), ScalingMatrix(2)), RotationY(angle) )
    # Deer.transform = multiplyMatrix( Vector3(0, 0, -1) )
    scene.update(dt = dt, camera=camera, light=light, screen=screen, fill=True, wireframe=True, vertices=False, depth=True, radius=5, verticeColor=False)

    pygame.display.flip()
    angle += 0.01

pygame.quit()
sys.exit()
