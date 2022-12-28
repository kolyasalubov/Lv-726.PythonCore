import re

explanatory_list = [
    'At least 1 letter between [a-z]',
    'At 1 letter between [A-Z]',
    'At least 1 number between [0-9]',
    'At least 1 character from [$#@]',
    'Maximum length 16 characters',
    'Minimum length 6 characters'

]


def password_validator(password):
    rule1 = re.findall('[a-b]', password)
    rule2 = re.findall('[A-Z]', password)
    rule3 = re.findall('[0-9]', password)
    rule4 = re.findall('[$#@]', password)
    password_rule = [
        len(rule1) > 0,
        len(rule2) == 1,
        len(rule3) > 0,
        len(rule4) > 0,
        len(password) <= 16,
        len(password) >= 6,
    ]
    info_message = ''
    counter = 0
    for val in password_rule:
        if not val:
            info_message += f'{explanatory_list[counter]}\n'
        counter += 1
    if min(password_rule) == 1:
        return 'The entered password has passed all the criteria of the rules'
    else:
        return info_message


user_password = input('Please enter your password: ')
print(password_validator(user_password))