# inputing the Fibonacci number trought keyboard
user_number = int(input('\nInput the number of numbers in the Fibonacci sequence: '))

# create first two elements of Fibonacci sequence and counter
previous_fibonacci_number = 0
fibonacci_number = 1
counter = 1

# if user_number < 0 - notify the user about incorrect input
if user_number <= 0:
    print('\nWarning!\nInput number must be > 0\n')

# if user_number = 1, there is only one Fibonacci number:
elif user_number == 1:
    print(f'\nFibonacci number - {previous_fibonacci_number}\n')

# otherwise generates a Fibonacci sequence for user_number.
else:
    while counter <= user_number:
        print(f'Fibonacci number {counter} = {previous_fibonacci_number}')
        next_fibonacci_number = previous_fibonacci_number + fibonacci_number
        previous_fibonacci_number = fibonacci_number
        fibonacci_number = next_fibonacci_number
        counter += 1

    

