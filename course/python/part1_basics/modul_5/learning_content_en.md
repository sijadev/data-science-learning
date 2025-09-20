# Module 5: Function Basics

## 5.1 Function Definition

### Learning Objectives
- Define and call functions
- Understand parameters and arguments
- Use return values
- Write docstrings
- Apply type hints

### Core Concepts

#### Basic Function Structure
```python
def function_name(parameters):
    """Docstring - function description"""
    # Function body
    return value  # Optional
```

#### Parameter Types

##### Positional Parameters
```python
def greet(name, age):
    return f"Hello {name}, you are {age} years old"

greet("Alice", 30)  # Order matters
```

##### Keyword Arguments
```python
greet(age=30, name="Alice")  # Order doesn't matter
```

##### Default Parameters
```python
def greet(name, title="Mr./Ms."):
    return f"Good day, {title} {name}"

greet("Schmidt")           # Uses default
greet("Weber", "Dr.")      # Overrides default
```

##### Variable Parameters (*args)
```python
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4, 5)  # Any number of arguments
```

##### Keyword Parameters (**kwargs)
```python
def create_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(name="Alice", age=30, city="Berlin")
```

##### Combination of All Parameter Types
```python
def flexible_func(pos1, pos2, *args, default="value", **kwargs):
    # Order: positional, *args, default, **kwargs
    pass
```

#### Return Values

##### No Return (None)
```python
def print_message(msg):
    print(msg)
    # Implicit return None
```

##### Single Value
```python
def square(x):
    return x ** 2
```

##### Multiple Values (Tuple)
```python
def get_name_age():
    return "Alice", 30

name, age = get_name_age()  # Tuple unpacking
```

##### Conditional Return
```python
def check_positive(number):
    if number > 0:
        return True
    return False
```

#### Docstrings
```python
def calculate_area(width, height):
    """
    Calculates the area of a rectangle.

    Args:
        width (float): Width of the rectangle
        height (float): Height of the rectangle

    Returns:
        float: The area of the rectangle

    Raises:
        ValueError: If width or height is negative

    Example:
        >>> calculate_area(5, 3)
        15
    """
    if width < 0 or height < 0:
        raise ValueError("Negative values not allowed")
    return width * height
```

#### Type Hints (Python 3.5+)
```python
from typing import List, Dict, Optional, Union

def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

def flexible_input(value: Union[int, str]) -> str:
    return str(value)
```

#### Functions as First-Class Objects
```python
# Functions can be assigned to variables
my_func = len

# Passed as parameters
def apply_to_list(lst, func):
    return [func(x) for x in lst]

# Stored in data structures
operations = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y
}
```

### Best Practices

#### Function Design
1. **Single Responsibility**: One function, one task
2. **Meaningful names**: `calculate_tax()` instead of `calc()`
3. **Short functions**: Maximum 20-30 lines
4. **No side effects**: Avoid global modifications

#### Parameters
1. **Few parameters**: Maximum 4-5 parameters
2. **Defaults for optional values**
3. **Immutable defaults**: Never `[]` or `{}` as default

```python
# Wrong
def add_item(item, lst=[]):
    lst.append(item)
    return lst

# Right
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

#### Documentation
1. **Always docstrings** for public functions
2. **Type hints** for better IDE support
3. **Examples** in docstrings

---

## 5.2 Scope and Namespaces

### Learning Objectives
- Understand and apply LEGB rule
- Use global and nonlocal keywords
- Create and use closures
- Master namespace concepts

### Core Concepts

#### LEGB Rule
Python searches for variables in this order:

1. **Local**: Within the current function
2. **Enclosing**: In enclosing functions
3. **Global**: At module level
4. **Built-in**: Built-in names (len, print, etc.)

```python
x = "Global"  # Global

def outer():
    x = "Enclosing"  # Enclosing

    def inner():
        x = "Local"  # Local
        print(x)     # Finds "Local"

    inner()

