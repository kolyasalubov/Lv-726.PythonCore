from math import pow, pi

print("1 - Rectangle \n2 - Triangle \n3 - Circle")

figure = input("Choose a figure: ")

def rectangle_square():
    if figure == "1":
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))
        square = a * b
        return f"The square of the rectangle is {square}"
print(rectangle_square())


def triangle_square():
    if figure == "2":
        a = float(input("Enter base: "))
        b = float(input("Enter height: "))
        square = 0.5 * a * b
        return f"The square of the triangle is {square}"
print(triangle_square())

def circle_square():
    if figure == "3":
        radius = float(input("Enter radius: "))
        square = pi * radius**2
        return f"The square of the circle is {square}"
print(circle_square())



