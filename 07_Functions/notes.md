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