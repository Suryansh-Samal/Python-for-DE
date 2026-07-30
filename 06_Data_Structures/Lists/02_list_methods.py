"""
Topic: List Methods
Description: Demonstrates commonly used list methods.
Author: Suryansh
"""

# Sample List
my_list = [1, 2, "Suryansh", ["aa", "bb", "cc"]]

# Append
my_list.append("Python")
print(my_list)

# Insert
my_list.insert(1, "Java")
print(my_list)

# Pop
my_list.pop()
print(my_list)

# Remove
my_list.remove("Java")
print(my_list)

# Iterate in reverse order
print("Reverse Iteration:")

for item in reversed(my_list):
    print(item)

# Reverse the original list
my_list.reverse()

print("Reversed List:")
print(my_list)