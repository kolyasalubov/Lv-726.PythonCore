from math import pow, pi

def rectangle_square():
    """This function returns the square of the rectangle.
    Input: sides, have to be entered by user in terminal."""
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    square = side1 * side2
    return f"The square of the rectangle is {square}"

def triangle_square():
    """This function returns the square of the triangle.
    Input: base and height, have to be entered by user in the terminal."""
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    square = 0.5 * height * base
    return f"The square of the triangle is {square}"

def circle_square():
    """This function returns the square of the circle.
    Input: radius, entered by user in terminal.
    Output: the square"""
    radius = float(input("Enter radius: "))
    square = pi * radius**2
    return f"The square of the circle is {square}"
