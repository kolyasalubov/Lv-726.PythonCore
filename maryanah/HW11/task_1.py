num = (input("Enter two numbers through a comma: "))

try:
    result = round(float(num[0]) / float(num[-1]),3)
    print(f"{num[0]} / {num[-1]} = {result}")
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Make sure you have entered numbers.")
except:
    print("Try again.")