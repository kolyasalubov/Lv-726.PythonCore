def solution(number):
    summa = 0
    for value in range(1,number+1):
        if value%3 == 0 or value%5 == 0:
            summa += value
    return summa
    

print(solution(15))

# another resolve:
# return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)