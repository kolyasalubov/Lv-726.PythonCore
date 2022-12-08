f1 = 0
f2 = 1

n = int(input("Enter number fibonachi:"))

print(f1, f2, end=" ")

while f2 < n:
    print(f2, end=" ")
    f1, f2 = f2, f1+f2

#    f1 = f2
#    f2 = f1+f2