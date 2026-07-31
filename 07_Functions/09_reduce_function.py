"""
Topic: reduce() Function
Description: Demonstrates how to use the reduce() function to
apply a function cumulatively to an iterable.
Author: Suryansh
"""

from functools import reduce

# ============================================
# Sample List
# ============================================

my_list = [1, 2, 3, 4, 5, 6]


# ============================================
# Function for reduce()
# ============================================

def multiply(x, y):
    """
    Returns the product of two numbers.
    """

    return x * y


# ============================================
# Using reduce()
# ============================================

result = reduce(multiply, my_list)

print("Product of all elements:")
print(result)