# subscribe to my youtube
# https://www.youtube.com/c/Auctux

import sys
import pygame
import constants
from event import HandleEvent
import utils.transform as transform
from utils.vector import Vector3
from utils.camera import Camera
from utils.light import Light
from utils.mesh.base import Mesh
import utils.mesh.meshes as meshes
import utils.mesh.spheres as spheres
import utils.tools as tools
from utils.world import Scene

screen = pygame.display.set_mode(constants.Size)
clock = pygame.time.Clock()
fps = 60

# mouse setup
pygame.mouse.get_rel()
pygame.mouse.set_visible(True)

# create mesh
Deer = Mesh.from_file("./assets/deer.obj", (186, 135, 89))
teapot = Mesh.from_file("./assets/utahteapot.obj", (255, 255, 0))
cube = Mesh.cube((240, 84, 84), Vector3(5, -2, 0))
sphere = Mesh.icosphere((246, 131, 15), 2)
torus = Mesh.from_file("./assets/torus.obj", (56, 147, 147), Vector3(-3, -2, 0))

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
    screen.fill(constants.BackgroundColor)
    clock.tick(fps)
    dt = clock.tick(fps) / 100
    frameRate = clock.get_fps()
    pygame.display.set_caption(str(frameRate) + " fps")
    camera.HandleInput(dt)
    run = HandleEvent(camera, dt)
    hue = 0

    if moveLight and light is not None:
        mx, my = pygame.mouse.get_pos()
        _x = tools.translateValue(mx, 0, constants.Width, -1, 1)
        _y = tools.translateValue(my, 0, constants.Height, -1, 1)
        light = Light(Vector3(-_x, -_y, -1))

    # apply the transformation matrix here
    torus.transform = transform.RotationX(angle) @ transform.ScalingMatrix(1.9)
    cube.transform = transform.RotationY(angle) @ transform.ScalingMatrix(1.2)
    sphere.transform = transform.RotationX(angle) @ (
        transform.RotationY(angle) @ transform.ScalingMatrix(1.4)
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
