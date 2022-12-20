import re


password = input("Create password:")

if re.findall("[a-z]", password) == []:
    print("At least 1 letter between [a-z].")
if re.findall("[A-Z]", password) == []:
    print("At least 1 letter between [A-Z].")
if re.findall("[0-9]", password) == []:
    print("At least 1 digit between [0-9].")
if re.findall("[$#@]", password) == []:
    print("At least 1 character from [$#@].")
if 6 >= len(password) <= 16:
    print("Minimum length 6 characters and Maximum length 16.")
