"""
Topic: filter() Function
Description: Demonstrates how to use the built-in filter() function
to filter elements from an iterable.
Author: Suryansh
"""

# ============================================
# Sample List
# ============================================

my_list = [1, 2, 3, 4, 5, 6]


# ============================================
# Function to Filter Even Numbers
# ============================================

def is_even(number):
    """
    Returns True for even numbers.
    """

    if number % 2 == 0:
        return True

    return False


# ============================================
# Using filter()
# ============================================

result = list(filter(is_even, my_list))

print(result)