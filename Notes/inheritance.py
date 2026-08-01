# Single Level Inheritance

class company():
    def __init__(self,comp_name):
        self.comp_name = comp_name

    def comp_info(self):
        print(f"Company name is {self.comp_name}")

class employee (company):
    def __init__(self, emp_name,comp_name):
        self.emp_name = emp_name

        company.__init__(self,comp_name)
    def info(self):
        print(f"Employee name is {self.emp_name} and company name is {self.comp_name}")

    def comp_info_employee(self):
        company.comp_info(self)

emp1 = employee('Suryansh', 'Apple')
emp1.info()
emp1.comp_info_employee()

#Multiple Inheritance

class Company():

    def __init__(self, comp_name):
        self.comp_name = comp_name

    def company_info(self):
        print(f'Company name is {self.comp_name}')

class Country():

    def __init__(self,country_name):
        self.country_name = country_name

    def country_info(self):
        print(f"Country is {self.country_name}")

class employee (Company,Country):

    def __init__(self, emp_name, comp_name, country_name):
        self.emp_name = emp_name
        Company.__init__(self,comp_name)
        Country.__init__(self,country_name)

    def full_info (self):
        print(f"Employee {self.emp_name} lives in country {self.country_name} and works at {self.comp_name}")

    def employee_country_info(self):
        Company.company_info(self)

    def employee_country_info(self):
        Country.country_info(self)

emp1 = employee("Suryansh", "Apple", "Luxembourg")
emp1.full_info()
emp1.company_info()
emp1.country_info()

# Multilevel Inheritance
class Company():
    def __init__(self,comp_name):
            self.comp_name = comp_name

    def company_info(self):
            print(f"Company name is {self.comp_name}")

class department(Company):
    def __init__(self,dept_name,comp_name):
        self.dept_name = dept_name
        Company.__init__(self,comp_name)

    def department_info(self):
        print(f"Department name is {self.dept_name} and company name is {self.comp_name}")

class employee(department):
    def __init__(self,emp_name,dept_name,comp_name):
        self.emp_name = emp_name
        department.__init__(self,dept_name,comp_name)

    def employee_info(self):
        print(f"Employee name is {self.emp_name} and department name is {self.dept_name} and company name is {self.comp_name}")

emp1 = employee("Suryansh", "Data Engineering", "Apple")
emp1.employee_info()
emp1.department_info()
emp1.company_info()