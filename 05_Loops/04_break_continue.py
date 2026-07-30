"""
Topic: Break & Continue
Description: Demonstrates break and continue statements.
Author: Suryansh
"""

tbl_list = ["Order", "Products", "Customers"]

print("Break Example")

for table in tbl_list:

    if table.lower() == "order":
        break

    print(table)

print()

print("Continue Example")

for table in tbl_list:

    if table.lower() == "order":
        continue

    print(table)