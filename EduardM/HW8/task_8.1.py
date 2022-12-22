from figure_area import rectangle_area, triangle_area, circle_area

"""
Write a script that calculates the area of a rectangle a*b, area
of the triangle 0.5*h*a, the area of the circle pi*r**2
and use this script in another module in which we ask the
user the area of which figure he wants to calculate
"""

f = input("Which figure do you want calculate the area of?\nReactangle = R, Triangle = T, Circle = C: ")


def area_calc(figure: str) -> str:

    if figure == "R":
        side1 = int(input("Enter side a: "))
        side2 = int(input("Enter side b: "))
        return f"Rectangle area is {rectangle_area(side1, side2)}"

    elif figure == "T":
        sideh = int(input("Enter side a: "))
        h = int(input("Enter side h: "))
        return f"Triangle area is {triangle_area(h, sideh)}"

    elif figure == "C":
        r = int(input("Enter side r: "))
        return f"Circle area is {circle_area(r)}"


def main() -> None:
    print(area_calc(f))


if __name__ == "__main__":
    main()
