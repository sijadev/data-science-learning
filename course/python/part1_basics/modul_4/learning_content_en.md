# Module 4: Data Structures

## 4.1 Lists (already created)

### Learning Objectives
- Create, manipulate and iterate through lists
- Understand and apply list comprehensions
- Master important list methods
- Use slicing and indexing

---

## 4.2 Tuples

### Learning Objectives
- Understand immutability of tuples
- Master tuple unpacking
- Use named tuples
- Know when to use tuples instead of lists

### Core Concepts

#### Tuple Properties
- **Immutable**: Cannot be changed after creation
- **Ordered**: Elements have a fixed order
- **Allow duplicates**: Same values can appear multiple times
- **Hashable**: Can be used as dictionary keys

#### Tuple Creation
```python
# Different syntaxes
empty = ()
single = (42,)  # Comma important!
coordinates = (10, 20)
without_parentheses = 1, 2, 3  # Tuple packing

# From other types
from_list = tuple([1, 2, 3])
from_string = tuple("ABC")  # ('A', 'B', 'C')
```

#### Tuple Unpacking
```python
point = (10, 20)
x, y = point

# Extended unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
# first=1, middle=[2,3,4], last=5

# Ignoring values
name, _, age = ("Alice", "unimportant", 30)
```

#### Named Tuples
```python
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])
alice = Person('Alice', 30, 'Berlin')

print(alice.name)  # Access via attribute
print(alice[0])    # Access via index
```

### When to Use Tuples?
- **Coordinates**: `(x, y, z)`
- **Records**: `(name, age, email)`
- **Dictionary keys**: Immutable combinations
- **Function returns**: Multiple related values
- **Performance**: Slightly faster than lists for iteration

---

## 4.3 Dictionaries

### Learning Objectives
- Understand and use key-value pairs
- Master dictionary methods
- Apply dictionary comprehensions
- Manage nested dictionaries

### Core Concepts

#### Dictionary Properties
- **Key-value structure**: Mapping of keys to values
- **No duplicates**: Each key is unique
- **Mutable**: Can be changed after creation
- **Unordered** (Python < 3.7) / **Ordered** (Python ≥ 3.7)

#### Dictionary Creation
```python
# Different syntaxes
person = {"name": "Alice", "age": 30}
numbers = dict(one=1, two=2, three=3)
from_list = dict([("a", 1), ("b", 2)])

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
```

#### Access and Manipulation
```python
# Safe access
value = dict.get("key", "default")

# Add/modify
dict["new_key"] = "new_value"
dict.update({"key1": "value1", "key2": "value2"})

# Remove
value = dict.pop("key")
del dict["key"]
```

#### Iteration
```python
for key in dict:                    # Over keys
for value in dict.values():         # Over values
for key, value in dict.items():     # Over pairs
```

### Practical Applications
- **Configuration**: Store settings
- **Caching**: Store calculated values
- **Grouping**: Organize data by categories
- **Counting**: Determine frequencies
- **Mapping**: Define relationships

---

## 4.4 Sets

### Learning Objectives
- Understand and apply set operations
- Efficiently remove duplicates
- Use set comprehensions
- Learn about frozen sets

### Core Concepts

#### Set Properties
- **No duplicates**: Each value is unique
- **Unordered**: No fixed order
- **Mutable**: Can be changed after creation
- **Only hashable elements**: Immutable types only

#### Set Creation
```python
# Different syntaxes
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 3, 2, 1])  # {1, 2, 3}
empty = set()  # Not {} - that's a dictionary!

# Set comprehension
evens = {x for x in range(10) if x % 2 == 0}
```

#### Set Operations
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union
a | b  # or a.union(b)

# Intersection
a & b  # or a.intersection(b)

# Difference
a - b  # or a.difference(b)

# Symmetric difference
a ^ b  # or a.symmetric_difference(b)
```

#### Comparisons
```python
# Subset
{1, 2}.issubset({1, 2, 3, 4})  # True

# Superset
{1, 2, 3}.issuperset({1, 2})   # True

# Disjoint (no common elements)
{1, 2}.isdisjoint({3, 4})      # True
```

#### Frozen Sets
```python
fs = frozenset([1, 2, 3])
# Immutable, can be used as dict key
```

### Practical Applications
- **Remove duplicates**: `list(set(lista))`
- **Membership tests**: Very fast for large datasets
- **Set comparisons**: Find common/different elements
- **Filtering**: Filter elements based on membership

---

## Comparison of Data Structures

| Property | List | Tuple | Dictionary | Set |
|----------|------|-------|------------|-----|
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Ordered | ✅ | ✅ | ✅ (3.7+) | ❌ |
| Duplicates | ✅ | ✅ | ❌ (Keys) | ❌ |
| Indexing | ✅ | ✅ | Key-based | ❌ |
| Slicing | ✅ | ✅ | ❌ | ❌ |
| Hashable | ❌ | ✅ | ❌ | ❌ |

## Best Practices

### Lists
- For sequences of mutable data
- When order is important
- For data that changes frequently

### Tuples
- For immutable sequences
- As dictionary keys
- For coordinates and records
- Return values from functions

### Dictionaries
- For key-value mappings
- Fast lookups
- Structured data
- Configurations and mappings

### Sets
- For unique values
- Set operations
- Fast membership tests
- Remove duplicates

### Performance Tips
1. **Membership test**: Set > Dict > List
2. **Sorted data**: Use `bisect` for lists
3. **Large datasets**: Choose right data structure
4. **Memory**: Tuple < List, Sets are memory-efficient

### Common Errors
1. **Empty set**: `set()` not `{}`
2. **Dictionary vs. Set**: `{}` is dictionary
3. **Tuple with one element**: `(42,)` not `(42)`
4. **Immutable keys**: Only hashable types in sets/dict keys
5. **List as dict key**: Not possible, use tuple

### Further Resources
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python - Python Data Structures](https://realpython.com/python-data-structures/)
- [Collections Module](https://docs.python.org/3/library/collections.html)