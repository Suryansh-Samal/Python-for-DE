"""
Topic: Lambda Functions
Description: Demonstrates creating and using anonymous (lambda) functions.
Author: Suryansh
"""

# ============================================
# Lambda Function
# ============================================

# Lambda function to add two numbers
addition = lambda x, y: x + y

# Calling the lambda function
result = addition(10, 20)

print("The addition of the passed values is:", result)