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
from utils.mesh.spheres import *
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

Deer = Mesh()
Deer.triangles = LoadMesh("./assets/deer.obj",(186, 135, 89))

cube = Mesh()
cube.triangles = CubeTriangles((0, 142, 123))

sphere = Mesh()
sphere.triangles = IcosphereTriangles((23, 123, 213), 2)

sphere2 = Mesh()
sphere2.triangles = SphereTriangles((255, 255, 255), 20)

scene = Scene()
#add object into the world
scene.world.append(sphere)

#camera setup
camera = Camera(Vector3(0, 0, 0),0.1, 1000.0, 90.0)
camera.speed = 0.5
camera.rotationSpeed = 0.8
#light setup
light = Light(Vector3(0, 0, -1))

angle = 0

run = True
while run:
    screen.fill(BackgroundColor)
    clock.tick(fps)
    dt = clock.tick(fps)/100
    frameRate = clock.get_fps()
    pygame.display.set_caption(str(frameRate) + " fps")

    run = HandleEvent(camera, dt)

    sphere.transform = multiplyMatrix(multiplyMatrix(RotationY(angle), ScalingMatrix(4)), RotationX(angle))

    # display scene
    scene.update(dt = dt, camera=camera, light=light, screen=screen,
                fill=True, wireframe=False, vertices=False, depth=True,
                showNormals=False, radius=8, verticeColor=False, wireframeColor=(0, 223,255))

    pygame.display.flip()
    angle += 0.01

pygame.quit()
sys.exit()
