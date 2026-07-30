"""
Topic: String Methods
Description: Demonstrates commonly used string methods in Python.
Author: Suryansh
"""

x = "Suryansh"

# Case Conversion
print(x.upper())
print(x.lower())
print(x.capitalize())

# Replace characters
print(x.replace("sh", "z"))

# Split string
y = "hello-Suryansh"
my_list = y.split("-")
print(my_list)

# Startswith & Endswith
file = "raw_data.csv"

if file.endswith(".csv"):
    print("This is a CSV file")

if file.startswith("raw"):
    print("This is a raw data file")

# Count occurrences
statement = "hey Suryansh, how are you Suryansh?, How was your day Suryansh?"

print(statement.count("Suryansh"))