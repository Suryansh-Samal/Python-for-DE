# Conditionals

## Topics Covered

- if
- elif
- else
- Nested if
- Comparison Operators
- Logical Operators

---

## if Statement

```python
age = 18

if age >= 18:
    print("Eligible")
```

---

## if...else

```python
age = 15

if age >= 18:
    print("Eligible")

else:
    print("Not Eligible")
```

---

## if...elif...else

```python
marks = 85

if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

else:
    print("C")
```

---

## Nested if

```python
age = 20

if age >= 18:

    if age < 60:
        print("Adult")

    else:
        print("Senior Citizen")
```

---

## Comparison Operators

| Operator | Meaning |
|-----------|---------|
| == | Equal |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

---

## Logical Operators

| Operator | Meaning |
|-----------|---------|
| and | Both conditions must be True |
| or | At least one condition must be True |
| not | Reverses the condition |

Example

```python
age = 20

if age >= 18 and age <= 60:
    print("Working Age")
```

---

## Key Points

- Python uses indentation instead of braces.
- Every condition ends with a colon (`:`).
- Use `elif` for multiple conditions.
- Nested `if` means placing one `if` inside another.