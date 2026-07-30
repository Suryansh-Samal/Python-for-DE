x = 'Suryansh'
print(x[3])  # Accessing the 4th character (index 3) of the string
print(x[0:5])  # Accessing characters from index 0 to 4 (5 is exclusive)
print(x[4:len(x)])  # Accessing characters from index 4 to the end of the string
print(x[4:8])  # Accessing characters from index 4 to 7 (8 is exclusive)
print(x[:])  # Accessing the entire string
print(x.upper())  # Converting the string to uppercase
print(x.lower())  # Converting the string to lowercase
print(x.capitalize())  # Capitalizing the first character of the string
print(x.replace('sh', 'z'))  # Replacing 'Sh' with 'z' in the string
y = 'hello-Suryansh'
my_list= y.split('-')  # Splitting the string into a list using '-' as the delimiter
print(my_list)  # Printing the resulting list after splitting
file= 'raw_data.csv'
if file.endswith('.csv'):  # Checking if the string ends with '.csv'
    print('This is a CSV file')  # Printing a message if the condition is true
if file.startswith('raw'):  # Checking if the string starts with 'raw'
    print('This is a raw data file')  # Printing a message if the condition is true
statement= 'hey Suryansh, how are you Suryansh?, How was your day Suryansh?'
print(statement.count('Suryansh'))  # Counting the occurrences of 'Suryansh' in the string
demo_str= '   1Hello Suryansh, How are you?   '
demo_var = '10'
print(demo_str.isnumeric())  # Checking if the string is numeric
print(demo_str.isalnum())  # Checking if the string is alphanumeric
print(demo_str.isalpha())  # Checking if the string contains only alphabetic characters
print(demo_var.isnumeric())  # Checking if the variable is numeric

z = 300
if z==10:
    print('z is equal to 10')  # Printing a message if z is equal to 10
elif z>100:
    if z>100 and z<200:
        print('z is greater than 100 and less than 200')  # Printing a message if z is greater than 100 and less than 200
    else:
        print('z is greater than 200')  # Printing a message if z is greater than 200
elif z<100:
    print('z is less than 100')  # Printing a message if z is less than 100
else:
    print('z is not equal to 10')  # Printing a message if z is not equal to 10 

my_list2 = [1, 2, 3, 4, 5]
for i in my_list2:
    print(i)  # Printing each element in the list

for i in range(1,11):
    print(i)  # Printing numbers from 1 to 10 (inclusive)