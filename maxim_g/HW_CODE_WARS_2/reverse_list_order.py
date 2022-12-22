def reverse_list(l):
    reverse_counter = len(l)
    reversed_list = []
    while reverse_counter + len(l) != len(l):
        reversed_list.append(l[reverse_counter - 1])
        reverse_counter -= 1
    for index_of_list in range(len(l)):
        l[index_of_list] = reversed_list[index_of_list]
    return l


result = reverse_list([9, 2, 0, 7])
print(result)