# 🎯 Sets

## What are Sets?

Sets are unordered collections of unique elements - no duplicates allowed.

```python
numbers = {1, 2, 3, 4, 5}
mixed = {1, "Text", 3.14}
```

## Set Properties

- **Unique:** Each element only once
- **Unordered:** No fixed sequence
- **Mutable:** Elements can be added/removed
- **Hashable:** Only immutable elements allowed

## Duplicate Removal

```python
list_with_duplicates = [1, 2, 2, 3, 3, 4]
unique_values = set(list_with_duplicates)
# {1, 2, 3, 4}
```

## Set Operations

### Mathematical Operations

- **Union:** `set_a | set_b`
- **Intersection:** `set_a & set_b`
- **Difference:** `set_a - set_b`
- **Symmetric Difference:** `set_a ^ set_b`

### Comparisons

- **Subset:** `set_a.issubset(set_b)`
- **Superset:** `set_a.issuperset(set_b)`
- **Disjoint:** `set_a.isdisjoint(set_b)`

## Set Methods

- `add()` - Add element
- `update()` - Add multiple elements
- `remove()` - Remove element (error if not present)
- `discard()` - Remove element (no error)
- `pop()` - Remove and return random element

## Frozenset

Immutable version of sets:

```python
frozen = frozenset([1, 2, 3, 4])
# Can be used as dictionary key
```

## Practical Applications

- Finding unique values
- Fast membership testing
- Mathematical set theory
- Data cleaning