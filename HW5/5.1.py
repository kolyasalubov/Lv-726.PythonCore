# Author: Serhii
# HW5 task 5.1


# input the MAX number to which you want to send
max_num = 11

# check if number is divisible by 2 and 3
n = 1  # starting numbers from 0
# run until it reaches Max number
print("Numbers not divisible by 2 and 3")
while n <= max_num:
    if n % 2 != 0 and n % 3 != 0:
        print(n, ", Memory ID =",id(n))
    n = n + 1       # incrementing the counter

# check if number is divisible by 3
n = 1  # starting numbers from 0
# run until it reaches Max number
print("Numbers are divisible by 3 - odd!")
while n <= max_num:
    if n % 3 == 0:
        print(n, ", Memory ID =",id(n))
    n = n + 1       # incrementing the counter


# check if number is divisible by 2
n = 1  # starting numbers from 0
# run until it reaches Max number
print("Numbers are divisible by 2 - even!")
while n <= max_num:
    if n % 2 == 0:
        print(n, ", Memory ID =",id(n))
    n = n + 1       # incrementing the counter
