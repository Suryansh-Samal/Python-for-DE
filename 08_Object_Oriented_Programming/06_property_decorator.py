"""
Topic: Property Decorator
Description: Demonstrates the use of @property and @property.setter.
Author: Suryansh
"""

# ============================================
# Property Decorator
# ============================================

class Employee:

    # Class Variable
    company = "Apple"

    def __init__(self, emp_name, emp_dept):
        """Initializes employee details."""

        self.emp_name = emp_name
        self.emp_dept = emp_dept

    # Getter Method
    @property
    def info(self):
        """Returns employee information."""

        return (
            f"Employee {self.emp_name} works for the "
            f"{self.emp_dept} department at {self.company}"
        )

    # Setter Method
    @info.setter
    def info(self, emp_details):
        """Updates employee name and department."""

        self.emp_name = emp_details[0]
        self.emp_dept = emp_details[1]


# ============================================
# Creating Objects
# ============================================

emp1 = Employee("Suryansh", "Data Engineering")
emp2 = Employee("Priya", "HR")

# Accessing the property
print(emp1.info)
print(emp2.info)

# Updating values using the setter
emp2.info = ["Priyaa", "HR"]

print("\nAfter Updating:")
print(emp2.info)