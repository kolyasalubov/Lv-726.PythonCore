def solution(number):
    sum = 0
    if number <= 0:
        return sum
    for num in range(1, number):
        if num % 3 == 0:
            sum += num
        elif num % 5 == 0:
            sum += num
    return sum
