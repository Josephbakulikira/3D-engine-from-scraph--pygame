from typing import Optional
from utils.vector import Vector3


class Triangle:
    def __init__(
        self,
        v1: Optional[Vector3] = None,
        v2: Optional[Vector3] = None,
        v3: Optional[Vector3] = None,
        color: tuple[int, int, int] = (255, 255, 255),
    ):
        self.vertex1 = v1 if v1 is not None else Vector3()
        self.vertex2 = v2 if v2 is not None else Vector3()
        self.vertex3 = v3 if v3 is not None else Vector3()
        self.color = color
        self.verticeColor = color

    def __repr__(self) -> str:
        return (
            f"triangle-> {(self.vertex1), (self.vertex2), (self.vertex3), {self.color}}"
        )

    def Shade(self, val: float) -> tuple[int, int, int]:
        channels = []
        for channel in self.color:
            if channel * val > 255:
                shade_channel = 255
            elif channel * val < 0:
                shade_channel = 0
            else:
                shade_channel = int(channel * val)
            channels.append(shade_channel)

        # awkward return statement expression due to mypy appeasement. Should revisit.
        return (channels[0], channels[1], channels[2])

    def GetPolygons(self) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
        return (
            (int(self.vertex1.x), int(self.vertex1.y)),
            (int(self.vertex2.x), int(self.vertex2.y)),
            (int(self.vertex3.x), int(self.vertex3.y)),
        )
