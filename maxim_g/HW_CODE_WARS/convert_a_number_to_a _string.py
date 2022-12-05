https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/python


def number_to_string(num):
    string_number_list = [
        '1', '2', '3', '4',
        '5', '6', '7',
        '8', '9', '0', '-'
    ]
    string_numbers = ''
    for int_val in str(num):
        for str_number in string_number_list:
            if int_val == str_number:
                string_numbers += str_number
    return string_numbers
