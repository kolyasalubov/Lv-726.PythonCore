

def list_animals(animals):
    string = ''
    for i in animals:
        string += str(animals.index(i) + 1) + '. ' + animals[animals.index(i)] + '\n'
    return string


print(list_animals(['dog', 'cat', 'elephant' ]))


# Test data
print('1. dog\n2. cat\n3. elephant\n')