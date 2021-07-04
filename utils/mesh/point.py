from utils.matrix import *
from utils.transform import *
from utils.vector import Vector3, crossProduct,dotProduct, Normalize
from constants import Width, Height, Zoffset, clipping
import pygame
<<<<<<< HEAD
=======
import utils.matrix as matrix
from utils.vector import Vector3
from constants import Width, Height, Zoffset
from utils.camera import Camera

>>>>>>> 4f9de1a37b8d2bf9ad6687ebf21a62e1384b3ede

class Point:
    def __init__(self, position=Vector3(), color=(255, 255, 255), radius=10):
        self.position = position
        self.color = color
<<<<<<< HEAD
        self.radius =radius
        self.transform = identityMatrix()
=======
        self.radius = radius
        self.transform = matrix.Matrix.identity()
>>>>>>> 4f9de1a37b8d2bf9ad6687ebf21a62e1384b3ede

    def update(self,screen, camera,showPoint=False):

        projected = None
        transformed = None
        transformed = multiplyMatrixVector(self.position, self.transform)
        transformed += Vector3(0, 0, Zoffset)
        transformed = multiplyMatrixVector(transformed, camera.viewMatrix)
        projected = multiplyMatrixVector(transformed, ProjectionMatrix(camera))
        projected *= Vector3(-1, -1, 1)

        offsetView = Vector3(1, 1, 0)
        projected = projected + offsetView
        projected *= Vector3(Width, Height, 1) * 0.5
        if showPoint:
            pygame.draw.circle(screen,self.color, projected.GetTuple(), self.radius)
        return projected
