def input_age():
    try:
        age = int(input("Enter your age:"))
        if age <=1:
            raise ValueError
    except ValueError:
        print("Please input a correct data")
    else:
        print(f"Your age is {age}!")

input_age()