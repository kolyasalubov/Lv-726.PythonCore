# exchange of variable values
some_value1 = 555
print(f'1-st variable = {some_value1}')
some_value2 = "data"
print(f'2-d variable = {some_value2}')

some_value1, some_value2 = some_value2, some_value1

print(f'After swaping 1-st variable = {some_value1}, and 2-d variable = {some_value2}')