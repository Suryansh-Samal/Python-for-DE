x = '10'

try:
    if x>10:
        print('x is greater than 10')
    else:
        print('x is less than or equal to 10')
except:
    print('x is not a number')

print('This is the end of the program')

y = '10'

try:
    if y>10:
        print('y is greater than 10')
    else:
        print('y is less than or equal to 10')
except Exception as e:
    print(f'The error is: {e}')

finally: #This function is always gonna run
    print('I will always run') 
print('This is the end of the program')


def my_func(x):

    try:
        if x%2==0:
            print('Hello World!')
            return 1

    except Exception as e:
        print(f"The error {e} occured")

    finally:
        print('The is the end of the code')

my_func(9)

def my_func2(x):

    return x
    print(X) 
    '''here it will not get printed bcuz it is written after the return statement anything written after
                will not be executed'''

my_func2(2)