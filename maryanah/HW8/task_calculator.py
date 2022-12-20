import calculator

while True:
    op = int(input("Choose operation (1 - add"
                  "/ 2 - subtraction"
                  "/ 3 - multiplication"
                  "/ 4 - division): "))
    if op == 1 or op == 2 or op == 3 or op == 4:
        break
    else:
        print("Choose one of the above operations.")
        continue

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if op == 1:
    result = calculator.add(num1, num2)
    print(f"Result: {result}")

elif op == 2:
    result = calculator.subtraction(num1, num2)
    print(f"Result: {result}")

elif op == 3:
    result = calculator.multiplication(num1, num2)
    print(f"Result: {result}")

elif op == 4:
    result = calculator.division(num1, num2)
    print(f"Result: {result}")
