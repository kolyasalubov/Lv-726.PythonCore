# Task1. Write a script that will calculate
# the factorial of the entered number
# without using recursion.

user_number = int(input("Inter the number: "))

factorial_of_entered_number = 0
for val in range(user_number+1):
    if not factorial_of_entered_number:
        factorial_of_entered_number += 1
    factorial_of_entered_number *= val

print(factorial_of_entered_number)


