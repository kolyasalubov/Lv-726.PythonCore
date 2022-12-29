def input_even_odd():
    try:
        ipt = int(input("Enter integer number :"))
        if isinstance(ipt, int) == True:
            print(f"Your numbers is {ipt}")
    except ValueError:
        print("Value Error! Please enter integer number!")

input_even_odd()