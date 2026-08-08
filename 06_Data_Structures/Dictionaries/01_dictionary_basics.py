"""
Topic: Dictionary Basics
Description: Demonstrates dictionary creation, accessing values, updating values,
nested dictionaries, and commonly used dictionary methods.
Author: Suryansh
"""

# ============================================
# Creating Dictionaries
# ============================================

my_dictionary = {
    "name": "Suryansh",
    "age": 18,
    "city": "Delhi",
    "demo": {
        "a": 1,
        "b": 2
    }
}

# Empty Dictionary
empty_dictionary = {}

# Display the dictionary
print(my_dictionary)


# ============================================
# Updating Dictionary Values
# ============================================

my_dictionary["age"] = 21

print(my_dictionary)

# ============================================
# Adding Item
# ============================================

my_dictionary["Domain"] = 'Data Engineering'

print(my_dictionary)


# ============================================
# Accessing Dictionary Values
# ============================================

# Access a value
print(my_dictionary["name"])

# Access a value from a nested dictionary
print(my_dictionary["demo"]["a"])

# Access all key-value pairs from nested dictionary
print(my_dictionary["demo"].items())


# ============================================
# Dictionary Methods
# ============================================

# Remove a key-value pair
my_dictionary.pop("city")

print(my_dictionary)

# Display all keys
print(my_dictionary.keys())

# Display all values
print(my_dictionary.values())

# Display all key-value pairs
print(my_dictionary.items())