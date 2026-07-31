my_list = [1,2,3,4,5]

def square(x):
    return x* x  # Returning the square of the input value

result = list(map(square, my_list))  # Using the map function to apply the square function to each element in my_list
print(result)  # Printing the list of squared values

result1 = square(9) 
print(result1)  # Printing the square of 9

result3 = tuple(map(square, my_list))  # Using the map function to apply the square function to each element in my_list
print(result3)  # Printing the tuple of squared values