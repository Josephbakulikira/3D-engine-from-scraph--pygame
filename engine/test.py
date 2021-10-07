# subscribe to my youtube
# https://www.youtube.com/c/Auctux
import sys
import pygame
from pygame.locals import *
from constants import *
from event import HandleEvent
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
from random import randint
pygame.init()
# screen = pygame.display.set_mode(Size)
flags = DOUBLEBUF
screen = pygame.display.set_mode(Size, flags, 16)
clock = pygame.time.Clock()
fps = 60
#mouse setup
pygame.mouse.get_rel()
pygame.mouse.set_visible(True)
a = pygame.event.set_grab(False)

# create scene and the world
res = 3
scene = Scene()

for x in range(res):
    for y in range(res):
        for z in range(res):
            cube = Mesh()
            s = 5
            r = randint(10, 255)
            g = randint(10, 255)
            b = randint(10, 255)
            cube.triangles = CubeTriangles((r, g, b),Vector3(x * s, y * s, z * s), s)
            cube.position = Vector3(x * s, y * s, z * s)
            cube.transform = Matrix.scaling(0.1)
            scene.world.append(cube)

#camera setup
camera = Camera(Vector3(0, 0, 0), 0.1, 1000.0, 75.0)
camera.speed = 0.5
camera.rotationSpeed = 0.8

#light setup
light = Light(Vector3(0.9, 0.9, -1))
hue = 0

angle = 0
moveLight = True
run = True

while run:
    screen.fill(BackgroundColor)
    clock.tick(fps)
    dt = clock.tick(fps)/100
    frameRate = clock.get_fps()
    pygame.display.set_caption(str(frameRate) + " fps")
    run = HandleEvent(camera, dt)
    hue = 0
    # handle input
    camera.HandleInput(dt)

    if moveLight == True and light != None:
        mx, my = pygame.mouse.get_pos()
        _x = translateValue( mx, 0,  Width,  -1,  1)
        _y = translateValue( my, 0, Height, -1, 1)
        light = Light(Vector3(-_x, -_y, -1))

    # apply the transformation matrix here
    # torus.transform = Matrix.rotation_x(angle) @ Matrix.scaling(1.9)
    # cube.transform = Matrix.rotation_y(angle) @ Matrix.scaling(1.2)
    # sphere.transform = Matrix.rotation_x(angle) @ (
    #     Matrix.rotation_y(angle) @ Matrix.scaling(1.4)
    # )

    # display scene
    scene.update(
        dt = dt,
        camera=camera,
        light=light,
        screen=screen,
        showAxis=True,
        fill=True,
        wireframe=True,
        vertices=True,
        depth=True,
        clippingDebug=False,
        showNormals=False,
        radius=2,
        verticeColor=False,
        wireframeColor=(255, 255, 255),
        ChangingColor=hue)


    pygame.display.flip()
    angle += 0.01

pygame.quit()
sys.exit()
