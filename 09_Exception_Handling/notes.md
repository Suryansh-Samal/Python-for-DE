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