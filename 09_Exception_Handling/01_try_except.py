"""
Topic: Try-Except
Description: Demonstrates basic exception handling using try and except.
Author: Suryansh
"""

# ============================================
# Basic Try-Except Example
# ============================================

x = "10"

try:

    if x > 10:
        print("x is greater than 10")

    else:
        print("x is less than or equal to 10")

except:
    print("x is not a number")

print("This is the end of the program")