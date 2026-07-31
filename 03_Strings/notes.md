# Strings

## Topics Covered

- String Indexing
- String Slicing
- String Methods
- String Validation Methods
- f-Strings

---

## String Indexing

Access a character using its index.

```python
name = "Python"

print(name[0])      # P
print(name[-1])     # n
```

---

## String Slicing

Extract a portion of a string.

```python
name = "Python"

print(name[0:4])
print(name[:4])
print(name[2:])
print(name[:])
print(name[::-1])
```

---

## Common String Methods

| Method | Description |
|---------|-------------|
| upper() | Converts to uppercase |
| lower() | Converts to lowercase |
| capitalize() | Capitalizes first letter |
| replace() | Replaces text |
| split() | Splits a string |
| count() | Counts occurrences |
| startswith() | Checks starting characters |
| endswith() | Checks ending characters |

Example:

```python
text = "Hello Python"

print(text.upper())
print(text.lower())
print(text.replace("Python", "World"))
```

---

## String Validation Methods

| Method | Description |
|---------|-------------|
| isnumeric() | Checks if string contains only numbers |
| isalpha() | Checks if string contains only alphabets |
| isalnum() | Checks if string contains only letters and numbers |

Example

```python
print("123".isnumeric())

print("Python".isalpha())

print("Python123".isalnum())
```

---

## f-Strings

Used for string formatting.

```python
name = "Suryansh"

print(f"Hello {name}")
```

Multiple variables

```python
name = "Suryansh"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

Expressions

```python
x = 10
y = 20

print(f"Sum = {x + y}")
```

---

## Key Points

- Strings are immutable.
- Indexing starts from 0.
- Negative indexing starts from -1.
- Slicing does not modify the original string.
- f-strings are the recommended way for string formatting.