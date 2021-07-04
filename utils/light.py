# simple directional light
class Light:
    def __init__(self, position):
        self.position = position
        self.direction = self.position.norm()
