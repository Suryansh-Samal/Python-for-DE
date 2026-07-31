"""
Topic: Try-Except-Finally
Description: Demonstrates exception handling using Exception as e and finally.
Author: Suryansh
"""

# ============================================
# Try-Except-Finally
# ============================================

y = "10"

try:

    if y > 10:
        print("y is greater than 10")

    else:
        print("y is less than or equal to 10")

except Exception as e:
    print(f"The error is: {e}")

finally:
    print("I will always run")

print("This is the end of the program")