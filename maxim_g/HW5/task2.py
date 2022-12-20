from random import randint as random_number

# Create a list that contains elements of integer type, then
# use the loop to change the type of these elements to a floating
# type.
# (Hint: use the built-in float () function).


random_number_list = [random_number(1,10) for number in range(10)]
print(random_number_list)

counter = 0
while counter < len(random_number_list):
    random_number_list[counter] = float(random_number_list[counter])
    counter += 1
print(random_number_list)