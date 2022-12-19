import doctest

def number_to_string(num):
    """(int) -> str

    Convert a Number to String!

    >>> number_to_string(123)
    '123'

    >>> number_to_string(-123)
    '-123'

    >>> number_to_string(-12*3)
    '-36'

    >>> number_to_string(2**3)
    '8'
    """
    return str(num)


if __name__ == "__main__":
    doctest.testmod()