"""
Topic: Constructors (__init__)
Description: Demonstrates constructors, class variables, instance variables,
and modifying class attributes.
Author: Suryansh
"""

# ============================================
# Class with Constructor
# ============================================

class Employee:

    # Class Variable
    company = "Apple"

    def __init__(self, emp_name, emp_dept):
        """Initializes object attributes."""

        self.emp_name = emp_name
        self.emp_dept = emp_dept

    def change_company(self, new_company):
        """Updates the class variable."""

        Employee.company = new_company

    def info(self):
        """Displays employee details."""

        print(
            f"Employee {self.emp_name} works for the "
            f"{self.emp_dept} department at {self.company}"
        )


# ============================================
# Creating Objects
# ============================================

emp1 = Employee("Suryansh", "Data Engineering")
emp2 = Employee("Piyush", "Development")

# Change company for all objects
emp1.change_company("NVIDIA")

# Create an instance variable for emp2 only
emp2.company = "Palantir"

# Display information
emp1.info()
emp2.info()