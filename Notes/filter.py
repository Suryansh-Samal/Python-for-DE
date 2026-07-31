my_list=[1,2,3,4,5,6] 

def square(x):
    if x%2==0:
        return x * x  # Returning the square of the input value

result = list(filter(square, my_list)) # Using the filter function to apply the square function to each element in my_list
print(result)  # Printing the list of squared values