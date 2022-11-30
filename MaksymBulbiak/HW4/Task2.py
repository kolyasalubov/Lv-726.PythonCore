def type_changing():
    
    lst = []


    try:
        num = int(input('Enter number of elemnets in list: '))

        for i in range(0,num):
            elm = int(input('Please, enter elements of integer type:\n'))
            lst.append(elm)

    except ValueError:
        print('\nInteger elements expected for type changing operation\n')
        type_changing()

    print(f'Entered list {lst}')
    float_lst = []
    for i in lst:
        float_lst.append(float(i))
    print(f'Changed list {float_lst}')

    
type_changing()
