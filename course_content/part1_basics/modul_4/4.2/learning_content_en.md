# 🗂️ Tuples

## What are Tuples?

Tuples are immutable sequences - once created, they cannot be changed.

```python
coordinates = (10, 20)
person = ("Alice", 30, "Berlin")
```

## Tuples vs. Lists

| Property | Tuples | Lists |
|----------|--------|-------|
| Mutability | Immutable | Mutable |
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Performance | Faster | Slower |
| Usage | Fixed data | Variable data |

## Tuple Operations

### Access

```python
point = (5, 10)
x = point[0]  # 5
y = point[1]  # 10
```

### Unpacking

```python
coordinates = (10, 20)
x, y = coordinates

# Extended Unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
```

## Named Tuples

Tuples with named fields for better readability:

```python
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'profession'])
alice = Person("Alice", 30, "Developer")
print(alice.name)  # Alice
```

## Use Cases

- Coordinates (x, y)
- RGB colors (r, g, b)
- Database records
- Function return values
- Dictionary keys