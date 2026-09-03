# Problem 3: Student Grading System
# Write a Python program that stores student names and marks in a dictionary.
# Calculate the grade for each student based on the following rules:
#
# 90-100 : A
# 75-89  : B
# 60-74  : C
# 50-59  : D
# Below 50 : F
#
# Display each student's name, marks, and grade.

students = {
    "Kiran": 86,
    "Rahul": 72,
    "Anu": 94,
    "Meena": 48
}

for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}: Marks = {marks}, Grade = {grade}")
