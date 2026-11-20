# Retail Sales Dashboard Using CSV and Matplotlib

import csv
import matplotlib.pyplot as plt

# Creating sales data
sales = [
    ["Product", "Sales"],
    ["Laptop", 40000],
    ["Mobile", 20000],
    ["Tablet", 20000],
    ["Headphones", 30000]
]

# Writing data into CSV file
file = open("sales.csv", "w", newline="")

writer = csv.writer(file)
writer.writerows(sales)

file.close()

# Reading CSV file
file = open("sales.csv", "r")

reader = csv.reader(file)
next(reader)

products = []
amounts = []

for row in reader:
    products.append(row[0])
    amounts.append(int(row[1]))

file.close()

# Displaying sales details
print("Retail Sales Report:")

for i in range(len(products)):
    print(products[i], ":", amounts[i])

print("Total Sales:", sum(amounts))

# Creating sales chart
plt.bar(products, amounts)

plt.xlabel("Products")
plt.ylabel("Sales Amount")
plt.title("Retail Sales Dashboard")

plt.show()

# OUTPUT:
# Retail Sales Report:
# Laptop : 40000
# Mobile : 20000
# Tablet : 20000
# Headphones : 30000
# Total Sales: 110000
#
# A bar chart displaying product-wise sales will appear.
