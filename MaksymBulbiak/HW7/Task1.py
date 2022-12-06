def largest_num(*args):
    """
    (tuple of int) -> int , int

    Write a function that returns the largest number of entered 
    numbers 

    >>> largest_num(2,3,122,4,56)
    122
    >>> largest_num(5,3,12,4,43,56,43,777)
    777
    >>> largest_num(5,3)
    5
    """
    num = 0
    for i in args:
        if i > num:
            num = i
    return(num)
         
print("The largest number is:",largest_num(5,3))


if __name__ == "__main__":
    import doctest
    doctest.testmod()