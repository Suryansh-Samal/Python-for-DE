# my_list = [1, 2, "Suryansh", ["aa", "bb", "cc"]]

# # String for slicing examples
# phone = "+91 9910731185"

# # Accessing elements from a nested list
# print(my_list[3][1])
# print(my_list[3][0:2])

# # Negative indexing and slicing
# print(my_list[-3:])

# # Accessing list elements
# print(my_list[3])
# print(my_list[2])

# # String slicing
# print(phone[-10:])
# print(phone[::-2])
# print(phone[::2])


# """
# Topic: filter() Function
# Description: Demonstrates how to use the built-in filter() function
# to filter elements from an iterable.
# Author: Suryansh
# """

# # ============================================
# # Sample List
# # ============================================

# my_list = [1, 2, 3, 4, 5, 6]


# # ============================================
# # Function to Filter Even Numbers
# # ============================================

# def is_even(number):
#     """
#     Returns True for even numbers.
#     """

#     if number % 2 == 0:
#         return True

#     return False


# # ============================================
# # Using filter()
# # ============================================

# result = list(filter(is_even, my_list))

# print(result)

# """
# Topic: map() Function
# Description: Demonstrates how to use the built-in map() function
# to transform elements of an iterable.
# Author: Suryansh
# """

# # ============================================
# # Sample List
# # ============================================

# my_list = [1, 2, 3, 4, 5]


# # ============================================
# # Function to Square Numbers
# # ============================================

# def square(number):
#     """
#     Returns the square of a number.
#     """

#     return number * number


# # ============================================
# # Using map() with a List
# # ============================================

# result = list(map(square, my_list))

# print("Squared List:")
# print(result)


# # ============================================
# # Calling the Function Directly
# # ============================================

# result = square(9)

# print("\nSquare of 9:")
# print(result)


# # ============================================
# # Using map() with a Tuple
# # ============================================

# result = tuple(map(square, my_list))

# print("\nSquared Tuple:")
# print(result)

class Employee:

    # Class Variable
    company = "Apple"

    def __init__(self, emp_name, emp_dept):
        """Initializes object attributes."""

        self.emp_name = emp_name
        self.emp_dept = emp_dept

    def change_company(self, new_company):
        """Updates the class variable."""

        Employee.company = new_company

    def info(self):
        """Displays employee details."""

        print(
            f"Employee {self.emp_name} works for the "
            f"{self.emp_dept} department at {self.company}"
        )


# ============================================
# Creating Objects
# ============================================

emp1 = Employee("Suryansh", "Data Engineering")
emp2 = Employee("Piyush", "Development")

# Change company for all objects
emp1.change_company("NVIDIA")


# Display information
emp1.info()
emp2.info()