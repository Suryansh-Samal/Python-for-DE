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
```