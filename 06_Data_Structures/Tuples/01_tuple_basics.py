"""
Topic: Tuple Basics
Description: Demonstrates tuple creation, indexing, and converting a tuple to a list.
Author: Suryansh
"""

# ============================================
# Creating a Tuple
# ============================================

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Display the tuple
print(my_tuple)


# ============================================
# Accessing Tuple Elements
# ============================================

# Access the last element
print(my_tuple[9])


# ============================================
# Converting Tuple to List
# ============================================

# Tuples are immutable, so convert to a list
my_tuple_list = list(my_tuple)

# Add a new element to the list
my_tuple_list.append(11)

# Display the updated list
print(my_tuple_list)