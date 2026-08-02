# Multithreading

## Topics Covered

- ThreadPoolExecutor
- map()
- submit()
- max_workers

---

## ThreadPoolExecutor

`ThreadPoolExecutor` creates and manages a pool of worker threads.

```python
from concurrent.futures import ThreadPoolExecutor
```

---

## map()

Executes the same function on multiple inputs concurrently.

```python
with ThreadPoolExecutor() as executor:

    executor.map(function, iterable)
```

### Example

```python
executor.map(process_table, tables)
```

---

## submit()

Submits one task at a time and returns a `Future` object.

```python
future = executor.submit(function, argument)
```

Example

```python
future = executor.submit(process_table, "orders")
```

---

## Future Object

A `Future` represents a task running in the background.

```python
future.result()
```

Calling `result()` waits until the task finishes.

---

## Difference Between map() and submit()

| map() | submit() |
|--------|----------|
| Processes an iterable automatically | Submits one task at a time |
| Simpler for the same function on many inputs | More control over each task |
| Returns results in input order | Returns a `Future` object |

---

## Key Points

- Multithreading allows multiple tasks to run concurrently.
- `ThreadPoolExecutor` manages worker threads.
- `max_workers` specifies the maximum number of threads.
- `map()` is ideal when applying one function to many items.
- `submit()` is useful when you need to manage individual tasks or `Future` objects.