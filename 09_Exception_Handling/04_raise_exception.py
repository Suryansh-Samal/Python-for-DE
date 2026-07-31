"""
Topic: raise Statement
Description: Demonstrates raising custom exceptions using the raise keyword.
Author: Suryansh
"""

# ============================================
# Raising an Exception
# ============================================

x = 9

if x < 10:
    raise ValueError("Value less than 10 is not allowed")