first = 'orange'
second = 'apple'

print(f"Before changing:\nFirst value: {first}\nSecond value: {second}")

first, second = second, first

print(f"\nAfter changing:\nFirst value: {first}\nSecond value: {second}")
