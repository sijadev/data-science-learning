# 📋 Lists

## What are Lists?

Lists are mutable sequences that can store different data types.

```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Text", 3.14, True]
```

## List Operations

### Accessing Elements

- Index access: `list[0]`
- Negative index: `list[-1]` (last element)
- Slicing: `list[1:4]`

### Adding Elements

- `append()` - Adds element at the end
- `extend()` - Adds multiple elements
- `insert()` - Inserts element at specific position

### Removing Elements

- `remove()` - Removes first occurrence
- `pop()` - Removes and returns element
- `del` - Deletes element at index

## Useful Methods

- `len()` - Length of the list
- `sort()` - Sorts the list
- `reverse()` - Reverses the order
- `count()` - Counts occurrences of element
- `index()` - Finds index of element

## List Comprehensions

Elegant method for creating lists:

```python
squares = [x**2 for x in range(10)]
even_numbers = [x for x in range(20) if x % 2 == 0]
```