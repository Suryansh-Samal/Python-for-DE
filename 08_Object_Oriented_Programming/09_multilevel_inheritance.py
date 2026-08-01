"""
Topic: Multilevel Inheritance
Description: Demonstrates multilevel inheritance in Python.
Author: Suryansh
"""

# ============================================
# Parent Class
# ============================================

class Company:

    def __init__(self, comp_name):
        self.comp_name = comp_name

    def company_info(self):
        print(f"Company Name: {self.comp_name}")


# ============================================
# Intermediate Class
# ============================================

class Department(Company):

    def __init__(self, dept_name, comp_name):

        self.dept_name = dept_name

        super().__init__(comp_name)

    def department_info(self):

        print(
            f"Department : {self.dept_name}\n"
            f"Company    : {self.comp_name}"
        )


# ============================================
# Child Class
# ============================================

class Employee(Department):

    def __init__(self, emp_name, dept_name, comp_name):

        self.emp_name = emp_name

        super().__init__(dept_name, comp_name)

    def employee_info(self):

        print(
            f"Employee   : {self.emp_name}\n"
            f"Department : {self.dept_name}\n"
            f"Company    : {self.comp_name}"
        )


# ============================================
# Creating Object
# ============================================

emp1 = Employee(
    "Suryansh",
    "Data Engineering",
    "Apple"
)

emp1.employee_info()
emp1.department_info()
emp1.company_info()