import math


def area_triangle(sides: tuple) -> int | float:
    """
    :param sides: tuple with triangle sides
    :return: area via Geron's formule
    """
    half_perimetr = sum(list(sides)) / 2
    return (half_perimetr * (half_perimetr - sides[0]) * (half_perimetr - sides[1]) * (half_perimetr - sides[2])) ** 0.5


def area_rectangle(sides: tuple) -> int | float:
    """
    :param sides: tuple with two neighbouring sides
    :return: rectangle's area
    """
    return sides[0] * sides[1]


def area_circle(r):
    """
    :param r: radius
    :return: area
    """
    return math.pi * r**2
