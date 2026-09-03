# Problem 4: File Analyzer
# Write a Python program that reads a text file and counts:
# 1. Number of lines
# 2. Number of words
# 3. Number of characters
#
# Use exception handling to display a suitable message if the file does not exist.

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print("Number of lines:", len(lines))
    print("Number of words:", len(words))
    print("Number of characters:", characters)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)
