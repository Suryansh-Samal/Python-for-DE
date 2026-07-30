"""
Topic: Nested Loops
Description: Iterating through strings inside a list.
Author: Suryansh
"""

tbl_list = ["Order", "Products", "Customers", "Employees", "Suppliers"]

for table in tbl_list:

    print(table)

    for character in table:
        print(character)