outer()
```

#### Local Scope
```python
def my_function():
    local_var = "Only available here"
    print(local_var)  # OK

my_function()
# print(local_var)  # NameError!
```

#### Global Scope
```python
global_var = "Available everywhere"

def access_global():
    print(global_var)  # Reading OK

def modify_global():
    global global_var  # Necessary for modification
    global_var = "Changed"

access_global()
modify_global()
```

#### Enclosing Scope (Closures)
```python
def outer_function(x):
    def inner_function(y):
        return x + y  # x from enclosing scope
    return inner_function

add_5 = outer_function(5)
result = add_5(3)  # 8
```

#### nonlocal Keyword
```python
def create_counter():
    count = 0

    def increment():
        nonlocal count  # Access enclosing variable
        count += 1
        return count

    return increment

counter = create_counter()
print(counter())  # 1
print(counter())  # 2
```

### Closures

#### What are Closures?
Functions that access variables from their enclosing scope:

```python
def multiplier_factory(factor):
    def multiplier(number):
        return number * factor  # factor is "captured"
    return multiplier

double = multiplier_factory(2)
triple = multiplier_factory(3)

print(double(5))  # 10
print(triple(5))  # 15
```

#### Practical Applications
```python
# Configuration
def create_api_client(base_url, api_key):
    def make_request(endpoint):
        return f"GET {base_url}/{endpoint} (key: {api_key})"
    return make_request

client = create_api_client("https://api.example.com", "secret123")

# State management
def create_accumulator(start=0):
    total = start

    def add(value):
        nonlocal total
        total += value
        return total

    def get():
        return total

    return add, get

add_func, get_func = create_accumulator(10)
```

### Namespace Debugging

#### globals() and locals()
```python
global_var = "Global value"

def debug_function():
    local_var = "Local value"

    print("Globals:", list(globals().keys())[:5])
    print("Locals:", locals())

debug_function()
```

#### vars() Function
```python
class Example:
    def __init__(self):
        self.attr = "value"

obj = Example()
print(vars(obj))  # {'attr': 'value'}
```

### Common Errors and Solutions

#### UnboundLocalError
```python
# Error
count = 0
def increment():
    count += 1  # UnboundLocalError!

# Solution
count = 0
def increment():
    global count
    count += 1
```

#### Mutable Default Arguments
```python
# Dangerous
def add_item(item, lst=[]):
    lst.append(item)
    return lst

# Safe
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

#### Late Binding Closures
```python
# Unexpected behavior
functions = []
for i in range(3):
    functions.append(lambda: i)  # All reference the same i!

# All return 2
for f in functions:
    print(f())  # 2, 2, 2

# Solution: Default parameter
functions = []
for i in range(3):
    functions.append(lambda x=i: x)  # x is bound at definition time

# Or: Closure factory
def make_closure(i):
    return lambda: i

functions = [make_closure(i) for i in range(3)]
```

### Best Practices

#### Scope Management
1. **Minimize global variables**
2. **Use classes** for state instead of global variables
3. **Explicit parameters** instead of global access
4. **Closures for configuration** and state

#### Naming
1. **Unique names** in different scopes
2. **`_private`** convention for "private" variables
3. **CONSTANTS** in UPPERCASE

#### Code Organization
```python
# Well structured
class DatabaseConfig:
    HOST = "localhost"
    PORT = 5432

    @classmethod
    def get_connection_string(cls):
        return f"postgresql://{cls.HOST}:{cls.PORT}"

# Instead of global variables
def create_processor(config):
    def process(data):
        # Uses config from closure
        return f"Processing {data} with {config}"
    return process
```

### Further Resources
- [Python Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [Real Python - Python Scope](https://realpython.com/python-scope-legb-rule/)
- [Closures in Python](https://realpython.com/python-closures/)
- [Function Documentation Guide](https://peps.python.org/pep-0257/)