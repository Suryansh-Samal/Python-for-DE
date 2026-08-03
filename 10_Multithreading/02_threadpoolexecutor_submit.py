"""
Topic: ThreadPoolExecutor using submit()
Description: Demonstrates concurrent execution of tasks using ThreadPoolExecutor and submit().
Author: Suryansh
"""

import random
import time
from concurrent.futures import ThreadPoolExecutor

# ============================================
# Sample Data
# ============================================

tables = [
    "orders",
    "customers",
    "products",
    "employees",
    "suppliers"
]


# ============================================
# Task Function
# ============================================

def process_table(table):
    """
    Simulates processing a database table.
    """

    wait_time = random.randint(1, 10)

    time.sleep(wait_time)

    print(f"Processing {table} completed in {wait_time} seconds.")


# ============================================
# Executing Threads using submit()
# ============================================

with ThreadPoolExecutor(max_workers=len(tables)) as executor:


    for table in tables:

        future = executor.submit(process_table, table)
