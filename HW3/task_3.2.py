# Author: Serhii
# HW3 task 3.2
# 4-digit numbers calculating
f4_number = input("Enter four-digit number:")

# Multiplication of every sign sequencently
multiply = 1
print("Way-1")
for y in f4_number:
    multiply *= int(y)
print(f"Multiplication of every sign sequencently is {multiply}")
print("Way-2")
multiply = int(f4_number[0]) * int(f4_number[1]) * int(f4_number[2]) * int(f4_number[3])
print(f"Multiplication of every sign sequencently is {multiply}")

# Reverse order of digits
print("Way-1")
reversed_f4_number_in_string = "".join(reversed(f4_number))
print(f"Reversed order of digits - {reversed_f4_number_in_string}")
print("Way-2")
reversed_f4_number_in_string = f4_number[3] + f4_number[2] + f4_number[1] + f4_number[0]
print(f"Reversed order of digits - {reversed_f4_number_in_string}")

# Sort digits' sequence
print("Way-1")
sorted_sequence = "".join(sorted(f4_number))
print(f"Sorted digits' sequence - {sorted_sequence}")
print("Way-2")
sorted_sequence = sorted(f4_number)
print(f"Sorted digits' sequence - {sorted_sequence}")
