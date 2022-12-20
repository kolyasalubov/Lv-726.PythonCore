from dataclasses import dataclass
from typing import List

sides = []
while True:
    inputed_side = input("Enter side: ")
    if inputed_side == "q":
        break
    if int(inputed_side) <= 0:
        raise ValueError("Side of polygon cannot be <= 0!")
        continue
    sides.append(int(inputed_side))


@dataclass
class Polygon:
    number_of_sides: int
    sides_list: List[int]


class Triangle(Polygon):
    def __init__(self, number_of_sides: int, sides_list: List[int]):
        super().__init__(3, sides_list)

    def calc_area(self) -> float:
        a, b, c = self.sides_list
        # semi-perimeter
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Rectangle(Polygon):
    def __init__(self, number_of_sides: int, sides_list: List[int]):
        super().__init__(4, sides_list)

    def calc_area(self) -> int:
        return self.sides_list[0] * self.sides_list[1]


if len(sides) == 3:
    if ((sides[0] + sides[1]) > sides[2]) and ((sides[0] + sides[2]) > sides[1]) \
            and ((sides[1] + sides[2]) > sides[0]):
        triangle = Triangle(3, sides)
        print(triangle.calc_area())
elif len(sides) == 4:
    if (sides[0] == sides[2]) and (sides[1] == sides[3]):
        rectangle = Rectangle(4, sides)
        print(rectangle.calc_area())
