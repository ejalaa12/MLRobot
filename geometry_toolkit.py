import numpy as np


def dist(xa, ya, xb, yb):
    "retuns the distance between two points"
    return ((xb - xa)**2 + (yb - ya)**2)**0.5


def find_equation(x, y, theta):
    "returns the affine value a, b of line defined by a point and an angle"
    if theta == 0 or theta == np.radians(180):
        return np.NaN, 'H'
    elif theta == np.radians(90) or theta == np.radians(270):
        return 'W', np.NaN
    else:
        a = np.tan(theta)
        b = y - a * x
        return a, b


def solve(a, b, w, h):
    pass
