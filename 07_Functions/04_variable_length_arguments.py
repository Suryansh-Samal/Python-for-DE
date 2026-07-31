"""
Topic: Variable-Length Arguments
Description: Demonstrates *args and **kwargs.
Author: Suryansh
"""

# ============================================
# *args
# ============================================

def calculate_sum(*numbers):
    """Returns the sum of all positional arguments."""

    print(numbers)

    return sum(numbers)


result = calculate_sum(10, 20, 30, 40)

print(result)


# ============================================
# **kwargs
# ============================================

def display_details(**details):
    """Displays keyword arguments."""

    print(details)

    print(details.keys())

    return details


display_details(
    a=10,
    b=20,
    c=30,
    d=40
)