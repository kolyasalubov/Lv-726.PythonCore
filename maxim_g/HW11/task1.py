
def even_or_odd_age(age):
    try:
        if age > -1:
            if not age % 2:
                print(f"The number {age } of your age is even!")
            elif age % 2:
                print(f"The number {age} of your age is odd!")
        else:
            raise ValueError
    except ValueError:
        print(f"You interred negative number _____ {age} _____ Try again!")


user_ag = int(input("Inter your age for calculate, even or odd: "))
even_or_odd_age(user_ag)