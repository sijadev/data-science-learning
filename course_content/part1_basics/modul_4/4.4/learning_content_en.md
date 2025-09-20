# 📚 Dictionaries

## What are Dictionaries?

Dictionaries store key-value pairs and allow fast access via keys.

```python
person = {
    "name": "Alice",
    "age": 30,
    "profession": "Developer"
}
```

## Dictionary Operations

### Accessing Values

```python
# Direct access
name = person["name"]

# Safe access
profession = person.get("profession", "Unknown")
```

### Adding and Modifying

```python
person["salary"] = 75000  # New key
person["age"] = 31        # Change value
```

### Removing Elements

- `pop()` - Removes and returns value
- `popitem()` - Removes last element
- `del` - Deletes key-value pair

## Dictionary Methods

- `keys()` - All keys
- `values()` - All values
- `items()` - All key-value pairs
- `update()` - Adds another dictionary
- `clear()` - Empties the dictionary

## Iteration

```python
# Over keys
for key in person:
    print(key, person[key])

# Over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

## Dictionary Comprehensions

```python
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

word_lengths = {word: len(word) for word in ["Python", "is", "great"]}
```

## Nested Dictionaries

```python
students = {
    "alice": {
        "grades": {"Math": 1, "Physics": 2},
        "semester": 3
    },
    "bob": {
        "grades": {"Math": 2, "Physics": 1},
        "semester": 2
    }
}
```

## Practical Applications

- Configuration data
- Database results
- Mapping tables
- Counters and statistics
- API responses