# 📦 Modules and Packages

## What are Modules?

Modules are Python files that contain functions, classes, and variables that can be reused in other programs.

## Importing Modules

### Import Complete Module

```python
import math
print(math.pi)        # 3.14159...
print(math.sqrt(16))  # 4.0
```

### Import Specific Functions

```python
from math import pi, sqrt
print(pi)        # 3.14159...
print(sqrt(16))  # 4.0
```

### Import with Alias

```python
import math as m
import datetime as dt

print(m.pi)
today = dt.date.today()
```

## Important Standard Modules

### math - Mathematical Functions

```python
import math

math.pi          # Pi constant
math.sqrt(x)     # Square root
math.ceil(x)     # Round up
math.floor(x)    # Round down
math.pow(x, y)   # Power
```

### random - Random Numbers

```python
import random

random.random()           # Random number 0-1
random.randint(1, 10)     # Random integer
random.choice(list)       # Random element
random.shuffle(list)      # Shuffle list
```

### datetime - Date and Time

```python
import datetime

now = datetime.datetime.now()
today = datetime.date.today()
time = datetime.time(14, 30, 0)
```

### os - Operating System

```python
import os

os.getcwd()              # Current directory
os.listdir('.')          # Files in directory
os.path.exists(path)     # Check if path exists
```

### json - JSON Data Processing

```python
import json

# Python to JSON
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)

# JSON to Python
data_back = json.loads(json_string)
```

## Collections Module

Advanced data structures:

```python
from collections import Counter, defaultdict, namedtuple

# Counter for frequencies
counter = Counter("hello world")
print(counter)  # Counter({'l': 3, 'o': 2, ...})

# defaultdict for automatic default values
dd = defaultdict(list)
dd['key'].append('value')

# namedtuple for structured data
Person = namedtuple('Person', 'name age')
alice = Person('Alice', 30)
```

## Creating Your Own Modules

1. Create a .py file (e.g., `my_module.py`)
2. Define functions and variables
3. Import the module in other files

```python
# my_module.py
def greeting(name):
    return f"Hello {name}!"

PI = 3.14159

# main_program.py
import my_module
print(my_module.greeting("World"))
```

## Packages

Packages are folders that contain multiple modules and are marked with an `__init__.py` file.

```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

## Module Search Path

Python searches for modules in:

1. Current directory
2. PYTHONPATH environment variable
3. Standard library
4. Site-packages (installed packages)

```python
import sys
print(sys.path)  # Shows search paths
```