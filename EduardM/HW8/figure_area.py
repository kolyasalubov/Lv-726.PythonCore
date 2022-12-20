import math


def rectangle_area(a: int, b: int) -> int:
    return a * b


def triangle_area(h: int, a: int) -> float:
    return 0.5 * h * a


def circle_area(r: int) -> float:
    return math.pi * math.pow(r, 2)
