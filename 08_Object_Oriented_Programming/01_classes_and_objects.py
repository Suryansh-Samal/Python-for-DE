"""
Topic: Classes and Objects
Description: Demonstrates creating classes, objects, and accessing class attributes.
Author: Suryansh
"""

# ============================================
# Creating a Class
# ============================================

class Employee:

    emp_name = "Rahul"
    emp_dept = "IT"

    def info(self):
        """Displays employee details."""

        print(f"Employee {self.emp_name} works for department {self.emp_dept}")


# Creating an Object
emp1 = Employee()

# Accessing Class Attributes
print(emp1.emp_name)
print(emp1.emp_dept)

# Calling a Method
emp1.info()