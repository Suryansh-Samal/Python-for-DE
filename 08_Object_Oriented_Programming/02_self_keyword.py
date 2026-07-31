"""
Topic: self Keyword
Description: Demonstrates how self refers to the current object and how method parameters work.
Author: Suryansh
"""

# ============================================
# Example 1
# ============================================

class Employee:

    emp_name = "Suryansh"
    emp_dept = "Data Engineering"

    def information(self, emp_name, emp_dept):
        """
        Uses the parameters passed to the method,
        not the class attributes.
        """

        print(f"Employee {emp_name} works for department {emp_dept}")


emp = Employee()

# Uses the method parameters
emp.information("Raj", "HR")


# ============================================
# Example 2
# ============================================

class EmployeeDetails:

    emp_name = "Ayush"
    emp_dept = "Business"

    def info(self):
        """
        Uses self to access the object's attributes.
        """

        print(f"Employee {self.emp_name} works for department {self.emp_dept}")


emp2 = EmployeeDetails()

emp2.info()