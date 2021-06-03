class Triangle:
    def __init__(self, v1=None, v2=None, v3=None):
        self.vertex1 = v1
        self.vertex2 = v2
        self.vertex3 = v3
        self.color = (255, 255, 255)

    def GetPolygons(self):
        return [(int(self.vertex1.x), int(self.vertex1.y)),
                (int(self.vertex2.x), int(self.vertex2.y)),
                (int(self.vertex3.x), int(self.vertex3.y))]

    def __repr__(self):
        #debug
        return f"triangle-> {(self.vertex1), (self.vertex2), (self.vertex3)}"
