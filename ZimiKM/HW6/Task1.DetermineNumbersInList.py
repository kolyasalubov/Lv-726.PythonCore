# Create empty lists
even_numbers = []
odd_numbers = []
other_numbers =[]

# Generates and iterates trought list of 10 elements from 1 to 10
for element in range(1,11):
# separates even numbers
    if element %2 == 0:
        even_numbers.append(element) 
# separates odd numbers, which are divisible by 3
    if element % 2 == 1 and element % 3 == 0:
        odd_numbers.append(element)
# separates numbers that are not divisible by 2 and 3
    if element % 2 == 1 and element % 3 != 0:
        other_numbers.append(element)
# outputing results
print(f'''even numbers - {even_numbers}
odd numbers, which are divisible by 3 - {odd_numbers}
numbers that are not divisible by 2 and 3 - {other_numbers}''' )
