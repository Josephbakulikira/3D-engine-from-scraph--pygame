from math import tan, pi
from constants import *

class Camera:
    def __init__(self, position, near, far, fov):
        self.position = position
        self.near = near
        self.far = far
        self.fov = fov
        self.tangent = 1.0 / tan(self.fov * 0.5 / 180 * pi)
