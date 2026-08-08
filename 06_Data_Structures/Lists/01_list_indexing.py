"""
Topic: List Indexing & Slicing
Description: Demonstrates list indexing, nested lists, and string slicing.
Author: Suryansh
"""

# List containing different data types and a nested list
my_list = [1, 2, "Suryansh", ["aa", "bb", "cc"]]

# String for slicing examples
phone = "+91 954xxx7xx4"

# Accessing elements from a nested list
print(my_list[3][1])
print(my_list[3][0:2])

# Negative indexing and slicing
print(my_list[-3:])

# Accessing list elements
print(my_list[3])
print(my_list[2])

# String slicing
print(phone[-10:])
print(phone[::-2])
print(phone[::2])