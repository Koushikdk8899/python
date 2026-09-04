# Lab Exercise 2: Variables, Operators and Input/Output

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nResults:")

# Arithmetic operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# Relational operators
print("\nRelational Operations:")
print("a is greater than b:", a > b)
print("a is less than b:", a < b)
print("a is equal to b:", a == b)

# Logical operators
print("\nLogical Operations:")
print("(a > 0 and b > 0):", a > 0 and b > 0)
print("(a > 0 or b > 0):", a > 0 or b > 0)
print("not(a > 0):", not(a > 0))