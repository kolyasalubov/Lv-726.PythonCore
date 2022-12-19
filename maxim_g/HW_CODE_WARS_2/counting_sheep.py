def count_sheeps(sheep):
    count_of_sheep = len([1 for bool_val in sheep if bool_val])
    return count_of_sheep


array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]
print(count_sheeps(array1))
