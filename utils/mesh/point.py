from utils.matrix import *
from utils.transform import *
from utils.vector import Vector3, crossProduct,dotProduct, Normalize
from constants import Width, Height, Zoffset, clipping
import pygame
import utils.matrix as matrix
from utils.vector import Vector3
from constants import Width, Height, Zoffset
from utils.camera import Camera


class Point:
    def __init__(self, position=Vector3(), color=(255, 255, 255), radius=10):
        self.position = position
        self.color = color
        self.radius = radius
        self.transform = matrix.Matrix.identity()

    def update(self,screen, camera,showPoint=False):

        projected = None
        transformed = None
        transformed = multiplyMatrixVector(self.position, self.transform)
        transformed += Vector3(0, 0, Zoffset)
        transformed = multiplyMatrixVector(transformed, camera.viewMatrix)
        projected = multiplyMatrixVector(transformed, camera.projection())
        projected *= Vector3(-1, -1, 1)

        offsetView = Vector3(1, 1, 0)
        projected = projected + offsetView
        projected *= Vector3(Width, Height, 1) * 0.5
        if showPoint:
            pygame.draw.circle(screen,self.color, projected.GetTuple(), self.radius)
        return projected
