#match_case_calculator.py
#Prompt for User Input numbers:
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
#Prompt for User Input operation:
operation = input("Choose the operation (+, -, *, /):")
#Perform the Calculations
match operation:
    case '+':
        result = num1 + num2
        print("The result is [result].")
    case '-':
        result = num1 - num2
        print("The result is [result].")
    case '*':
        result = num1 * num2
        print("The result is [result].")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print("The result is [result].")
        else:
            print("Error")
    case _:
        print("invalid choice of operation")
