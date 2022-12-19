def count_match(string: str) -> dict:
    '''Find number of included char in string
    Parameter:string - target string
    
    Result: return dictionary (match_dict) with 
    char as key and  number of included as value'''

    #kreated dict with list of char from string
    match_dict = {key: 0 for key in string}

    #counting match of char in string
    for key in match_dict:
        count = string.count(key)
        match_dict.update({key: count})
    return match_dict


#Input string and output result
user_string = input('Enter the string: ')
result = count_match(user_string)
print(result)