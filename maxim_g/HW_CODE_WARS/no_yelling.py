https://www.codewars.com/kata/587a75dbcaf9670c32000292/train/python

def filter_words(st):
    # return st.capitalize() # easy option
    return st[0].title()+st[1:].lower()

print(filter_words('HELLO world!'))