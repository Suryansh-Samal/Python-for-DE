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

## Class Methods

### Syntax

```python
@classmethod
def method_name(cls):
    pass
```

---

### Example

```python
class Employee:

    company = "Apple"

    @classmethod
    def change_company(cls, company):
        cls.company = company
```

---

## cls

- `cls` refers to the **class itself**.
- It is similar to `self`, but `self` refers to an object, while `cls` refers to the class.

---

## Difference Between self and cls

| self | cls |
|------|-----|
| Refers to the current object | Refers to the class |
| Used in instance methods | Used in class methods |
| Can access instance variables | Can access class variables |

---

## Difference Between Instance, Class and Static Methods

| Method Type | First Parameter | Can Access Instance Variables | Can Access Class Variables |
|-------------|-----------------|-------------------------------|----------------------------|
| Instance Method | `self` | ✅ | ✅ |
| Class Method | `cls` | ❌ | ✅ |
| Static Method | None | ❌ | ❌ |

---

## Key Points

- `@classmethod` is used with the `cls` parameter.
- It is commonly used to modify or access class variables.
- Class methods can be called using either the class name or an object, but calling them with the class name is the recommended approach.

## Property Decorator

### @property

The `@property` decorator allows a method to be accessed like an attribute.

### Syntax

```python
@property
def method(self):
    return value
```

---

### @property.setter

A setter updates the value of an attribute through a property.

### Syntax

```python
@property_name.setter
def property_name(self, value):
    self.attribute = value
```

---

## Example

```python
class Employee:

    def __init__(self, name):
        self.name = name

    @property
    def info(self):
        return self.name

    @info.setter
    def info(self, value):
        self.name = value
```

---

## Key Points

- `@property` creates a getter method.
- `@property.setter` creates a setter method.
- Properties can be accessed like normal attributes.
- No parentheses are used when accessing a property.
- Setters allow controlled updates to object attributes.

# Inheritance

## Topics Covered

- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Parent Class
- Child Class
- `super()`

---

## Single Inheritance

A child class inherits from one parent class.

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

## Multiple Inheritance

A child class inherits from more than one parent class.

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

---

## Multilevel Inheritance

Inheritance occurs through multiple levels.

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

---

## super()

`super()` calls methods or constructors of the parent class.

```python
super().__init__(arguments)
```

---

## Key Points

- Inheritance promotes code reuse.
- Child classes inherit attributes and methods from parent classes.
- `super()` is the preferred way to call the parent constructor.
- Multiple inheritance allows one class to inherit from multiple parents.
- Multilevel inheritance creates a chain of inheritance.