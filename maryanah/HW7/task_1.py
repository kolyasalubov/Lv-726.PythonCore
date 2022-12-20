def max_num(num1, num2):
    """This function returns the maximum value
    of two numbers, entered by user."""
    if num1 >= num2:
        return num1
    else:
        return num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(max_num(num1, num2))
