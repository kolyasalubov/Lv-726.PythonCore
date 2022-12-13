from math import sqrt, pi

def rectangle_area(side1, side2):
    """This function returns the area of the rectangle.
    Input: sides, have to be entered by user in terminal."""
    return side1 * side2

def triangle_area(side1, side2, side3):
    """This function returns the area of the triangle.
    Input: sides, have to be entered by user in the terminal."""
    per = (side1 + side2 + side3) / 2
    return sqrt(per * (per - side1) * (per - side2) * (per - side3))

def circle_area(radius):
    """This function returns the area of the circle.
    Input: radius, entered by user in terminal.
    Output: the area"""
    return pi * radius**2

shape = input("Choose shape (rectangle / triangle / circle): ")

if shape == 'rectangle':
    side1 = int(input("Enter first side: "))
    side2 = int(input("Enter second side: "))
    print("The area is:", rectangle_area(side1, side2))

elif shape == 'triangle':
    side1 = int(input("Enter first side: "))
    side2 = int(input("Enter second side: "))
    side3 = int(input("Enter third side: "))
    print("The area is:", triangle_area(side1, side2, side3))

elif shape == 'circle':
    radius = int(input("Enter radius: "))
    print("The area is:", circle_area(radius))

else:
    print("You should choose one of the mentioned shapes.")
