import math


num = int(input('Enter a number:'))

print(math.factorial(num))


# Another option
def factorial_func():
    
    if num < 0:
        print('\nA number less than zero')
    elif num == 0:
        print('\nFactorial is 1')
    elif num > 0:
        fact = 1
        for i in range(1,num+1):
            fact *= i
        print(f'\n{fact}')
            

factorial_func()