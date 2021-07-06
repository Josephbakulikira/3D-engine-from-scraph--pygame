from math import floor

class Triangle:
    def __init__(self, v1=None, v2=None, v3=None, color=(255, 255, 255)):
        self.vertex1 = v1
        self.vertex2 = v2
        self.vertex3 = v3
        self.color = color
        self.verticeColor = color

    def Shade(self, val):
        r, g, b = 0, 0, 0
        if self.color[0] * val > 255:
            r = 255
        elif self.color[0] * val < 0:
            r = 0
        else:
            r = int(self.color[0] * val)

        if self.color[1] * val > 255:
            g = 255
        elif self.color[1] * val < 0:
            g = 0
        else:
            g = int(self.color[1] * val)

        if self.color[2] * val > 255:
            b = 255
        elif self.color[2] * val < 0:
            b = 0
        else:
            b = int(self.color[2] * val)

        return (r, g, b)

    def GetPolygons(self):
        return [(int(self.vertex1.x), int(self.vertex1.y)),
                (int(self.vertex2.x), int(self.vertex2.y)),
                (int(self.vertex3.x), int(self.vertex3.y))]

    def __repr__(self):
        #debug
        return f"triangle-> {(self.vertex1), (self.vertex2), (self.vertex3), {self.color}}"
