my_dictionary = {'name':'Suryansh', 'age': 20, 'city': 'Delhi', 'demo' : {'a': 1, 'b': 2}}  # Creating a dictionary with keys and values, including a nested dictionary   
my_dictionary['age'] = 21  # Updating the value associated with the key 'age'
empty_dictionary = {}  # Creating an empty dictionary
print(my_dictionary)
print(my_dictionary['demo']['a'])  # Accessing the value associated with the key 'a' in the nested dictionary
print(my_dictionary['demo'].items())  # Accessing the items of the nested dictionary
print(my_dictionary['name'])  # Accessing the value associated with the key 'name'
my_dictionary.pop ('city')  # Removing the key-value pair with the key 'city'
print(my_dictionary)  # Printing the updated dictionary after removing the key 'city'
print(my_dictionary.keys())  # Printing all the keys in the dictionary
print(my_dictionary.values())  # Printing all the values in the dictionary
print(my_dictionary.items())  # Printing all the key-value pairs in the dictionary