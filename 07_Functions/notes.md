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