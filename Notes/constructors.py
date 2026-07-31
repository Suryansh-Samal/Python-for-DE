class employee ():
    company = "Apple"

    def __init__(self,emp_name,emp_dept):
        self.emp_name = emp_name
        self.emp_dept = emp_dept

    def changes(self,new_company): #passing self cuz python gonna take object too 
        employee.company = new_company
    
    def info(self):
        print(f'Employee {self.emp_name} works for department {self.emp_dept} at {self.company}')

    @staticmethod
    def addition(x,y):
        print(x+y)
emp1 = employee('Suryansh' , 'Data Engineering')
emp2 = employee('Piyush' , 'Development')
emp1.changes('Nvidia')
emp2.company = 'Palantir'
emp1.info()
emp2.info()
emp1.addition(2,3)
