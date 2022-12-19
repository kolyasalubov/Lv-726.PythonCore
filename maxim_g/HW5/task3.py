# Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

number_for_break = int(input("Inter the number: "))  # test data number 20

val1 = 0
val2 = 1
fibonacci_number = 0
while True:
    if (fibonacci_number + val2) > number_for_break:
        break
    fibonacci_number = val1 + val2
    val1 = val2
    val2 = fibonacci_number

print(fibonacci_number)








