"""
Topic: Multiple Inheritance
Description: Demonstrates inheriting from multiple parent classes.
Author: Suryansh
"""

# ============================================
# Parent Class 1
# ============================================

class Company:

    def __init__(self, comp_name):
        self.comp_name = comp_name

    def company_info(self):
        print(f"Company Name: {self.comp_name}")


# ============================================
# Parent Class 2
# ============================================

class Country:

    def __init__(self, country_name):
        self.country_name = country_name

    def country_info(self):
        print(f"Country: {self.country_name}")


# ============================================
# Child Class
# ============================================

class Employee(Company, Country):

    def __init__(self, emp_name, comp_name, country_name):

        self.emp_name = emp_name

        Company.__init__(self, comp_name)
        Country.__init__(self, country_name)

    def employee_info(self):

        print(
            f"Employee Name : {self.emp_name}\n"
            f"Company      : {self.comp_name}\n"
            f"Country      : {self.country_name}"
        )


# ============================================
# Creating Object
# ============================================

emp1 = Employee("Suryansh", "Apple", "Luxembourg")

emp1.employee_info()
emp1.company_info()
emp1.country_info()