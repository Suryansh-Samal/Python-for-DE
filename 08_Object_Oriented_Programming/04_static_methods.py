"""
Topic: Static Methods
Description: Demonstrates the use of @staticmethod.
Author: Suryansh
"""

class Employee:

    @staticmethod
    def addition(x, y):
        """Returns the sum of two numbers."""

        print(x + y)


Employee.addition(2, 3)