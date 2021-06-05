from math import tan, pi
from constants import *
from utils.vector import *
from utils.transform import *

class Camera:
    def __init__(self, position, near, far, fov):
        self.position = position
        self.near = near
        self.far = far
        self.fov = fov
        self.tangent = 1.0 / tan(self.fov * 0.5 / 180 * pi)
        self.direction = Vector3()
        self.up = Vector3()
        self.transform = identityMatrix()
        self.rotation = identityMatrix()
        self.target = position
