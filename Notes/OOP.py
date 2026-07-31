class employee ():

    emp_name = 'Rahul'
    emp_dept = 'IT'

    def info(self,emp_name,emp_dept):
        print(f'Employee {self.emp_name} works for department {self.emp_dept}')

emp1 = employee()
print(emp1.emp_name)
print(emp1.emp_dept)
emp1.info('Raj','Business')

# class employee2 ():

#     emp_name = "Suryansh"
#     emp_dept = 'Data Engineering'

#     def information (self,emp_name,emp_dept):
#         print(f"Employee {emp_name} works for department {emp_dept}") 
#         '''if we will use self here so it will take internal variables that is emp_name = Suryansh and emp_dept = Data Engineering'''

# emp2 = employee2()
# emp2.information('Raj','HR')
# '''passing parameter is compulsory here cuz in function it is asked to pass the parameter no matter if the function use it or not'''

# class employee3():
#     emp_name = 'Ayush'
#     emp_dept = 'Business'

#     def info2(self):
#         print(f"Employee {self.emp_name} works for department {self.emp_dept}")

# emp3 = employee3
# employee3.info2(emp3) #passing the object that we created in the class 