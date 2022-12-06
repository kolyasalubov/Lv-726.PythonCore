# # #Solution with List Coprehension for an example from a lecture assignment.


# a = [int(input('Enter next numbers: ')) for item in range(int(input('Enter number: ')))]

# print(max(a))
# print(min(a))




# Task 1
def calculation_func():
    """
    In the range from 1 to 10 determine 
    • even numbers that are divisible by 2,
    • odd numbers, which are divisible by 3,
    • numbers that are not divisible by 2 and 3.
    """
    even_num = [i for i in range(1,10) if i % 2 == 0]
    print('Even numbers: ',even_num)

    odd_num = [i for i in range(1,10) if i % 3 == 0 and  i % 2 == 1]
    print('Odd numbers: ',odd_num)

    div_num = [i for i in range(1,10) if not i % 3 == 0 and not i % 2  == 0]
    print('Not div numbers: ',div_num)


calculation_func()
