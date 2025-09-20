# Module 2: Data Types and Variables

## 2.1 Basic Data Types

### Learning Objectives
- Understand fundamental data types in Python
- Perform type casting and type conversion
- Work with different number formats
- Master string operations

### Core Concepts

#### Numeric Types

##### Integer (int)
Whole numbers without decimal point:
```python
age = 25
negative = -42
binary = 0b1010     # 10 in decimal
hexadecimal = 0xFF  # 255 in decimal
million = 1_000_000 # Underscores for readability
```

##### Float
Floating-point numbers with decimal point:
```python
pi = 3.14159
temperature = -17.5
scientific = 2.5e-3  # 0.0025
```
**Warning**: Floating-point arithmetic is not exact!
```python
0.1 + 0.2 == 0.3  # False!
```

##### Complex
Complex numbers with real and imaginary parts:
```python
z = 3 + 4j
z.real    # 3.0
z.imag    # 4.0
abs(z)    # 5.0 (magnitude)
```

#### String (str)
Text strings:
```python
single = 'Single quotes'
double = "Double quotes"
triple = """Multi-line
string"""
raw = r"Raw string: \n not interpreted"
```

**String Operations**:
- Indexing: `text[0]` (first character)
- Slicing: `text[1:5]` (substring)
- Concatenation: `"Hello" + " " + "World"`
- Repetition: `"Ha" * 3` → "HaHaHa"
- Methods: `.upper()`, `.lower()`, `.strip()`, `.split()`

#### Boolean (bool)
Truth values True and False:
```python
is_active = True
is_deleted = False
```

**Falsy Values** (interpreted as False):
- `0`, `0.0`, `0j`
- `""` (empty string)
- `[]`, `()`, `{}` (empty containers)
- `None`

**Truthy Values**: All other values

#### None
Represents "no value" or "undefined":
```python
result = None
if result is None:  # Best practice: use 'is'
    print("No result")
```

#### Type Casting
Explicit type conversion:
```python
int("42")      # String to integer
float("3.14")  # String to float
str(100)       # Number to string
bool(1)        # Number to boolean
list("abc")    # String to list ['a', 'b', 'c']
```

### Practical Exercises
1. Create and convert different number formats
2. Perform string manipulations
3. Type casting with error handling
4. Test truthy/falsy values

---

## 2.2 Variables and Operators

### Learning Objectives
- Understand variable assignment and naming conventions
- Master all operator types
- Understand operator precedence
- Correctly evaluate expressions

### Core Concepts

#### Variable Assignment
```python
# Simple assignment
name = "Python"

# Multiple assignment
x, y, z = 1, 2, 3

# Same values
a = b = c = 0

# Tuple unpacking
coordinates = (10, 20)
x, y = coordinates

# Variable swapping
x, y = y, x
```

#### Arithmetic Operators
| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| + | Addition | 10 + 3 | 13 |
| - | Subtraction | 10 - 3 | 7 |
| * | Multiplication | 10 * 3 | 30 |
| / | Division | 10 / 3 | 3.333... |
| // | Floor division | 10 // 3 | 3 |
| % | Modulo (remainder) | 10 % 3 | 1 |
| ** | Exponentiation | 2 ** 3 | 8 |

#### Comparison Operators
```python
==  # Equal
!=  # Not equal
>   # Greater than
<   # Less than
>=  # Greater than or equal
<=  # Less than or equal
```

**Chained Comparisons**:
```python
1 < x < 10  # Equivalent to: 1 < x and x < 10
```

#### Logical Operators
```python
and  # Logical AND
or   # Logical OR
not  # Logical NOT
```

**Short-Circuit Evaluation**:
- `and` stops at first False
- `or` stops at first True

#### Bitwise Operators
```python
&   # Bitwise AND
|   # Bitwise OR
^   # Bitwise XOR
~   # Bitwise NOT
<<  # Left shift
>>  # Right shift
```

#### Assignment Operators
```python
+=   # x += 5  → x = x + 5
-=   # x -= 3  → x = x - 3
*=   # x *= 2  → x = x * 2
/=   # x /= 2  → x = x / 2
//=  # x //= 2 → x = x // 2
%=   # x %= 3  → x = x % 3
**=  # x **= 2 → x = x ** 2
```

#### Identity and Membership Operators
```python
# Identity (compares object IDs)
is      # x is y
is not  # x is not y

# Membership
in      # x in sequence
not in  # x not in sequence
```

#### Walrus Operator := (Python 3.8+)
Assignment in expressions:
```python
if (n := len(data)) > 10:
    print(f"List has {n} elements")
```

### Operator Precedence
From highest to lowest:
1. `()` Parentheses
2. `**` Exponentiation
3. `+x`, `-x`, `~x` Unary operators
4. `*`, `/`, `//`, `%`
5. `+`, `-`
6. `<<`, `>>`
7. `&`
8. `^`
9. `|`
10. `==`, `!=`, `<`, `<=`, `>`, `>=`
11. `is`, `is not`, `in`, `not in`
12. `not`
13. `and`
14. `or`

### Best Practices
1. **Meaningful variable names**: `user_age` instead of `a`
2. **Constants in UPPERCASE**: `MAX_SIZE = 100`
3. **Spaces around operators**: `x = y + z` not `x=y+z`
4. **Parentheses for clarity**: `(a + b) * c` when uncertain
5. **`is` for None comparison**: `if x is None:` not `if x == None:`

### Common Errors and Solutions

#### Integer Division
```python
# Error: Unexpected result
result = 5 / 2  # 2.5 (float)

# Solution: Use floor division
result = 5 // 2  # 2 (int)
```

#### Mutable Default Arguments
```python
# Error
def add_item(item, lista=[]):  # Dangerous!
    lista.append(item)
    return lista

# Solution
def add_item(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista
```

### Practical Exercises
1. Calculator with all arithmetic operations
2. Implement bit flags for permissions
3. Evaluate expressions with different operator precedence
4. Demonstrate short-circuit evaluation

### Further Resources
- [Python Operators Documentation](https://docs.python.org/3/library/operator.html)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Real Python - Operators and Expressions](https://realpython.com/python-operators-expressions/)