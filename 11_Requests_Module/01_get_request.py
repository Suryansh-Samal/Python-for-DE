"""
Topic: GET Request
Description: Demonstrates sending an HTTP GET request using the requests module.
Author: Suryansh
"""

import requests

# ============================================
# Sending a GET Request
# ============================================

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

# ============================================
# Status Code
# ============================================

print("Status Code:", response.status_code)

# ============================================
# JSON Response
# ============================================

data = response.json()

print(data)