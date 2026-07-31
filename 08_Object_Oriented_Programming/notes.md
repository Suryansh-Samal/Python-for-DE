# Classes and Objects

## Topics Covered

- Creating Classes
- Creating Objects
- Class Attributes
- Instance Methods
- The `self` Keyword

## Key Points

- A class is a blueprint for creating objects.
- An object is an instance of a class.
- `self` refers to the current object.
- Use `self.attribute` to access class or instance attributes.
- Method parameters are different from object attributes.

## Example

```python
class Employee:

    name = "Rahul"

    def display(self):
        print(self.name)

emp = Employee()

emp.display()

## Constructors

- Constructors are defined using the `__init__()` method.
- They are called automatically when an object is created.
- Constructors are commonly used to initialize object attributes.

### Example

```python
class Employee:

    def __init__(self, name):
        self.name = name
```

---

## Class Variables

- Shared by all objects of a class.
- Accessed using the class name.

```python
class Employee:

    company = "Apple"
```

---

## Instance Variables

- Unique for each object.
- Created using `self`.

```python
self.emp_name = emp_name
```

---

## Static Methods

- Declared using `@staticmethod`.
- Do not receive `self` or `cls`.
- Used for utility functions that don't access object or class data.

```python
@staticmethod
def add(x, y):
    return x + y
```
```