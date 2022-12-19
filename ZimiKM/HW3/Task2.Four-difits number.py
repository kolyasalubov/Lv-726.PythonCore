# input four-digits number
some_number = input('Input some four-digits number = ')

# find the product of the digits of this number.
multi_number = 1
for element in some_number:
    multi_number *= int(element)

print('The product of the digits of this number = ', multi_number)

# output the number in reverse order
print('Number in reverse order = ', some_number[::-1])

# output sorted number
sorted_some_number = sorted(some_number)
print('Sorted number =', ''.join(sorted_some_number))