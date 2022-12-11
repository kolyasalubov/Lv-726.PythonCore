
from random import randint
'''script-game that randomly generates a number from a range 
numbers from 1 to 100 and asks the user to guess this number 
up to 10 times and printed message about win else prints message 
about loss.

Parameters: user_name - value that save the entered user name

Result: text message about win with number of attempts or loss

'''

#ask user to input his name
user_name = input('Please, input your name? \n')
#choice of number from randint
number = randint(1, 100)

print(f'Well, {user_name}, I am thinking of a number between 1 and 100.')

#count of attempts
count = 0

while True:
    #checking the number of attempts
    if count > 10:
        print(f"You'r very unlycky, my dear trainee {user_name}, moore than 10 attempts")
        break
    
    count += 1 
    guess_number = int(input('Take a guess, enter your number: '))

    #checking the number
    if guess_number == number:
        print(f'Good job, my dear trainee {user_name}. You gessed it on the {count}-th try. Go on!')
        break
    
    elif 1<= guess_number <= 100 and guess_number < number:
        print('Your number is less. Try again.')

    elif 1<= guess_number <= 100 and guess_number > number:
        print('Your number is more. Try again.')

    elif not 1 <= guess_number <= 100:
        print(f'Fatal error, my dear trainee {user_name}. Just read the condition...')