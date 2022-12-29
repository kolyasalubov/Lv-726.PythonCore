def main(age):
    if age % 2 == 0:
        print(f"Your age {age} is even")
    else:
        print(f"Your age {age} is odd")

try:
    user = int(input("Write your age:"))
    if user < 0:
        raise ValueError
    main(user)
except ValueError:
    print("Please input a correct data!")


