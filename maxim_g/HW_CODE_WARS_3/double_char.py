
def double_char(s):
    double_str = ''
    for val in s:
        double_str += val*2
    return double_str


result = double_char('Hello world!')
print(result)  # HHeelllloo  wwoorrlldd!!