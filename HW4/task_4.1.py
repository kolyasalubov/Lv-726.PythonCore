# Author: Serhii
# HW4 task 4.1
# Inputing the user digit from keyboard

your_magic_number = int(input('\nInput a digit: '))
factorial_A = 1
factorial_B = 1


if your_magic_number < 0:
    print('Incorrect input! Number must be > 0\n')
    # if your_magic_number < 0 then RESULT = Achtung!!
elif your_magic_number == 0:
    print(f'\nFactorial of {your_magic_number}! is equal to 1\n')
    # if your_magic_number = 0 then RESULT = 1
else:
    for i in range(1,your_magic_number + 1):
        factorial_A *= i
        factorial_B = factorial_B * i
    print(f'\nFactorial (way_A) of {your_magic_number} is equal to: {your_magic_number}! = {factorial_A}\n')
    print(f'\nFactorial (way_B) of {your_magic_number} is equal to: {your_magic_number}! = {factorial_B}\n')