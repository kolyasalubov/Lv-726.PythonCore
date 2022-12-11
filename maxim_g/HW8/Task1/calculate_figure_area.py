import my_math_module

math_dict = {
    'rectangle': my_math_module.area_of_rectangle,
    'triangle': my_math_module.area_of_triangle,
    'circle': my_math_module.area_of_circle
}


erroneous_data = False
while True:
    if not erroneous_data:
        user_get = input('What geometric shape do you want to calculate the area of?: ')
    if user_get == "exit":
        print('Exit from program')
        break
    figure_area = input('enter the area of the figure separated by a space: ').split()
    int_area = tuple([int(val) for val in figure_area])
    if user_get in math_dict:
        try:
            print(f'Result:  calculate area of {user_get} is {math_dict[user_get](*int_area)}')
            erroneous_data = False
        except ValueError:
            print("You entered incorrect data please try again")
            erroneous_data = True
        except TypeError:
            print("You entered incorrect data please try again")
            erroneous_data = True
    else:
        print("Not found please try again")
