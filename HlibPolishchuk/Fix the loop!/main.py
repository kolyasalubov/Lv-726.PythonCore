def list_animals(animals):
    list = ''
    i=0
    for elements in animals:
        list += str(i + 1) + '. ' + elements + '\n'
        i+=1
    return list