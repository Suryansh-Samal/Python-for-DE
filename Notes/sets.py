a = {1,2,3,3,4,4,4,4}
b = {1,2,3,4,5,6,7}
print(a.union(b))  # Printing the union of sets a and b, which combines all unique elements from both sets
print(a.intersection(b))  # Printing the intersection of sets a and b, which shows the common elements between both sets
print(a)  # Printing the set, which will automatically remove duplicate values
a.remove(4)  # Removing the element 4 from set a
print(a)  # Printing the updated set a after removing the element 4
a.add(10)  # Adding the element 10 to set a
print(a)  # Printing the updated set a after adding the element 10  
c = set() #empty set
