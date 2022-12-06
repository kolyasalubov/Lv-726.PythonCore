inputLog = input("Enter your login")
login = "First"

while inputLog != login:
    print("login failed, please try again")
    inputLog = input("Enter your login")
if inputLog == login:
    print("Congratulations, login accepted")


#print(login)