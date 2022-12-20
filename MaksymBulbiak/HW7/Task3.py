

def calc_func(wrd):
    """
    (str) -> dict

    Write a function that calculates the number of characters 
    included in a given string

    Example (Input --> Output)

    "hello" --> {"h":1, "e":1,"l":2,"o":1}

    >>> calc_func("Thanks")
    {'t': 1, 'h': 1, 'a': 1, 'n': 1, 'k': 1, 's': 1}
    >>> calc_func("Pneumonoultramicroscopicsilicovolcanoconiosis")
    {'p': 2, 'n': 4, 'e': 1, 'u': 2, 'm': 2, 'o': 9, 'l': 3, 't': 1, 'r': 2,\
 'a': 2, 'i': 6, 'c': 6, 's': 4, 'v': 1}
    >>> calc_func("HipPopotOmonstroSesquiPPedaliophobia")
    {'h': 2, 'i': 4, 'p': 6, 'o': 7, 't': 2, 'm': 1, 'n': 1, 's': 3, 'r': 1,\
 'e': 2, 'q': 1, 'u': 1, 'd': 1, 'a': 2, 'l': 1, 'b': 1}
    """
    n_wrd = wrd.lower()
    res = {}
    for i in n_wrd:
        if i not in res:
            res[i] = 1
        else:
            res[i]+= 1
    return res



if __name__ == "__main__":
    import doctest
    doctest.testmod()