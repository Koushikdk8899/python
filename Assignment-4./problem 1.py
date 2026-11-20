# Log File Reader Program

# Creating a log file
file = open("log.txt", "w")

file.write("System started successfully\n")
file.write("User logged in\n")
file.write("File opened\n")
file.write("System backup completed\n")

file.close()

# Reading the log file
file = open("log.txt", "r")

print("Log File Contents:")

for line in file:
    print(line, end="")

file.close()

# OUTPUT:
# Log File Contents:
# System started successfully
# User logged in
# File opened
# System backup completed
