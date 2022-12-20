def char_count(string: str) -> dict:
    string = string.lower()
    return {ch: string.count(ch) for ch in string}


print(char_count("AAabbBc"))
