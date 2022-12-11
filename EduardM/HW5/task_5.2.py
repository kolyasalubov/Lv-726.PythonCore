number = int(input("Enter the number: "))

fib_num1 = 0
fib_num2 = 1
print(fib_num1)

while fib_num2 <= number:
    print(fib_num2)
    fib_num1, fib_num2 = fib_num2, (fib_num1 + fib_num2)
