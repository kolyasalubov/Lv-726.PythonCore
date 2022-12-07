# Task3.
# Print Fibonacci numbers up to the entered number n,
# using cycles. (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

# VARIABLES
first = 0
second = 1
def printFibonacci():
    global first, second
    count = int(input('Enter the TOTAL count of numbers: '))
    while count >= 0:
        first, second = second, (first + second)
        count -= 1
        print(first)

printFibonacci()