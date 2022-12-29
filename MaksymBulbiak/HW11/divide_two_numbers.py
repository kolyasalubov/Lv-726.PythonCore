def divide_two_numbers():
    try:
        num1, num2 = map(float, input('Enter two numbers separated by commas:').split(','))  
        print("Result:",round(num1 / num2,2))
    except ValueError:
        print("Value Error!")
    except ZeroDivisionError:
        print("Division by zero is impossible")
    else:
        print("The sum of these numbers:",round(num1+num2,2))
    finally:
        print("The function is completed")
divide_two_numbers()