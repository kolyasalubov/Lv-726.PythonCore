from calculator import * 

"""
Write a script - calculator.py, in which you create functions
addition, subtraction, multiplication, division, and in another module
ask the user what action he wants to perform and with which
numbers
"""

action = input("Write one of the math operation\nDivision, Addition,\
Multiplication or Subtraction:")

if action == 'Division':
    numbers  = [int(input('Enter next numbers: ')) for item in range(2)]
    print(division(numbers))


if action == 'Addition':
    numbers = [int(input('Enter next numbers: ')) for item in range(int(input('Enter number: ')))]
    print(addition(numbers))

if action == 'Multiplication':
    numbers = [int(input('Enter next numbers: ')) for item in range(int(input('Enter number: ')))]
    print(multiplication(numbers))

if action == 'Subtraction':
    numbers = [int(input('Enter next numbers: ')) for item in range(int(input('Enter number: ')))]
    print(subtraction(numbers))
  