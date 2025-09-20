# Module 3: Control Structures

## 3.1 Conditional Statements

### Learning Objectives
- Understand and apply if, elif, else statements
- Structure nested conditions
- Use the ternary operator
- Master match-case (pattern matching)

### Core Concepts

#### if-elif-else Structure
```python
if condition1:
    # Code when condition1 is True
    pass
elif condition2:
    # Code when condition1 is False and condition2 is True
    pass
else:
    # Code when all conditions are False
    pass
```

#### Nested Conditions
```python
# Nested
if outer_condition:
    if inner_condition:
        do_something()

# Better with logical operators
if outer_condition and inner_condition:
    do_something()
```

#### Ternary Operator (Conditional Expression)
```python
# Syntax: value_if_true if condition else value_if_false
status = "active" if is_active else "inactive"

# Equivalent to:
if is_active:
    status = "active"
else:
    status = "inactive"
```

#### match-case (Python 3.10+)
Pattern matching for complex conditions:
```python
match value:
    case pattern1:
        action1()
    case pattern2 | pattern3:  # Multiple patterns
        action2()
    case pattern4 if condition:  # Guard
        action3()
    case _:  # Default
        default_action()
```

**Pattern Types**:
- Literal Patterns: `case 42:`, `case "hello":`
- Capture Patterns: `case x:` (binds value to variable)
- Sequence Patterns: `case [x, y, z]:`
- Mapping Patterns: `case {"key": value}:`
- Class Patterns: `case Point(x=0, y=0):`

#### Truthy and Falsy Values
**Falsy** (interpreted as False):
- `None`
- `False`
- `0`, `0.0`, `0j`
- `""`, `[]`, `()`, `{}`, `set()`

**Truthy**: All other values

### Best Practices
1. **Prefer flat structures**: Avoid too many nested levels
2. **Guard clauses**: Return early instead of deep nesting
3. **Explicit comparisons**: `if x is None:` instead of `if not x:`
4. **match-case for complex logic**: When having many elif branches

### Common Errors

#### Error: = instead of ==
```python
# Error
if x = 5:  # SyntaxError!
    pass

# Correct
if x == 5:
    pass
```

#### Error: Mutable default values
```python
# Dangerous
def add_item(item, lista=[]):
    lista.append(item)
    return lista

# Safe
def add_item(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista
```

---

## 3.2 Loops

### Learning Objectives
- Master for and while loops
- Use range(), enumerate(), zip()
- Understand break, continue and else in loops
- Understand list comprehensions

### Core Concepts

#### for Loop
Iterates over sequences:
```python
for element in sequence:
    process(element)

# With index
for i, element in enumerate(sequence):
    print(f"{i}: {element}")

# Parallel iteration
for a, b in zip(list1, list2):
    process(a, b)
```

#### while Loop
Runs while condition is True:
```python
while condition:
    do_something()
    update_condition()

# Infinite loop with break
while True:
    if exit_condition:
        break
    process()
```

#### range() Function
Generates number sequences:
```python
range(stop)           # 0 to stop-1
range(start, stop)    # start to stop-1
range(start, stop, step)  # with step size
```

**Examples**:
```python
range(5)        # 0, 1, 2, 3, 4
range(2, 8)     # 2, 3, 4, 5, 6, 7
range(10, 0, -2)  # 10, 8, 6, 4, 2
```

#### enumerate() Function
Adds index to iterables:
```python
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

#### zip() Function
Combines multiple iterables:
```python
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

#### break and continue
- **break**: Exits loop completely
- **continue**: Jumps to next iteration

```python
for i in range(10):
    if i == 5:
        break  # Stops at 5
    if i % 2 == 0:
        continue  # Skips even numbers
    print(i)  # Only 1, 3
```

#### else in Loops
Executed when loop is **not** terminated by break:
```python
for item in items:
    if condition(item):
        break
else:
    print("No item met the condition")
```

#### List Comprehensions
Compact syntax for list creation:
```python
# Traditional
squares = []
for x in range(5):
    squares.append(x**2)

# Comprehension
squares = [x**2 for x in range(5)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
```

### Loop Patterns

#### Counter Pattern
```python
counter = 0
for item in items:
    if condition(item):
        counter += 1
```

#### Accumulator Pattern
```python
total = 0
for number in numbers:
    total += number
```

#### Flag Pattern
```python
found = False
for item in items:
    if condition(item):
        found = True
        break
```

#### Sentinel Pattern
```python
while True:
    data = get_input()
    if data == SENTINEL:
        break
    process(data)
```

### Performance Tips
1. **List comprehensions**: Faster than append in loop
2. **Generator expressions**: Memory-efficient for large datasets
3. **join() instead of +=**: For string concatenation
4. **enumerate() instead of range(len())**: More Pythonic and readable

### Practical Examples

#### Finding prime numbers
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(100) if is_prime(n)]
```

#### Fibonacci sequence
```python
def fibonacci(n):
    a, b = 0, 1
    result = []
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result
```

#### Nested iteration
```python
# Multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()
```

### Common Errors and Solutions

#### Infinite loops
```python
# Error
i = 0
while i < 10:
    print(i)
    # i is never incremented!

# Solution
i = 0
while i < 10:
    print(i)
    i += 1
```

#### Modification during iteration
```python
# Dangerous
lista = [1, 2, 3, 4, 5]
for item in lista:
    if item % 2 == 0:
        lista.remove(item)  # Error!

# Safe
lista = [1, 2, 3, 4, 5]
lista = [item for item in lista if item % 2 != 0]
```

### Further Resources
- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python - Conditionals](https://realpython.com/python-conditional-statements/)
- [Python Loops Tutorial](https://realpython.com/python-for-loop/)
- [List Comprehensions Guide](https://realpython.com/list-comprehension-python/)