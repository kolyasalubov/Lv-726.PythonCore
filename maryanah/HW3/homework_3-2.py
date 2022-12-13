number = 5138
print(f"Original number: {number}")

number_str = str(number)
number_list = list(number_str)

multiplication = int(number_list[0]) * int(number_list[1])\
                 * int(number_list[2]) * int(number_list[3])
print(f"\nDigits multiplication: {multiplication}")

number_list.reverse()
number_str_reversed = ''.join(number_list)
print(f"Reversed number: {number_str_reversed}")

number_list.sort()
number_str_sorted = ''.join(number_list)
print(f"Sorted number: {number_str_sorted}")
