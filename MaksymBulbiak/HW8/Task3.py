from area import *

"""
Write a script that calculates the area of a rectangle a*b, area
of the triangle 0.5*h*a, the area of the circle pi*r**2
and use this script in another module in which we ask the
user the area of which figure he wants to calculate
"""

figure = input("Which figure do you want calculate the area of?\nReactangle = R, Triangle = T, Circle = C:")

if figure  == 'R':
    a = input("Enter side a:")
    b = input("Enter side b:")
    print("Rectangle area is",rectangle_area(a,b))


elif figure  == 'T':
    a = input("Enter side a:")
    h = input("Enter side h:")
    print("Triangle area is",triangle_area(h,a))


elif figure  == 'C':
    r = input("Enter side r:")
    print("Circle area is",circle_area(r))

