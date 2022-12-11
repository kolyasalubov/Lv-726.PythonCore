def calc_add(a, b):
    return a+b


def calc_sub(a, b):
    return a-b


def calc_mult(a, b):
    return a*b


def calc_div(a, b):
    return a/b


def calculator():
    procedure = input('What do you want to do? Input: "+" if add, "-" if sub, "*" if mult or "/" if div:')
    a = int(input('input a='))
    b = int(input('input b='))
    if procedure == '/':
        while b == 0:
            b = int(input('You input wrong value! b!=0 !!!.Try again: b='))
        result = calc_div(a,b)    
    elif procedure == '+':
        result = calc_add(a,b)
    elif procedure == '-':
        result = calc_sub(a,b)
    else:
        result = calc_mult(a,b)
    return result


print(calculator())


