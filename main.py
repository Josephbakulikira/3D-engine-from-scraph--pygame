# subscribe to my youtube
# https://www.youtube.com/c/Auctux

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
from utils.mesh.point import *
from utils.matrix import *
from utils.tools import *
from utils.world import Scene
from math import pi

screen = pygame.display.set_mode(Size)
clock = pygame.time.Clock()
fps = 60

# mouse setup
pygame.mouse.get_rel()
pygame.mouse.set_visible(True)
a = pygame.event.set_grab(False)

# create mesh
Deer = Mesh()
Deer.triangles = LoadMesh("./assets/deer.obj", (186, 135, 89))

teapot = Mesh()
teapot.triangles = LoadMesh("./assets/utahteapot.obj", (255, 255, 0))

cube = Mesh()
cube.triangles = CubeTriangles((240, 84, 84))
cube.position = Vector3(5, -2, 0)

sphere = Mesh()
sphere.triangles = IcosphereTriangles((246, 131, 15), 2)
sphere.position = Vector3(0, 0, 0)

torus = Mesh()
torus.triangles = LoadMesh("./assets/torus.obj", (56, 147, 147))
torus.position = Vector3(-3, -2, 0)

# create scene and the world
scene = Scene()

# add object you want to display into the world
scene.world.append(torus)
scene.world.append(sphere)
scene.world.append(cube)

# camera setup
camera = Camera(Vector3(0, 0, 0), 0.1, 1000.0, 75.0)
camera.speed = 0.5
camera.rotationSpeed = 0.8

# light setup
light = Light(Vector3(0.9, 0.9, -1))
hue = 0

angle = 0
moveLight = True
run = True
while run:
    screen.fill(BackgroundColor)
    clock.tick(fps)
    dt = clock.tick(fps) / 100
    frameRate = clock.get_fps()
    pygame.display.set_caption(str(frameRate) + " fps")
    camera.HandleInput(dt)
    run = HandleEvent(camera, dt)
    hue = 0

    if moveLight == True and light != None:
        mx, my = pygame.mouse.get_pos()
        _x = translateValue(mx, 0, Width, -1, 1)
        _y = translateValue(my, 0, Height, -1, 1)
        light = Light(Vector3(-_x, -_y, -1))

    # apply the transformation matrix here
    torus.transform = multiplyMatrix(RotationX(angle), ScalingMatrix(1.9))
    cube.transform = multiplyMatrix(RotationY(angle), ScalingMatrix(1.2))
    sphere.transform = multiplyMatrix(
        RotationX(angle), multiplyMatrix(RotationY(angle), ScalingMatrix(1.4))
    )

    # display scene
    scene.update(
        dt=dt,
        camera=camera,
        light=light,
        screen=screen,
        showAxis=True,
        fill=True,
        wireframe=False,
        vertices=False,
        depth=True,
        clippingDebug=True,
        showNormals=False,
        radius=9,
        verticeColor=False,
        wireframeColor=(255, 255, 255),
        ChangingColor=hue,
    )

    pygame.display.flip()
    angle += 0.01

pygame.quit()
sys.exit()
