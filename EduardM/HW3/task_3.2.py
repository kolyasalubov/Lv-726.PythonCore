number = 4312

# 1
mul_all_num = int(str(number)[0]) * int(str(number)[1]) * int(str(number)[2]) * int(str(number)[3])
print(mul_all_num)

# 2
print(int(str(number)[::-1]))

# 3
print("".join([str(n) for n in
                    sorted([int(num) for num in str(number)])]))
