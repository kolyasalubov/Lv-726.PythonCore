# Author: Serhii
# HW4 task 4.1
# Inputing the user digit from keyboard

your_magic_number = int(input('\nInput a digit: '))
factorial_A, factorial_B = 1, 1
# factorial_A = factorial_B = 1
print(f'Printing here two Factorials: A={factorial_A} and B={factorial_A}')
print(f'Printing here Memory Addr of two Factorials: A =', id(factorial_A), 'and B =', id(factorial_B))

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