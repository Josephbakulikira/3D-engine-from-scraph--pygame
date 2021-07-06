from utils.vector import Normalize

class Light: # simple directional light
    def __init__(self, position):
        self.position = position
        self.direction = Normalize(self.position)
