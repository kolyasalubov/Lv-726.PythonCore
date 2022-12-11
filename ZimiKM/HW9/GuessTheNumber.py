
import random

user_name = input('Please, input your name? \n')
number = random.randint(1, 40)

print(f'Well, {user_name}, I am thinking of a number between 1 and 40.')

count = 0

while True:
    if count > 10:
        print(f"You'r very unlycky, my dear trainee {user_name}, moore than 10 attempts")
        break
    
    count += 1 
    guess_number = int(input('Take a guess, enter your number: '))

    if guess_number == number:
        print(f'Good job, my dear trainee {user_name}. You gessed it on the {count}-th try. Go on!')
        break
    
    elif 1<= guess_number <= 40 and guess_number < number:
        print('Your number is less. Try again.')

    elif 1<= guess_number <= 40 and guess_number > number:
        print('Your number is more. Try again.')

    elif not 1 <= guess_number <= 40:
        print(f'Fatal error, my dear trainee {user_name}. Just read the condition...')