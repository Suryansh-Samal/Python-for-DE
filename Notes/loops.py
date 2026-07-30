tbl_list = ['Order', ' Products', ' Customers', ' Employees', ' Suppliers']
for i in tbl_list:
     if( i.lower()== 'order'):
            print('Table found')  # Printing a message if the table name matches 'order'    
     else:
            print('Table not found')  # Printing a message if the table name does not match 'order'

for i in tbl_list:
      print(i)  # Printing each table name in the list
      for x in i :
            print(x)  # Printing each character in the table name

for i in tbl_list:
      if i.lower() == 'order':
            break
      print(i)  # This line will not execute because of the break statement

for i in tbl_list:
      if i.lower() == 'order':
            continue
      print(i)  # This line will not execute because of the break statement

x = 11
while x <= 20:
      print(x)  # Printing the value of x
      x += 1  # Incrementing x by 1