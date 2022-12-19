from math import sqrt, pi

print("1 - Rectangle \n2 - Triangle \n3 - Circle")

figure = input("Choose a figure: ")

if figure == "1":
    print("The lengths of the sides of the rectangle: ")
    a = float(input("a = "))
    b = float(input("b = "))
    print("Area:" , a*b)
elif figure == "2":
    print("The lengths of the sides of the triangle:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    p = (a + b + c) / 2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print("Area:", s)
elif figure == "3":
    r = float(input("Сircle radius = "))
    print("Area:", pi * r ** 2)
else:
    print("Input error")
