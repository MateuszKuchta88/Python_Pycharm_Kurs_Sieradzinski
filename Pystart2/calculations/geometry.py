from math import pi, pow, sqrt


def circle_area(r: float) -> float:
    return pi * pow(r, 2)


def circle_l(r: float) -> float:
    return 2 * pi * r


def triangle_area(a: float) -> float:
    return pow(a, 2) * sqrt(3) / 4


def line_centre(p1: tuple, p2: tuple) -> tuple:
    x1, y1 = p1
    x2, y2 = p2
    return (x2 - x1) / 2, (y2 - y1) / 2


def line_length(p1: tuple, p2: tuple) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
