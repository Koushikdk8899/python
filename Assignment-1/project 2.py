print("UNIT CONVERTER")
print("1. Kilometers to Meters")
print("2. Meters to Kilometers")
print("3. Kilograms to Grams")
print("4. Grams to Kilograms")
print("5. Celsius to Fahrenheit")
print("6. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))
value = float(input("Enter value: "))

if choice == 1:
    result = value * 1000
    print("Result:", result, "meters")

elif choice == 2:
    result = value / 1000
    print("Result:", result, "kilometers")

elif choice == 3:
    result = value * 1000
    print("Result:", result, "grams")

elif choice == 4:
    result = value / 1000
    print("Result:", result, "kilograms")

elif choice == 5:
    result = (value * 9 / 5) + 32
    print("Result:", result, "Fahrenheit")

elif choice == 6:
    result = (value - 32) * 5 / 9
    print("Result:", result, "Celsius")

else:
    print("Invalid choice")