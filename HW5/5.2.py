# Author: Serhii
# HW5 task 5.2

# Init variables
login_realist = input("Hey, Please enter your login: ")
login_desired = 'First'
# Writing your Login into secure hidden file
file = ".login.txt"
print ("Writing your Login into secure and hidden Linux file: ", file)
with open('.login.txt', 'w') as f:
    f.write('login_realist')
    # f.write('You has firstly entered: ' + login_realist)
    # f.write(name + ' lives in ' + live)
    f.close()

print("===========  Way-1  ===========")
while not login_realist == "First":
    print("Login incorrect. Please enter proper login: ")
    login_realist = input()
print("Hello, %s" % login_realist)


print("===========  Way-2  ===========")
while 1:
    login_realist = input("Hey, Please enter your login again: ")
    if login_realist == "First":
        print(f"Hello, {login_realist}")
        break


print("===========  Way-3  ===========")
login_realist = str(input("Hey, Please enter your login again: "))
login_desired = 'First'
while login_realist == login_desired:
    print(f'Hello, {login_realist}')
    print(f'But firstly You had entered the Login: X')
    break
else:
    print("Login incorrect. Please enter proper login: ")