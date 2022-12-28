def range_gen(num1, num2):
    while num1 < num2:
        yield num1
        num1 += 1



first_call = range_gen(3, 10)
print(first_call)

print('First range: ', end='')
for num in first_call:
    print(num, end=' ')

second_call = range_gen(5, 7)

print("\nSecond range: ", end='')
for num in second_call:
    print(num, end=' ')