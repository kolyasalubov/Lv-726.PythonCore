from random import randint

n = randint(0, 100)
i = 0

print("Try to guess a number in the range of 1 to 100. You have 10 attempts.")

while True:
    a = int(input(f"Enter the number: "))
    if a == n:
        print(f'\nYou win! {a} is a secret number.')
        break
    if a < n:
        print('The mystery number is bigger than')
    else:
        print('The number is less than')
    i += 1

    if i == 10:
        print(f'You have lost. The number you have guessed {n}')
        break
