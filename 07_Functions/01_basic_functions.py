"""
Topic: Basic Functions
Description: Demonstrates function definition, function calls, and return statements.
Author: Suryansh
"""

# ============================================
# Basic Function
# ============================================

x = 10


def my_func():
    """Returns the value of x increased by 5."""

    print(x)

    return x + 5


# Function Call
value = my_func()

print(value)