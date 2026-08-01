"""
Topic: Class Methods
Description: Demonstrates the use of @classmethod to modify class variables.
Author: Suryansh
"""

# ============================================
# Class Methods
# ============================================

class Employee:

    # Class Variable
    company = "Apple"

    def __init__(self, emp_name, emp_dept):
        """Initializes employee details."""

        self.emp_name = emp_name
        self.emp_dept = emp_dept

    @classmethod
    def change_company(cls, new_company):
        """
        Modifies the class variable for all objects.
        """

        cls.company = new_company

    @staticmethod
    def addition(x, y):
        """Returns the sum of two numbers."""

        print(x + y)

    def info(self):
        """Displays employee details."""

        print(
            f"Employee {self.emp_name} works in the "
            f"{self.emp_dept} department at {self.company}"
        )


# ============================================
# Creating Objects
# ============================================

emp1 = Employee("Suryansh", "Data Engineering")
emp2 = Employee("Piyush", "Development")

# Display initial company
emp1.info()
emp2.info()

# Change class variable
Employee.change_company("NVIDIA")

print()

# Display updated company
emp1.info()
emp2.info()

print()

# Static Method
Employee.addition(4, 6)