from functools import reduce
my_list=[1,2,3,4,5,6]
def square(x,y):
    return x * y  # Returning the product of x and y

result = reduce(square, my_list)  # Using the reduce function to apply the square function cumulatively to the items of my_list
print(result)  # Printing the final result after reducing the list