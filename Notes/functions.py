
x = 10
def my_func ():
        print(x)  # Printing the value of x
        return x + 5  # Returning the value of x incremented by 5

value=my_func()  # Calling the function my_func
print(value)  # Printing the returned value from the function

def my_func2 (x,y):
        print(x,y)  # Printing the values of x and y
        return x + y  # Returning the sum of x and y

my_func2(10,20)  # Calling the function my_func2 with arguments 10 and 20

def my_func3 (x,y=10):
        print(x+y)  # Printing the sum of x and y
        return x + y  # Returning the sum of x and y
my_func3(10)  # Calling the function my_func3 with only one argument, y will take the default value of 10

def my_func4 (x,y=10):
        print(x+y)  # Printing the sum of x and y
        return x + y  # Returning the sum of x and y
my_func4(10,20)  # Calling the function my_func4 with both arguments, x=10 and y=20

def my_func5(*x):
        print(x)  # Printing the tuple of arguments passed to the function
        return sum(x)  # Returning the sum of all arguments passed to the function
my_func5(10,20,30,40) # Calling the function my_func5 with four arguments

def my_func6(**x):
        print(x) # Printing the dictionary of keyword arguments passed to the function
        print(x.keys()) #Printing the keys of the dictionary
        return x
my_func6(a=10,b=20,c=30,d=40)  # Calling the function my_func6 with four keyword arguments