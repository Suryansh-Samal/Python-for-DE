# Loops

## Topics Covered

- for Loop
- while Loop
- range()
- enumerate()
- Nested Loops
- break
- continue

---

## for Loop

```python
numbers = [1,2,3]

for number in numbers:
    print(number)
```

---

## range()

```python
for i in range(1,6):
    print(i)
```

---

## enumerate()

```python
numbers = [100,200,300]

for index, value in enumerate(numbers):
    print(index, value)
```

Returns

```text
0 100
1 200
2 300
```

---

## Nested Loops

```python
names = ["Python","SQL"]

for word in names:

    for letter in word:

        print(letter)
```

---

## break

Stops the loop immediately.

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

Output

```text
0
1
2
3
4
```

---

## continue

Skips the current iteration.

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

Output

```text
0
1
3
4
```

---

## while Loop

```python
x = 1

while x <= 5:

    print(x)

    x += 1
```

---

## Key Points

- `for` loops iterate over sequences.
- `while` loops run until a condition becomes False.
- `range()` generates a sequence of numbers.
- `enumerate()` provides both index and value.
- `break` exits the loop.
- `continue` skips the current iteration.
- Nested loops execute one loop inside another.