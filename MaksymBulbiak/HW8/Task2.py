import random 

"""
Write a game script that randomly generates a number from a range
numbers from 1 to 100 and asks the user to guess this number.
The program reads the numbers entered by the user and prompts the user
about whether the guessed number is greater or less 
than the number entered by the user.
The game must continue until the user enters the guessed number
program, then prints a welcome message.
"""


num = random.randint(1, 100)

while True:
    p_num = int(input("Enter your number:"))
    if p_num == num:
        print("Congratulations, you won!")
        break
    elif p_num <= num:
        print("Number is greater then yours")
    elif p_num >= num:
        print("Number is less then yours")