words = list("hello")

def char_num(words):
        number = {char: words.count(char) for char in words}
        return number

number = char_num(words)
print(number)







