# JSON-Based Log File Analyzer

import json

# Creating log messages
logs = [
    {"message": "System started", "status": "INFO"},
    {"message": "User logged in", "status": "INFO"},
    {"message": "File not found", "status": "ERROR"},
    {"message": "System backup completed", "status": "INFO"}
]

# Writing logs into JSON file
file = open("logs.json", "w")

json.dump(logs, file, indent=4)

file.close()

# Reading JSON file
file = open("logs.json", "r")

data = json.load(file)

file.close()

# Displaying log records
print("Log File Analysis:")

for log in data:
    print(log["status"], "-", log["message"])

# Counting log entries
total = len(data)
errors = 0

for log in data:
    if log["status"] == "ERROR":
        errors = errors + 1

print("\nTotal Log Entries:", total)
print("Total Errors:", errors)

# OUTPUT:
# Log File Analysis:
# INFO - System started
# INFO - User logged in
# ERROR - File not found
# INFO - System backup completed
#
# Total Log Entries: 4
# Total Errors: 1
