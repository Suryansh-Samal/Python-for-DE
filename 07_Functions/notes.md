# Functions

## Topics Covered

- Function Definition
- Function Calls
- return Statement
- Function Parameters
- Positional Arguments
- Default Arguments
- *args
- **kwargs

## Key Points

- Functions are defined using the `def` keyword.
- `return` sends a value back to the caller.
- Parameters receive values passed to the function.
- Default arguments are used when no value is provided.
- `*args` accepts a variable number of positional arguments as a tuple.
- `**kwargs` accepts a variable number of keyword arguments as a dictionary.

## Example Syntax

### Basic Function

```python
def greet():
    print("Hello")
```

### Function with Parameters

```python
def add(a, b):
    return a + b
```

### Default Arguments

```python
def add(a, b=10):
    return a + b
```

### *args

```python
def total(*numbers):
    return sum(numbers)
```

### **kwargs

```python
def details(**data):
    print(data)
```

## filter()

### Syntax

```python
filter(function, iterable)
```

### Example

```python
numbers = [1, 2, 3, 4, 5]

def is_even(number):
    return number % 2 == 0

result = list(filter(is_even, numbers))

print(result)
```

### Output

```text
[2, 4]
```

### Key Points

- `filter()` returns only the elements that satisfy a condition.
- The function passed to `filter()` must return `True` or `False`.
- `filter()` returns a filter object, so it is commonly converted to a list using `list()`.

## Variable Scope

### Types of Variables

- Global Variables
- Local Variables

---

### Global Variable

A global variable is declared outside a function and can be accessed from anywhere in the program.

```python
x = 100
```

---

### Local Variable

A local variable is declared inside a function and can only be accessed within that function.

```python
def demo():
    x = 50
```

---

### global Keyword

The `global` keyword allows a function to modify a global variable.

```python
x = 100

def change():
    global x
    x = 50
```

---

## Key Points

- Global variables are accessible throughout the program.
- Local variables exist only inside the function where they are defined.
- A local variable with the same name as a global variable **shadows** the global variable inside that function.
- Use the `global` keyword only when you need to modify a global variable.

## Lambda Functions

### Syntax

```python
lambda arguments: expression
```

### Example

```python
addition = lambda x, y: x + y

print(addition(10, 20))
```

### Output

```text
30
```

## Key Points

- Lambda functions are anonymous functions.
- They are defined using the `lambda` keyword.
- A lambda function can have multiple arguments but only one expression.
- They are commonly used with functions like `map()`, `filter()`, and `sorted()`.

## map()

### Syntax

```python
map(function, iterable)
```

### Example

```python
numbers = [1, 2, 3, 4]

def square(x):
    return x * x

result = list(map(square, numbers))

print(result)
```

### Output

```text
[1, 4, 9, 16]
```

## Key Points

- `map()` applies a function to every element of an iterable.
- It returns a `map` object.
- Convert the result using `list()`, `tuple()`, or another iterable type if needed.
- Commonly used with:
  - User-defined functions
  - Lambda functions

  ## reduce()

### Syntax

```python
reduce(function, iterable)
```

### Example

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)
```

### Output

```text
10
```

## Key Points

- `reduce()` is available in the `functools` module.
- It combines all elements of an iterable into a single value.
- The function supplied to `reduce()` must accept **two arguments**.
- Common operations include:
  - Sum
  - Product
  - Maximum
  - Minimum