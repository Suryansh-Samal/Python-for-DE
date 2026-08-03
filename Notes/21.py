class employee ():
    company= 'Apple'

    def __init__(self,emp_name,emp_dept):
        self.emp_name = emp_name
        self.emp_dept = emp_dept

    @classmethod
    def changes(cls,new_company):
        cls.company = new_company

    @staticmethod
    def addition(x,y):
        print(x + y)

    def info(self):
        print(f'Employee {self.emp_name} works in department {self.emp_dept} at {self.company}')

emp1= employee('Suryansh', 'Data Engineering')
emp1.info()
emp1.addition(4,6)
emp1.changes('Microsoft')
emp1.info()