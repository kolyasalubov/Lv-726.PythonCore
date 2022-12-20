def solution(number):
    sum_of_m = 0
    for int_n in range(number):
        match not bool(int_n % 5 == 0 or int_n % 3 == 0):
            case False:
                sum_of_m += int_n
            case True:
                continue
    return sum_of_m


result = solution(15)
print(result)

