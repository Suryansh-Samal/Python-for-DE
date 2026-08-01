class employee():
    company = 'Apple'

    def __init__(self,emp_name,emp_dept):
        self.emp_name = emp_name
        self.emp_dept = emp_dept

    @property
    def info(self):
        print(f'Employee {self.emp_name} works for department {self.emp_dept} at {self.company}')

    @info.setter
    def info(self,emp_details):
        self.emp_name = emp_details[0]
        self.emp_dept = emp_details[1]
emp1 = employee('Suryansh', 'Data')
emp2 = employee('Priya', 'HR')
emp1.info
emp2.info
emp2.info = ['Priyaa', 'HR']
print(emp2.info)