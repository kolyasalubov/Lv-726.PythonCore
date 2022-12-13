# https://www.codewars.com/kata/reversing-words-in-a-string

def reverse(st):
    reverse_list = ' '.join(st.split()[::-1])
    return reverse_list

