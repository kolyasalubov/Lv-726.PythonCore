def bool_to_word(boolean):
    match boolean:
        case False:
            return 'No'
        case True:
            return "Yes"


result = bool_to_word(False)
print(result)

print(len(1))