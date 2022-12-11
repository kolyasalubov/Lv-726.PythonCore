def count_mach(input_string: st) -> dict:
    mach_dict = {key: 0 for key in input_string}

    for key in mach_dict:
        count = input_string.count(key)
        mach_dict.update({key: count})
    return mach_dict


print(count_mach('hello'))