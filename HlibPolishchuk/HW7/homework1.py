num1 = int(input("Your First number:"))
num2 = int(input("Your Second number:"))

def max_num(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2

print("The largest number of two numbers:", max_num(num1,num2))


