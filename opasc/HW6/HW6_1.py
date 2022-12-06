a = []
b = []
c = []

for number in range(11):
    if number >= 2 and number % 2 == 0:
        a.append(number)
#        print(f"Even numbers that are divisible by 2: {a}")
    elif number >= 3 and number % 3 == 0:
        b.append(number)
#        print(f"Odd numbers, which are divisible by 3: {b}")
    else:
        c.append(number)
#        print(f"Numbers that are not divisible by 2 and 3: {c}")

print(f"Even numbers that are divisible by 2: {a}",
      f"Odd numbers, which are divisible by 3: {b}",
      f"Numbers that are not divisible by 2 and 3: {c}",
      sep="\n")
