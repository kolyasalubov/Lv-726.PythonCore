# Author - Serhii Hladyr
# Mail: sergiy.gladyr@gmail.com
import os
import platform
import re
import sys

# Init Variables
name = input ("Your name: ")
age = input ("Your age: ")
live = input ("Where do you live?: ")
python_1 = (sys.version)
python_2 = (sys.version_info)
python_3 = (platform.python_version_tuple())
python_4 = ".".join(map(str, sys.version_info[:3]))

# Sanitizing function
def sanitize(string):
    special_char = re.compile('[@_!$%^&*()<>?/\|}{~:]#')
    if special_char.search(string) == None:
        return "string is accepted"
    else:
        return "string not accpeted"

# Run commands
print ("This is the first Python Program in IT Academy")
print ("Hello,", name)
print ("Your age is", age)
print ("You live in", live)
print ("Sanitizing result of your Name: ", (sanitize(name)))

print ("1 - Your are using next python version (sys):", python_1)
print ("2 - Your are using next python version (sys info):", python_2)
print ("3 - Your are using next python version (platform):", python_3)
print ("4 - Your are using next python version (join map):", python_4)

############### Stages 1,2,3 ################

# Make variables lowercase
print ("Stage-1: Here is the stage with lowercasing Name and Live")
name = name.lower()
live = live.lower()

# Write lowercase variables to files
file = "document.txt"
print ("Stage-2: Writing both Name and Live to txt File:", file)
with open('document.txt', 'w') as f:
    f.write(name + ' lives in ' + live)
    f.close()

# Output the file content to screen
print ("Stage-3: Outputing the file content to screen:")
file = open("document.txt")
print(file.read())
file.close()