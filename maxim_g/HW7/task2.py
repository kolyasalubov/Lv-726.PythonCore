# Task2. Write a program that calculates the area of ​​a rectangle, triangle and circle
# (write three functions to calculate the area, and call them in the main program depending on the user's choice).

PI = 3.14


def calculate_area_rectangle(width, height):
    return width * height


def calculate_area_triangle(a, b, c):
    return round((a + b + c) / 2, 2)


def calculate_area_circle(radius):
    return round(PI * (radius * radius), 2)


if __name__ == "__main__":
    print(calculate_area_rectangle(5, 7))
    print(calculate_area_triangle(10, 9, 14))
    print(calculate_area_circle(6))
