#Calculator

while True:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    Operator = input("Enter operator (+, -, *, /): ")

    if Operator == "+":
        print(num1 + num2)
    elif Operator == "-":
        print(num1 - num2)
    elif Operator == "*":
        print(num1 * num2)
    elif Operator == "/":
        print(num1 / num2)
    else:
        print("Invalid Operator")

        

