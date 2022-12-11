# Input: string
str = 'hello'

# Convert to list.
str_list = list(str)

def char_num(str):
    """This function calculates the number of characters
    included in a given string."""
    # Create a dictionary.
    number = {char: str.count(char) for char in str}
    return number

number = char_num(str_list)
print(number)