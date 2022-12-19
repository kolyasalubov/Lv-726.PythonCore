def are_you_playing_banjo(name):
    match name[0]:
        case 'R' | 'r':
            return f"{name} plays banjo"
    return f"{name} does not play banjo"


result1 = are_you_playing_banjo("Roman")
print(result1)

result2 = are_you_playing_banjo("rikki")
print(result2)