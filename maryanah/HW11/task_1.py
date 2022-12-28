num = (input("Enter two numbers through a comma: "))

try:
    result = round(eval(num.replace(',', '/')), 3)
    print(result)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Make sure you have entered numbers.")
except:
    print("Try again.")