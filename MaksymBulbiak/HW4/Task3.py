def fibonacci_func():
    """
    Print Fibonacci numbers up to the entered number n, using cycles.
    (Sequence of Fibonacci numbers 0,1,1,2,3,5,8,13 etc.)

    """
    try:
        n = int(input('Enter a number: '))
    except ValueError:
        print('\nInteger number expected for fibonacci_func  \n')
        fibonacci_func()
    m = n
    l1 = 0
    l2 = 1
    print(0)
    print(1) 
    print(1)
    while n >= 0:
        l1 , l2 = l2, l1 + l2
        n -= 1
        if m >= l1:
            print(l1)

        
fibonacci_func()
