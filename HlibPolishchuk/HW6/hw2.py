#2


guess = input("Write your login:")
login = 'First'
count = 0

while guess != login:
    count += 1
    print("Incorrect login")
    guess = input("Try again:")

if guess == login:
    print("\nCongratulations your login is accepted!")

print("\nYou spend", count, "trying")