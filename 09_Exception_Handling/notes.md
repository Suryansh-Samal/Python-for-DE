# Exception Handling

## Topics Covered

- try
- except
- Exception as e
- finally
- Exception Handling in Functions
- return Statement

---

## Syntax

```python
try:
    # Code that may raise an exception

except Exception as e:
    # Handle the exception

finally:
    # Executes regardless of whether an exception occurs
```

---

## Key Points

- `try` contains code that may raise an exception.
- `except` handles the exception.
- `Exception as e` stores the error message.
- `finally` always executes.
- Code written after a `return` statement is never executed.

## raise

### Syntax

```python
raise ExceptionType("Error Message")
```

### Example

```python
age = 15

if age < 18:
    raise ValueError("Age must be at least 18.")
```

## Key Points

- The `raise` keyword is used to generate an exception manually.
- It is commonly used for input validation.
- You can raise built-in exceptions such as:
  - `ValueError`
  - `TypeError`
  - `KeyError`
  - `IndexError`
- You can also create and raise custom exceptions.