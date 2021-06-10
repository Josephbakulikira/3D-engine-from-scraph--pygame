from constants import *
from utils.vector import *
from math import cos, sin
from utils.matrix import *

def ProjectionMatrix(camera):
    matrix = Matrix()
    matrix.val =  [ [aspect * camera.tangent, 0.0, 0.0, 0.0],
             [0.0, camera.tangent, 0.0, 0.0 ],
             [ 0.0, 0.0, camera.far/(camera.far - camera.near), 1],
             [ 0.0, 0.0, (-camera.far * camera.near) / (camera.far - camera.near), 0.0]
             ]
    return matrix

def PointAt(current, next, up):
    f = Normalize(next - current) #  forward vector
    u = Normalize( up - f * (dotProduct(up, f)) ) #  up vector
    r = crossProduct(u, f) # right vector
    matrix = Matrix()
    matrix.val =[
           [r.x, r.y, r.z, 0.0],
           [u.x, u.y, u.z, 0.0],
           [f.x, f.y, f.z, 0.0],
           [current.x, current.y, current.z, 1.0]
           ]
    return matrix



def RotationX(angle):
    matrix = Matrix()
    matrix.val = [[1, 0.0, 0.0, 0.0],
            [0.0, cos(angle), sin(angle), 0.0],
            [0.0,-sin(angle), cos(angle), 0.0],
            [0.0, 0.0, 0.0, 1]]
    return matrix


def RotationY(angle):
    matrix = Matrix()
    matrix.val = [[cos(angle), 0.0, -sin(angle), 0.0],
            [0.0, 1, 0.0, 0.0],
            [sin(angle), 0.0, cos(angle),0.0],
            [0.0, 0.0, 0.0, 1]]
    return matrix

def RotationZ(angle):
    matrix = Matrix()
    matrix.val = [[cos(angle), sin(angle), 0.0, 0.0],
            [-sin(angle), cos(angle), 0.0, 0.0],
            [0.0, 0.0, 1, 0.0],
            [0.0, 0.0, 0.0, 1]]
    return matrix

def ScalingMatrix(scale):
    matrix = Matrix()
    matrix.val = [[scale, 0.0, 0.0, 0.0],
            [0.0, scale, 0.0, 0.0],
            [0.0, 0.0, scale, 0.0],
            [0.0, 0.0, 0.0, 1]]
    return matrix

def identityMatrix():
    matrix = Matrix()
    matrix.val = [[1, 0.0, 0.0, 0.0],
            [0.0, 1, 0.0, 0.0],
            [0.0, 0.0, 1, 0.0],
            [0.0, 0.0, 0.0, 1]]
    return matrix

def translateMatrix(pos):
    matrix = Matrix()
    matrix.val = [[1, 0.0, 0.0, pos.x],
                [0.0, 1, 0.0, pos.y],
                [0.0, 0.0, 1, pos.z],
                [0.0, 0.0, 0.0, 1]]
    return matrix

def Shearing(xy, xz, yx, yz, zx, zy):
    matrix = Matrix()
    matrix.val = [ [1, xy, xz, 0.0],
                      [yx, 1, yz, 0.0],
                      [zx, zy, 1, 0.0],
                      [0.0, 0.0, 0.0, 1] ]
    return matrix
