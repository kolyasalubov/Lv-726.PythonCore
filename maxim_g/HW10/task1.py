

class Polygon():
    def __init__(self, sides):
        self.sides = sides
        self.sides_list = self.type_side(self.sides)

    def type_side(self, side_count):
        return [float(input(f'input side {side+1} with number: ')) for side in range(side_count)]

    def show_sides(self):
        counter = 0
        while self.sides > counter:
            print(f"Side {counter+1} is a {self.sides_list[counter]}")
            counter += 1


result = Polygon(4)
result.show_sides()


class Rectangle(Polygon):
    sides_of_rectangle = 2

    def __init__(self):
        super().__init__(Rectangle.sides_of_rectangle)
        self.square_of_rectangle = self.find_area(self.sides_list)

    def find_area(self, sides_list_of_rectangle):
        sum_of_all_sides = sides_list_of_rectangle
        return sum_of_all_sides[0] * sum_of_all_sides[1]

    def output_square_of_rectangle(self):
        print(f'Square of rectangle is {self.square_of_rectangle}')


rectangle1 = Rectangle()
# test data 7, 4
rectangle1.output_square_of_rectangle()  # S = a · b = 7 · 4 = 28(м)2
