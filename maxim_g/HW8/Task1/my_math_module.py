from math import pow, pi

PI = pi


def area_of_rectangle(*args):
    a, b = args
    return a * b


def area_of_triangle(*args):
    a, b, c, = args
    p = (a + b + c) / 2
    return round(p, 2)


def area_of_circle(c):
    c_area = round(PI * pow(c, 2), 2)
    return c_area




