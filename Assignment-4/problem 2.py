# Student Data Manager Using Files

file = open("student.txt", "a")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

# Writing student details
file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll + "\n")
file.write("Marks: " + marks + "\n")
file.write("-------------------\n")

file.close()

print("\nStudent details saved successfully!")

# Reading student records
file = open("student.txt", "r")

print("\nStudent Records:")

for line in file:
    print(line, end="")

file.close()

# OUTPUT:
# Enter student name: Koushik
# Enter roll number: 65
# Enter marks: 96
#
# Student details saved successfully!
#
# Student Records:
# Name: koushik
# Roll Number: 65
# Marks: 96
# -------------------
