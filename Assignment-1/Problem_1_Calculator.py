# Problem 1: Simple Calculator
# Write a Python program that accepts two numbers and an operator (+, -, *, /)
# from the user and displays the result.
#
# Requirements:
# 1. Use input() to read the values.
# 2. Use conditional statements to select the operation.
# 3. Handle division by zero appropriately.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")
