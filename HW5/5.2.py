# Task2.
# Create a list that contains elements of integer type, then
# use the loop to change the type of these elements to a floating
# type. (Hint: use the built-in float () function).

import subprocess
cmd = 'git branch'
status, output = subprocess.getstatusoutput(cmd)
branches = []
if status == 0:
    branches += output.split('\n')
print('Hey, Man! You are using the next Git Branches: ', branches)
print('==============================================')
def changeIntegerToFloat():
    list = []
    total = int(input('Hey, Man! Please enter the TOTAL number of elements in list: '))

    for i in range(0, total):
        element = int(input(f"Please, enter the {i}th element of integer type:\n"))
        list.append(element)

    print(f'Hey, Man! You have entered the next list of elements: {list}')
    floated_list = []
    for i in list:
        print(f'Warning! I am floating: {i} to --> ', float(i))
        floated_list.append(float(i))
    print(f'Hey, Man! Here is your RESULT: {floated_list}')


changeIntegerToFloat()