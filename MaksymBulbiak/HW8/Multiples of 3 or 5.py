def solution(number):
    result = 0
    if number > 0:
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                result += i
    else:
        return result
    return result