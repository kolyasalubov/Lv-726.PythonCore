# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users.
# If the login is different, send an error message.
# (need to use loop while)


is_password_correct = False
while not is_password_correct:
    user_password = input("Inter the login please: ")
    if user_password == 'First':
        print("Success login accepted")
        is_password_correct = True
    else:
        print("Entered login is not correct, try again")


