even = []

for i in range(1, 11):
    if i%2==0:
        even.append(i)
print("Even numbers:", even)

#################################################

odd = []

for i in range(1, 11):
    if i % 2 == 1 and i % 3 == 0:
        odd.append(i)
print("\nOdd numbers, which are divisible by 3:", odd)

########################################

other = []

for i in range(1, 11):
    if not i % 2 == 0 and not i % 3 == 0:
        other.append(i)
print("\nNumbers that are not divisible by 2 and 3:", other)

########################################

