# Task3. Write a function that calculates the number of characters included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}


def calculate_char(collection_of_chars: str) -> dict:
    result_dict = {}
    for char in collection_of_chars:
        if char in result_dict:
            result_dict[char] += 1
        else:
            result_dict[char] = 1
    print(result_dict)


result = calculate_char('hello')
print(result)


