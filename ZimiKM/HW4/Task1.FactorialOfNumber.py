# Inputes the user digit from keyboard
entered_number = int(input('\nInput some digit: '))
factorial = 1

# if entered_number < 0 then output - warning
if entered_number < 0:
    print('Incorrect input! Number must be > 0\n')

# if entered_number = 0 then output - 1    
elif entered_number == 0:
    print(f'\nFactorial of {entered_number}! is equal to 1\n')

# creates variable to multiplication/determinate factorial from user digit    
else:
    for element in range(1,entered_number + 1):
        factorial *= element
# outputs the answer
    print(f'\nFactorial of {entered_number} is equal to: {entered_number}! = {factorial}\n')

