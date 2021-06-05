from math import pow, sqrt

def toVector3(matrix):
    return Vector3(matrix.val[0][0], matrix.val[0][1], matrix.val[0][2])

def crossProduct(a, b):
    x = a.y * b.z - a.z * b.y
    y = a.z * b.x - a.x * b.z
    z = a.x * b.y - a.y * b.x
    return Vector3(x, y, z)

def dotProduct(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z

def GetMagnitude(a):
    if type(a) == Vector3:
        return sqrt( pow(a.x,2) + pow(a.y,2) + pow(a.z,2) )
    else:
        return sqrt(pow(a.x,2) + pow(a.y,2))

def Normalize(a):
    mg = GetMagnitude(a)
    if mg == 0:
        return Vector3()
    return Vector3(a.x/mg, a.y/mg, a.z/mg)

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = 1

    def __add__(a, b):
        if type(b) == Vector3:
            return Vector3(a.x + b.x, a.y + b.y, a.z + b.z)
        return Vector3(a.x + b, a.y + b, a.z + b)

    def __sub__(a, b):
        if type(b) == Vector3:
            return Vector3(a.x - b.x, a.y - b.y, a.z - b.z)
        return Vector3(a.x - b, a.y - b, a.z - b)

    def __mul__(a, b):
        if type(b) == Vector3:
            return Vector3(a.x * b.x, a.y * b.y, a.z * b.z)
        return Vector3(a.x * b, a.y * b, a.z * b)

    def __truediv__(a, b):
        if type(b) == Vector3:
            return Vector3(a.x / b.x, a.y / b.y, a.z / b.z)
        return Vector3(a.x / b, a.y / b, a.z / b)

    def toMatrix(self):
        return [[self.x, self.y, self.z, self.w]]


    def GetTuple(self):
        return (int(self.x), int(self.y))

    def __repr__(self):
        #debug
        return f" vec3-> ({self.x}, {self.y}, {self.z})"

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(a, b):
        if type(b) == Vector2:
            return Vector2(a.x + b.x, a.y + b.y)
        return Vector2(a.x + b, a.y + b)

    def __sub__(a, b):
        if type(b) == Vector2:
            return Vector2(a.x - b.x, a.y - b.y)
        return Vector2(a.x - b, a.y - b)

    def __mul__(a, b):
        if type(b) == Vector2:
            return Vector2(a.x * b.x, a.y * b.y)
        return Vector2(a.x * b, a.y * b)

    def __truediv__(a, b):
        if type(b) == Vector2:
            return Vector2(a.x / b.x, a.y / b.y)
        return Vector2(a.x / b, a.y / b)

    def __repr__(self):
        return f"vec2-> ({self.x}, {self.y})"
