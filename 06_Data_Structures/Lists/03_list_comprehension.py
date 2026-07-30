"""
Topic: List Comprehension
Description: Demonstrates filtering and creating a new list using list comprehension.
Author: Suryansh
"""

# Original List
my_list = [1, 2, 3, 4, 5, 6]

# List Comprehension
new_list = [
    number
    for number in my_list
    if number % 2 == 0 and number != 6
]

print(new_list)