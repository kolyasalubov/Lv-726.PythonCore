# Author: Serhii
# Exchange values between second variables
print("==========  INIT  ==========")
first = int(input("Enter value 'first':"))
second = int(input("Enter value 'second':"))

#####################################
print("==========  Way-1 do Exchange ==========")
first = first + second
second = first - second
first = first - second
print(f"first = {first}")
print(f"second = {second}")

###################################################
print("==========  Way-2 aka Rollback  ==========")
first, second = second, first
print(f"first = {first}")
print(f"second = {second}")