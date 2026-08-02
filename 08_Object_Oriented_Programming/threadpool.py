# import time
# import random 
# from concurrent.futures import ThreadPoolExecutor

# my_table = ['orders', 'customers', 'products', 'employees', 'suppliers']

# def my_func(i):
#     wait = random.randint(1,10)
#     time.sleep(wait)
#     print(f"I am {i}. I took {wait} seconds")

# with ThreadPoolExecutor  (max_workers=len(my_table)) as executor:
#     futures= executor.map(my_func,my_table)

#Another way to do it

import time
import random 
from concurrent.futures import ThreadPoolExecutor

my_table = ['orders', 'customers', 'products', 'employees', 'suppliers']

def my_func(i):
    wait = random.randint(1,10)
    time.sleep(wait)
    print(f"I am {i}. I took {wait} seconds")

with ThreadPoolExecutor (max_workers=len(my_table)) as executor:
    for i in my_table:
        futures= executor.submit(my_func,i)
