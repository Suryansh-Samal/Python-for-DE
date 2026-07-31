"""
Topic: Default Arguments
Description: Demonstrates default parameter values in Python functions.
Author: Suryansh
"""

# ============================================
# Default Arguments
# ============================================

def add_numbers(x, y=10):
    """Returns the sum of x and y."""

    print(x + y)

    return x + y


# Uses the default value of y
add_numbers(10)

# Overrides the default value of y
add_numbers(10, 20)