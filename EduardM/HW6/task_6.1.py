even = []
odd = []
other = []

for number in range(1, 11):
    if number >= 2 and number % 2 == 0:
        even.append(number)
    elif number >= 3 and number % 3 == 0:
        odd.append(number)
    else:
        other.append(number)

print(f"Even numbers that are divisible by 2: {even}")
print(f"\nOdd numbers, which are divisible by 3: {odd}")
print(f"\nNumbers that are not divisible by 2 and 3: {other}")
