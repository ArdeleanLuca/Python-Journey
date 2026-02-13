# Calculator in Python
number1 = float(input("Enter the first number: "))
operation = input("Enter the operator (+ - * /): ")
number2 = float(input("Enter the second number: "))

if operation == "+":
    result = number1 + number2
    print(round(result))
elif operation == "-":
    result = number1 - number2
    print(round(result))
elif operation == "*":
    result = number1 * number2
    print(round(result))
elif operation == "/":
    result = number1 / number2
    print(round(result))
else:
    print("Invalid operation, please choose a valid one!")
