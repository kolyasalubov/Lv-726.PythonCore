
logo = r"""                                       
                              _   _                                  _               
                             | | | |                                | |              
   __ _ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
  / _` | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | (_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \__, |\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
   __/ |                                                                             
  |___/                                                                                              """


def create_number():
    from random import randint
    random_number = randint(1 ,100)
    return random_number


def set_difficulty(selected_difficulty):
    if selected_difficulty == 'easy':
        return 10
    return 5


def check_number(user_number, conceived_number):
    if user_number > conceived_number:
        return 'Too high.'
    elif user_number < conceived_number:
        return 'Too low.'
    else:
        return f'You got it! The answer was {conceived_number}.'


print(logo)
print("\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


guessed_number = create_number()
# print(f"Pssst, the correct answer is {guessed_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number_of_attempts = set_difficulty(difficulty)
is_game_finish = False
while not is_game_finish:
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    message = check_number(user_guess, guessed_number)
    print(message)
    if user_guess == guessed_number:
        is_game_finish = True
    else:
        number_of_attempts -= 1
        if number_of_attempts > 0:
            print("Guess again.")
        else:
            print("You've run out of guesses, you lose.")
            is_game_finish = True

