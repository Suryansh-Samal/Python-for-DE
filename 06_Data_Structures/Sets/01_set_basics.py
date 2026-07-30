"""
Topic: Set Basics
Description: Demonstrates set creation, duplicate removal, and common set methods.
Author: Suryansh
"""

# ============================================
# Creating Sets
# ============================================

# Duplicate values are automatically removed
a = {1, 2, 3, 3, 4, 4, 4, 4}

b = {1, 2, 3, 4, 5, 6, 7}

# Empty Set
c = set()

print(a)
print(b)
print(c)


# ============================================
# Set Operations
# ============================================

# Union
print("Union:")
print(a.union(b))

# Intersection
print("\nIntersection:")
print(a.intersection(b))


# ============================================
# Set Methods
# ============================================

# Remove an element
a.remove(4)

print("\nAfter remove():")
print(a)

# Add an element
a.add(10)

print("\nAfter add():")
print(a)