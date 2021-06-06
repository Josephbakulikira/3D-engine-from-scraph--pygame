from math import tan, pi
from constants import *
from utils.vector import *
from utils.transform import *
from utils.matrix import *
import pygame

def cameraRotation(vec):
    return multiplyMatrix(RotationX(vec.x), RotationY(vec.y))

class Camera:
    def __init__(self, position, near, far, fov):
        self.position = position
        self.near = near
        self.far = far
        self.fov = fov
        self.yaw = 0
        self.phi = 0
        self.tangent = 1.0 / tan(self.fov * 0.5 / 180 * pi)
        self.direction = Vector3()
        self.up = Vector3()
        self.transform = identityMatrix()
        self.rotation = cameraRotation(Vector2(self.yaw, self.phi))
        self.target = position
        self.speed = 0.1
        self.rotationSpeed = 1.5
        self.temp = Vector3()

    def HandleInput(self, dt):
        keys = pygame.key.get_pressed()
        delta = self.speed * dt

        if keys[pygame.K_UP]:
            self.position.y += delta
        if keys[pygame.K_DOWN]:
            self.position.y -= delta
        if keys[pygame.K_RIGHT]:
            self.position.x -= delta
        if keys[pygame.K_LEFT]:
            self.position.x += delta

        self.temp = self.target * delta

        if keys[pygame.K_w]: #zoom in
            self.position += self.temp
        if keys[pygame.K_s]: #zoom out
            self.position -= self.temp
        if keys[pygame.K_a]:
            self.yaw -= 0.04
        if keys[pygame.K_d]:
            self.yaw += 0.04

    def HandleMouseEvent(self, x, y, deltaTime):
        # not finished
        self.yaw += x
