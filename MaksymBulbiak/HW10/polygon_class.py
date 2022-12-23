class Polygon:
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
        self.sides_value = [0 for i in range(num_of_sides)]

    def inputSides(self):
        self.sides_value = [int(input(f"Enter side {str(i+1)}: ")) for i in range(self.num_of_sides)]

    def dispSides(self):
        [print(f"Side {i+1} is {self.sides_value[i]}") for i in range(self.num_of_sides)]

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def findAreaRectangle(self):
        a, b = self.sides_value
        area = a*b
        print(f"The area of the rectangle is {area}")   

def start():
    r = Rectangle()
    r.inputSides()
    r.dispSides()
    r.findAreaRectangle()


start()
