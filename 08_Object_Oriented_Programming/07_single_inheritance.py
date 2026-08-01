"""
Topic: Single Inheritance
Description: Demonstrates inheritance between a parent class and a child class.
Author: Suryansh
"""

# ============================================
# Parent Class
# ============================================

class Company:

    def __init__(self, comp_name):
        self.comp_name = comp_name

    def company_info(self):
        """Displays company information."""

        print(f"Company Name: {self.comp_name}")


# ============================================
# Child Class
# ============================================

class Employee(Company):

    def __init__(self, emp_name, comp_name):
        self.emp_name = emp_name

        super().__init__(comp_name)

    def employee_info(self):
        """Displays employee information."""

        print(
            f"Employee Name: {self.emp_name}\n"
            f"Company Name : {self.comp_name}"
        )


# ============================================
# Creating Object
# ============================================

emp1 = Employee("Suryansh", "Apple")

emp1.employee_info()
emp1.company_info()