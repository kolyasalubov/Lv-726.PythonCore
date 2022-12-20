def addition(numbers,sum=0):
    for i in numbers:
        sum+=i
    return sum


def subtraction(numbers):
    sub = numbers[0]
    for i in numbers[1:]:
        sub-=i
    return sub


def multiplication(numbers,mul=1):
    for i in numbers:
        mul*=i
    return mul


def division(numbers ,div=0):
    div = numbers[0] / numbers[1] 
    return div





