n1 = 2
n2 = 1


def larger_num(two_numbers: list) -> int | float:
    """
    :param two_numbers: it's a list with two numbers
    :return: max number
    """
    return max(two_numbers)


print(larger_num([n1, n2]))
