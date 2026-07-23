#3 number Calculator

while True:
    num1 = float(input("Enter number 1: "))
    operator1 = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter number 2: "))
    operator2 = input("Enter operator (+, -, *, /): ")
    num3 = float(input("Enter number 3: "))
    result = 0

    if operator1 == "+":
        result = num1 + num2
    elif operator1 == "-":
        result = num1 - num2
    elif operator1 == "*":
        result = num1 * num2
    elif operator1 == "/":
        result = num1 / num2

    #2nd operator
    if operator2 == "+":
        print(result + num3)
    elif operator2 == "-":
        print(result - num3)
    elif operator2 == "*":
        print(result * num3)
    elif operator2 == "/":
        print(result / num3)
    
    else:
        print("Invalid Operator ./.")
     



