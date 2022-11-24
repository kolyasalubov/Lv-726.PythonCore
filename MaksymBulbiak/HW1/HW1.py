def open_func():
    file = 'C:\\Users\\Max\\Desktop\\first\\Lv-726.PythonCore\\HW1\\ZenOfPython.txt'
    open_file = open(file,'r')
    read_file = open_file.read()
    


    def word_searching():
        new_file = read_file.lower().split()
        countBetter = 0
        countNever = 0
        countIs = 0
        for word in new_file:
            if 'better' == word:
                countBetter += 1
            elif 'never' == word:
                countNever += 1
            elif 'is' == word:
                countIs += 1
        print(f"\nTask 1.1\nthe word 'better' happens {countBetter} times, the word 'never' {countNever} times, and the word 'is' {countIs} times.\n")

    word_searching()


    def uppercase_func():
        new_file = read_file.upper()
        print("Task 1.2\n",new_file)

    uppercase_func()


    def character_replacement():
        new_file = read_file.replace('i','&')
        print("\nTask 1.3\n",new_file)
    
    character_replacement()


    def numbers(num):
        if len(num) != 4:
            numbers(input("\nTask 2\nTry again to write a four-digit number!\n"))
        else:
            product = 0
            for i in num:
                product += int(i)
            print("\nTask 2.1\n Product:",product)
        print("\nTask 2.2\n Reverse:",num[::-1])
        sorted_num = sorted(num)
        sorted_num = ''.join(sorted_num)
        print("\nTask 2.3\n Sorted:",sorted_num)


    numbers(input("\nWrite a four-digit number!\n"))


    def substitution_of_variables(var1,var2):
        var1 , var2 = var2, var1
        print(f"\nTask 3\nFirst variable:\n{var1}\n\nSecond variable:\n{var2}\n")

    substitution_of_variables(input("\nWrite first variable\n"),input("\nWrite second variable\n"))

open_func()
