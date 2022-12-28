class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f"The area of the triangle is {area}")

    def isTriangle(self):
        a, b, c = self.sides
        if a <= 0 or b <= 0 or c <= 0:
            # check if all sides are more than 0
            return 0
        elif (a + b) <= c or (a + c) <= b or (b + c) <= a:
            # check if sum of each two sides are more than third
            return 0
        else:
            return 1


class Rectangle(Polygon):
    """This is class for initialize Rectangle."""

    def __init__(self):
        super().__init__(2)

    def findArea(self):
        a, b = self.sides
        # calculate area
        area = a * b
        print(f"The area of the rectangle is {area}")

# Initialize triangle
triangle1 = Triangle()

# Enter sides
triangle1.inputSides()

# Check if sides are correct. If yes, calculate area
if triangle1.isTriangle():
    triangle1.findArea()
else:
    print("Enter correct numbers.")

# Initialize rectangle
rectangle1 = Rectangle()

# Enter sides
rectangle1.inputSides()

# Calculate area
rectangle1.findArea()
