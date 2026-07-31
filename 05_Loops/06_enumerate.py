"""
Topic: enumerate() Function
Description: Demonstrates how to iterate over a list with both index and value.
Author: Suryansh
"""

# ============================================
# Sample List
# ============================================

my_list = [100, 200, 300, 400, 500]


# ============================================
# enumerate() Returns Tuples
# ============================================

print("Enumerate Output:")

for item in enumerate(my_list):
    print(item)


# ============================================
# Unpacking Index and Value
# ============================================

print("\nIndex and Value:")

for index, value in enumerate(my_list):
    print(f"Index : {index}")
    print(f"Value : {value}")