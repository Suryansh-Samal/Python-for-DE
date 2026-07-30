my_list = [1,2,'Suryansh',['aa','bb','cc']]
phone = '+91 9910731185'
print(my_list[3][1])  # Accessing the second element of the nested list (index 1)
print(my_list[3][0:2])  # Accessing the first two elements of the nested list (index 0 and 1)
print(my_list[-3:])  # Accessing the last three elements of the main list (index -3 to the end)
print(my_list[3]) # Accessing the entire nested list (index 3)
print(my_list[2])  # Accessing the third element of the main list (index 2)
print(phone[-10:]) # Accessing the last 10 characters of the phone string (the actual phone number)
print(phone[::-2]) # Accessing every second character of the phone string (from start to end) in reverse order
print(phone[::2]) # Accessing every second character of the phone string (from start to end) in normal order
my_list.append('Python')  # Adding 'Python' to the end of the main list
print(my_list)  # Printing the updated main list after appending 'Python'
my_list.insert(1,'Java')  # Inserting 'Java' at index 1 of the main list
print(my_list)  # Printing the updated main list after inserting 'Java'
my_list.pop()  # Removing the last element from the main list
print(my_list)  # Printing the updated main list after popping the last element 
my_list.remove('Java')  # Removing 'Java' from the main list
print(my_list)  # Printing the updated main list after removing 'Java'

for i in reversed(my_list):
    print(i)  # Printing each element of the main list in reverse order

my_list.reverse()  # Reversing the order of elements in the main list
print(my_list)  # Printing the main list after reversing its order

my_list2 = [1, 2, 3, 4, 5,6]
new_list = [i*1 for i in my_list2 if (i%2==0) and (i!= 6)]  # Creating a new list with elements from my_list2 that are even, multiplied by 1
print(new_list)  # Printing the new list containing even elements from my_list2