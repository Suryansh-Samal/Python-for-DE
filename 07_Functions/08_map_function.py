"""
Topic: map() Function
Description: Demonstrates how to use the built-in map() function
to transform elements of an iterable.
Author: Suryansh
"""

# ============================================
# Sample List
# ============================================

my_list = [1, 2, 3, 4, 5]


# ============================================
# Function to Square Numbers
# ============================================

def square(number):
    """
    Returns the square of a number.
    """

    return number * number


# ============================================
# Using map() with a List
# ============================================

result = list(map(square, my_list))

print("Squared List:")
print(result)


# ============================================
# Calling the Function Directly
# ============================================

result = square(9)

print("\nSquare of 9:")
print(result)


# ============================================
# Using map() with a Tuple
# ============================================

result = tuple(map(square, my_list))

print("\nSquared Tuple:")
print(result)