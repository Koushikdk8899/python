# CSV-Based Payroll Management System

import csv

# Creating CSV file
file = open("payroll.csv", "w", newline="")

writer = csv.writer(file)

writer.writerow(["Employee Name", "Basic Salary", "Bonus", "Total Salary"])

n = int(input("Enter number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    salary = int(input("Enter basic salary: "))
    bonus = int(input("Enter bonus: "))

    total = salary + bonus

    writer.writerow([name, salary, bonus, total])

file.close()

# Reading CSV file
file = open("payroll.csv", "r")

reader = csv.reader(file)

print("\nPayroll Records:")

for row in reader:
    print(row)

file.close()

# OUTPUT:
# Enter number of employees: 2
# Enter employee name: Raju
# Enter basic salary: 20000
# Enter bonus: 3000
# Enter employee name: Karthik
# Enter basic salary: 25000
# Enter bonus: 5000
#
# Payroll Records:
# ['Employee Name', 'Basic Salary', 'Bonus', 'Total Salary']
# ['Raju', '20000', '3000', '23000']
# ['Karthik', '25000', '5000', '30000']
