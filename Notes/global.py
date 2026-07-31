x = 100 #global variable

def my_func():
    print(x)
    return x

my_func()

def my_func2():
     x = 50
     print(x) #here the new x value that is 50 will be printed cuz it over write the previous y value that is 10
     return x

my_func2()

z = 20

def my_func3():
      global x
      x = 40
      print(x) #here new x value that is 40 will be printed cuz it overwrites it again
      return x

my_func3()

def my_func4():
     global x
     print(x) #the global x value will be printed here
     return x

my_func4()
