firstVariable = input("Enter first variable:")
secondVariable = input("Enter second variable:")

print(f"Original value:\nFirst: {firstVariable} \nSecond: {secondVariable}")

firstVariable, secondVariable = secondVariable, firstVariable

print(f"Revers value:\nFirst: {firstVariable} \nSecond: {secondVariable}")