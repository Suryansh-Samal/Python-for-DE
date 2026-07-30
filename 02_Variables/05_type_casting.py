# ============================================
# Type Casting in Python
# ============================================

# --------------------------------------------
# Implicit Type Casting
# Python automatically converts one data type
# to another when it is safe to do so.
# --------------------------------------------

x = 10          # Integer
y = 5.5         # Float

result = x + y  # int + float = float

print(result)
print(type(result))


# --------------------------------------------
# Explicit Type Casting
# The programmer manually converts a data type.
# --------------------------------------------

# String to Integer
age = "20"

print(age)
print(type(age))

age = int(age)

print(age)
print(type(age))


# --------------------------------------------
# String to Float
# --------------------------------------------

price = "99.99"

price = float(price)

print(price)
print(type(price))


# --------------------------------------------
# Integer to String
# --------------------------------------------

number = 25

number = str(number)

print(number)
print(type(number))


# --------------------------------------------
# Integer to Boolean
# --------------------------------------------

print(bool(1))      # True
print(bool(0))      # False


# --------------------------------------------
# String to Boolean
# --------------------------------------------

print(bool(""))         # False (Empty string)
print(bool("Python"))   # True (Non-empty string)


# --------------------------------------------
# Float to Integer
# int() removes the decimal part (does not round)
# --------------------------------------------

value = 15.89

value = int(value)

print(value)
print(type(value))


# --------------------------------------------
# Integer to Float
# --------------------------------------------

marks = 95

marks = float(marks)

print(marks)
print(type(marks))