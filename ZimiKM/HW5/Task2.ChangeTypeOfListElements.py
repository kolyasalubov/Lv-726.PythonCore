# creates a list that contains elements of integer type
some_list = (1, 2, 12, 5, 7, 10, 21)

# creates a new empty list 
new_list = [] 
# changes the type of list elements in a loop
for element in some_list:
    new_list.append(float(element))

print(f'\nThe new list with float numbers looks like this:\n{new_list}\n')