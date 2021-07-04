import utils.matrix as matrix
import utils.transform as transform
from utils.vector import Vector3
from constants import Width, Height, Zoffset
from utils.camera import Camera
import pygame


class Point:
    def __init__(
        self,
        position: Vector3 = Vector3(),
        color: tuple[int, int, int] = (255, 255, 255),
        radius: float = 10,
    ):
        self.position = position
        self.color = color
        self.radius = radius
        self.transform = transform.identityMatrix()

    def update(
        self, screen: pygame.Surface, camera: Camera, showPoint: bool = False
    ) -> Vector3:

        transformed = matrix.multiplyMatrixVector(self.position, self.transform)
        transformed += Vector3(0, 0, Zoffset)
        transformed = matrix.multiplyMatrixVector(transformed, camera.viewMatrix)

        projected = matrix.multiplyMatrixVector(
            transformed, transform.ProjectionMatrix(camera)
        )
        projected *= Vector3(-1, -1, 1)

        offsetView = Vector3(1, 1, 0)
        projected = projected + offsetView
        projected *= Vector3(Width, Height, 1) * 0.5

        if showPoint:
            pygame.draw.circle(screen, self.color, projected.GetTuple(), self.radius)

        return projected
