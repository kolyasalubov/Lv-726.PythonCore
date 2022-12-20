f1 = 1
f2 = 1

# while

n = int(input("Write a number:"))

print("\nFibonacci numbers:", f1, f2, end=" ")
while n > 2:
    f1, f2 = f2, f1 + f2
    print(f2, end = ' ')
    n -= 1


#for

n = int(input("Write a number:"))

print("\nFibonacci numbers:", f1, f2, end=" ")
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end = ' ')
