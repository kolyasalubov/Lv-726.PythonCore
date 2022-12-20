import re

"""
Write a Python program to check the validity of a password (input from users).
"""

password = input("Password:\n")
# try:
#     assert  re.findall("[a-z]",password)
#     assert  re.findall("[A-Z]",password)
#     assert  re.findall("[$#@]",password)
#     assert  re.findall("[0-9]",password)
#     assert  len(password) < 16
#     assert  len(password) > 6
#     print("You have entered!")
# except:
#     print("At least 1 letter between [a-z].\nand 1 letter between [A-Z].\n\
# At least 1 character from [$#@].\nAt least 1 number between [0-9].\n\
# Minimum length 6 characters.\nMaximum length 16 characters.\n\
# At least 1 number between [0-9].")


if re.findall("[a-z]",password) == []:
    print("At least 1 letter between [a-z]")
if re.findall("[A-Z]",password) == []:
    print("And 1 letter between [A-Z]")
if re.findall("[$#@]",password) == []:
    print("At least 1 character from [$#@]")
if re.findall("[0-9]",password) == []:
    print("At least 1 number between [0-9]")
if 6 >= len(password) <= 16:
    print("Minimum length 6 characters.\nMaximum length 16 characters.")
