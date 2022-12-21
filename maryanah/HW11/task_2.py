def age(age):
    if age % 2 == 0:
        print(f"Your age {age} is even.")
    else:
        print(f"Your {age} is odd.")

try:
    user_age = int(input("Enter your age: "))
    if user_age < 0:
        raise ValueError("Your age cannot be negative.")
    age(user_age)
except ValueError as e:
    print(e)

