# Part 2: Python Fortgeschritten - Learning Overview

## Modul 6: Erweiterte Funktionskonzepte

### 6.1 Funktionale Programmierung
```python
# Lambda-Funktionen
square = lambda x: x**2
add = lambda x, y: x + y

# map() - Funktion auf alle Elemente anwenden
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))

# filter() - Elemente filtern
evens = list(filter(lambda x: x % 2 == 0, numbers))

# reduce() - Sequenz zu einem Wert reduzieren
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)

# Closures
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(3)  # 8
```

### 6.2 Decorators
```python
# Function Decorator
def timer_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start}s")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(1)

# Property Decorator
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

    @area.setter
    def area(self, value):
        self._radius = (value / 3.14159) ** 0.5
```

### 6.3 Generators und Iterators
```python
# Generator Function
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Generator Expression
squares = (x**2 for x in range(10))

# Custom Iterator
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            self.current += 1
            return self.current - 1
        raise StopIteration
```

## Modul 7: Objektorientierte Programmierung

### 7.1 Klassen und Objekte
```python
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    # Class method
    @classmethod
    def create_puppy(cls, name):
        return cls(name, 0)

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 2
```

### 7.2 OOP-Prinzipien
```python
# Vererbung
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Multiple Vererbung
class Flyable:
    def fly(self):
        return "Flying high!"

class Bird(Animal, Flyable):
    def speak(self):
        return f"{self.name} chirps!"

# Abstract Base Classes
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

### 7.3 Magic Methods
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Index out of range")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

## Modul 8: Fehlerbehandlung und Debugging

### 8.1 Exception Handling
```python
# Try-Except-Else-Finally
try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found!")
except IOError as e:
    print(f"IO Error: {e}")
else:
    print("File read successfully")
finally:
    if 'file' in locals():
        file.close()

# Custom Exceptions
class ValidationError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

def validate_age(age):
    if age < 0:
        raise ValidationError("Age cannot be negative", "NEGATIVE_AGE")
    if age > 150:
        raise ValidationError("Age too high", "INVALID_AGE")
    return True

# Context Managers
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager('data.txt', 'r') as f:
    content = f.read()
```

### 8.2 Logging und Debugging
```python
import logging

# Logging Configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log'
)

logger = logging.getLogger(__name__)

# Logging Levels
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

# Debugging mit pdb
import pdb

def complex_function(x, y):
    result = x * y
    pdb.set_trace()  # Breakpoint
    result = result + 10
    return result

# Unit Testing
import unittest

class TestMathOperations(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 5

    def test_addition(self):
        self.assertEqual(self.a + self.b, 15)

    def test_subtraction(self):
        self.assertEqual(self.a - self.b, 5)

    def tearDown(self):
        del self.a
        del self.b

if __name__ == '__main__':
    unittest.main()
```

## Modul 9: File I/O und Datenformate

### 9.1 Dateioperationen
```python
# Text Files
with open('data.txt', 'r') as f:
    content = f.read()  # Entire file
    lines = f.readlines()  # List of lines

with open('output.txt', 'w') as f:
    f.write("Hello World\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# CSV Files
import csv

# Reading CSV
with open('data.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        print(row)

# Writing CSV
with open('output.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Alice', 'age': 30, 'city': 'Berlin'})

# JSON Files
import json

# Reading JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# Writing JSON
data = {'name': 'Python', 'version': 3.12}
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)

# Binary Files
with open('image.jpg', 'rb') as f:
    binary_data = f.read()

with open('copy.jpg', 'wb') as f:
    f.write(binary_data)
```

### 9.2 Reguläre Ausdrücke
```python
import re

# Pattern Matching
text = "The phone number is 123-456-7890"
pattern = r'\d{3}-\d{3}-\d{4}'
match = re.search(pattern, text)

if match:
    print(f"Found: {match.group()}")

# Finding All Matches
emails = "Contact: john@email.com, jane@company.org"
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
matches = re.findall(pattern, emails)

# Substitution
text = "The date is 2024-01-15"
new_text = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3.\2.\1', text)

# Groups and Capturing
pattern = r'(?P<name>\w+)@(?P<domain>\w+\.com)'
match = re.search(pattern, "john@example.com")
if match:
    print(match.group('name'))  # john
    print(match.group('domain'))  # example.com

# Compile for Performance
pattern = re.compile(r'\d+')
numbers = pattern.findall("There are 123 apples and 456 oranges")
```

## Modul 10: Module und Packages

### 10.1 Module erstellen
```python
# mymodule.py
"""
My custom module with utility functions.
"""

__version__ = '1.0.0'
__author__ = 'Your Name'

def greet(name):
    """Greet a person."""
    return f"Hello, {name}!"

class Calculator:
    """Simple calculator class."""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

if __name__ == "__main__":
    # Code that only runs when module is executed directly
    print("Module test:")
    print(greet("World"))
```

### Package Structure
```
mypackage/
├── __init__.py
├── module1.py
├── module2.py
├── subpackage/
│   ├── __init__.py
│   └── module3.py
└── tests/
    ├── __init__.py
    └── test_module1.py
```

### setup.py
```python
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of the package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mypackage",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.0",
        "numpy>=1.19.0",
    ],
)
```

## Best Practices für Part 2

1. **Funktionale Programmierung**: Nutze map, filter, reduce für sauberen Code
2. **OOP**: Befolge SOLID-Prinzipien
3. **Exceptions**: Spezifisch fangen, nie blankes except
4. **Logging**: Immer logging statt print in Production
5. **File I/O**: Immer Context Manager (with) verwenden
6. **Regex**: Compile häufig verwendete Patterns
7. **Module**: Klare Struktur und Dokumentation
8. **Testing**: Schreibe Tests für kritische Funktionen

## Weiterführende Ressourcen
- [Python Advanced Tutorial](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - Advanced Topics](https://realpython.com/tutorials/advanced/)
- [Python Design Patterns](https://python-patterns.guide/)
- [Effective Python Book](https://effectivepython.com/)