def sum_two_smallest_numbers(numbers):
    new_list = (sorted(numbers))
    new_list1 = []  # про всяк випадок ще буде список підрукою відсортований
    for i in new_list:
        if i > 0 and isinstance(i, int):
            new_list1.append(i)  
    return new_list1[0] + new_list1[1]
    #your code here