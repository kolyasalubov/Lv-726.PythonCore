def check_login():
    """Write a script that checks the login that the user enters. 
    If the login is "First", then greet the users. If the login is 
    different, send an error message. 
    (need to use loop while)
    """
    while True:
        user_ent = input('Enter your login: ')
        if  user_ent == 'First':
            print("Congratulations, you have entered")
            break
    

check_login()
     