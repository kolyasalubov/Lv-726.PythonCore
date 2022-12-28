def bread(func):
    def inner(*args):
        print("<\\^^^^^^^/>")
        func(*args)
        print("<\\_______/>")
    return inner


def toppings(func):
    def inner(*args):
        print("# tomato #")
        func(*args)
        print("~ salad ~")
    return inner

@bread
@toppings
def sandwich(filling):
    print(f"- {filling} -")

my_sandwich = sandwich('meat')