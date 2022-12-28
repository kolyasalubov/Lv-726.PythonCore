def list_animals(animals):
    new_list = ''
    for i in animals:
        new_list += f"{animals.index(i) + 1}. {i}\n"
    return new_list

print(list_animals(['dog', 'cat', 'elephant']))
