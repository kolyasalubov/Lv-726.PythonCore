from math import pi
'''
Calculates the area of ​a rectangle, triangle and circle

'''

def circle_area(radius) -> float:
    '''
    Calculate circle area vith radius r

    Parameter: 
        radius (int or float) > 0
    Return:
        circle area
    '''
    return pi * radius **2


def triangle_area(side1, side2, side3) -> float:
    '''
    Calculate triangle area vith 3 sides

    Parameter: 
        side1, side2, side3 - (int or float) > 0
    Return:
        triangle area - float
    '''
    semiperimeter = (side1 + side2 + side3) / 2
    return (semiperimeter*(semiperimeter - side1)*
            (semiperimeter - side2)*(semiperimeter - side3))**0.5


def rectangle_area(side1, side2):
    return side1 * side2


figure = input("""Area of wich figure You want to calculate:
        circle, triangle or rectangle? - """)
if figure == 'circle':
    radius = int(input("""Input the Radius of the Circle
        (radius must be > 0): """))
    print(f"""Circle area with radius {radius} is equal to
            {circle_area(radius)}""")
elif figure == 'triangle':
    side1, side2, side3 = input("""Input the Sides of triangle
            (must be >0): """).split()
    side1, side2, side3 = int(side1), int(side2), int(side3)
    print(f"""Area of the Triangle with sides {side1, side2, side3}
            is equal to {triangle_area(side1, side2, side3)}""")
elif figure == 'rectangle':
    side1, side2 = input("""Input the Rectangle sides
            (must be >0): """).split()
    side1, side2 = int(side1), int(side2)
    print(f"""Area of the Rectangle with sides {side1, side2}
            is equal to {rectangle_area(side1, side2)}""")
else:
    print('You input something wrong. Try again')