# prepare zen of python string from txt file
with open('zen_of_python.txt', 'r') as file:
    zen_of_python_string = file.read()

# first task
print(zen_of_python_string)


# first part from first task
find_word_list = ["better", "never", "is"]

count_better_word = zen_of_python_string.count(find_word_list[0])
print(count_better_word)

count_never_word = zen_of_python_string.count(find_word_list[1])
print(count_never_word)

count_is_word = zen_of_python_string.count(find_word_list[2])
print(count_is_word)


# second part from first task

upper_zen_of_python_string = zen_of_python_string.upper()
print(upper_zen_of_python_string)

# third part from first task

modified_zen_of_python_string = zen_of_python_string.replace('i', '&')
print(modified_zen_of_python_string)


# second task
number = 8753

# first part from second task
number_list = [number % 10, number % 100 // 10, number % 1000 // 100, number % 10000 // 1000][::-1]
sum_of_multiply_numbers = number_list[0] * number_list[1] * number_list[2] * number_list[3]
print(sum_of_multiply_numbers)

# second part from second task
number_reverse_list = str(number)[::-1]
print(number_reverse_list)

# third part from second task
sorted_number_list = sorted(number_list)
print(sorted_number_list)

# third task

a = 'this string has reference from \'A\' variable'
b = 'this string has reference from \'B\' variable'
print(a)
print(b)

a, b = b, a
print(a)




