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

#mouse setup
pygame.mouse.get_rel()
pygame.mouse.set_visible(True)
a = pygame.event.set_grab(False)

Deer = Mesh()
Deer.triangles = LoadMesh("./assets/deer.obj",(186, 135, 89))

teapot = Mesh()
teapot.triangles = LoadMesh("./assets/utahteapot.obj", (255, 255, 0))

cube = Mesh()
cube.triangles = CubeTriangles((240,84,84))
cube.position = Vector3(3, 2, 0)

sphere = Mesh()
sphere.triangles = IcosphereTriangles((246,131,15), 2)
sphere.position = Vector3(4.3, 0, 0)

torus = Mesh()
torus.triangles = LoadMesh("./assets/torus.obj", (56,147,147))
torus.position = Vector3(-1, 0, 0)
# sphere2 = Mesh()
# sphere2.triangles = SphereTriangles((255, 255, 255), 20)

scene = Scene()
#add object into the world
scene.world.append(torus)
scene.world.append(sphere)
scene.world.append(cube)
#scene.world.append(teapot)
#scene.world.append(Deer)



#camera setup
camera = Camera(Vector3(0, 1, 0), 0.1, 1000.0, 75.0)
camera.speed = 0.5
camera.rotationSpeed = 0.8

#light setup
light = Light(Vector3(0.9, 0.9, -1))

angle = 0

moveLight = True

run = True
while run:
    screen.fill(BackgroundColor)
    clock.tick(fps)
    dt = clock.tick(fps)/100
    frameRate = clock.get_fps()
    pygame.display.set_caption(str(frameRate) + " fps")
    camera.HandleInput(dt)
    run = HandleEvent(camera, dt)


    if moveLight == True and light != None:
        mx, my = pygame.mouse.get_pos()
        _x = translateValue( mx, 0,  Width,  -1,  1)
        _y = translateValue( my, 0, Height, -1, 1)
        light = Light(Vector3(-_x, -_y, -1))


    #Deer.transform = RotationY(angle)
    #teapot.transform = RotationY(angle)
    torus.transform = multiplyMatrix(RotationX(angle), ScalingMatrix(1.9))
    cube.transform = RotationY(angle)
    sphere.transform = RotationX(angle)

    # display scene
    scene.update(dt = dt, camera=camera, light=light, screen=screen, showAxis=False,
                fill=True, wireframe=False, vertices=False, depth=True, clippingDebug=False,
                showNormals=False, radius=8, verticeColor=False, wireframeColor=(255, 255, 255))
    #p.position.x += angle/10
    pygame.display.flip()
    angle += 0.01

pygame.quit()
sys.exit()
