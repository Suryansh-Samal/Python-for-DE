"""
Topic: Exception Handling in Functions
Description: Demonstrates using try, except, finally, and return statements inside functions.
Author: Suryansh
"""

# ============================================
# Example 1
# ============================================

def check_even(x):
    """Checks whether a number is even."""

    try:

        if x % 2 == 0:
            print("Hello World!")
            return 1

    except Exception as e:
        print(f"The error occurred: {e}")

    finally:
        print("This is the end of the code")


check_even(9)


# ============================================
# Example 2
# ============================================

def return_example(x):
    """
    Statements after the return keyword
    are never executed.
    """

    return x

    print(x)   # Unreachable code


return_example(2)