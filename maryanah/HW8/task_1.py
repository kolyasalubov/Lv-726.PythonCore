import random


# Generate secret number.
number_sec = random.randint(1, 100)

# Create counter.
i = 1

print("Let's play. Try to guess a number in the range of 1 to 100. You have 10 attempts.")

while i <= 10:
    number_in = int(input(f"{i}. Enter the number: "))
    i += 1
    if number_in == number_sec:
        print(f"\nCongratulations! {number_in} is a secret number.")
        break
    elif number_in < number_sec:
        print("Your number is less. Try again.")
    elif number_in > number_sec:
        print("Your number is more. Try again.")
else:
    print("\nGame over... Try to play one more time.")
