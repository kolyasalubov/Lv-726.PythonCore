# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3

START = 1
STOP = 11

divisible_rules = [
            (lambda value: value % 2 == 0),
            (lambda value: value % 3 != 0),
            (lambda value: value % 2 != 0 and value % 3 != 0),
                  ]
name_operation_list = ["divisible by 2", 'divisible by 3', 'not divisible by 2 and 3']
result_dict = {}

for operation in name_operation_list:
    index_for_lambda = name_operation_list.index(operation)
    for val in range(START, STOP):
        if divisible_rules[index_for_lambda](val):
            if operation in result_dict:
                result_dict[operation].append(val)
            else:
                result_dict[operation] = [val]
for key in result_dict:
    print(f"{key}:  {result_dict[key]}")
