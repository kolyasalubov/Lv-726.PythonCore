number = int(input("Enter the number: "))

if number == 0:
    result = 1
else:
    result = 1
    for num in range(1, number + 1):
        result = result * num

print(result)
