

def find_largest_number(numbers):
    """
    This function returns the largest number from list
    :param numbers:
    :return string:
    """
    large_number = numbers[0]
    for val in numbers:
        if large_number < val:
            large_number = val
    return f'number {large_number} is the largest'


result = find_largest_number([17, 20])
print(result)