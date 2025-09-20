# 4.3 Dictionaries - Code Examples

# ========================================
# Creating Dictionaries
# ========================================
print("=" * 50)
print("CREATING DICTIONARIES")
print("=" * 50)

# Different ways to create dictionaries
empty = {}
person = {"name": "Alice", "age": 30, "city": "Berlin"}
numbers = {1: "one", 2: "two", 3: "three"}
mixed = {"string": "text", 42: "number", (1, 2): "tuple"}

print(f"Empty dict: {empty}")
print(f"Person: {person}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")

# With dict() constructor
d1 = dict(name="Bob", age=25)
d2 = dict([("a", 1), ("b", 2), ("c", 3)])
d3 = dict(zip(["x", "y", "z"], [1, 2, 3]))

print(f"\ndict() with keywords: {d1}")
print(f"dict() with list: {d2}")
print(f"dict() with zip: {d3}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(f"\nSquare numbers: {squares}")

# ========================================
# Accessing Elements
# ========================================
print("\n" + "=" * 50)
print("ACCESSING ELEMENTS")
print("=" * 50)

person = {"name": "Alice", "age": 30, "city": "Berlin"}

# Direct access
print(f"Name: {person['name']}")

# get() method (safer)
print(f"Age: {person.get('age')}")
print(f"Country (with default): {person.get('country', 'Germany')}")

# Error handling
try:
    print(person['phone'])
except KeyError:
    print("Key 'phone' not found")

# All keys, values, items
print(f"\nKeys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# ========================================
# Dictionary Methods
# ========================================
print("\n" + "=" * 50)
print("DICTIONARY METHODS")
print("=" * 50)

d = {"a": 1, "b": 2}
print(f"Start: {d}")

# Add/modify
d["c"] = 3
print(f"After d['c'] = 3: {d}")

# update() - multiple items
d.update({"d": 4, "e": 5})
print(f"After update(): {d}")

# setdefault() - only if not present
d.setdefault("f", 6)
d.setdefault("a", 999)  # Doesn't change anything, since 'a' exists
print(f"After setdefault(): {d}")

# pop() - remove with return
value = d.pop("b")
print(f"After pop('b'): {d}, removed: {value}")

# popitem() - remove last item
item = d.popitem()
print(f"After popitem(): {d}, removed: {item}")

# del - delete key
del d["c"]
print(f"After del d['c']: {d}")

# clear() - delete everything
copy = d.copy()
copy.clear()
print(f"After clear(): {copy}")

# ========================================
# Dictionary Iteration
# ========================================
print("\n" + "=" * 50)
print("DICTIONARY ITERATION")
print("=" * 50)

products = {
    "Apple": 0.50,
    "Banana": 0.30,
    "Orange": 0.60,
    "Mango": 1.20
}

print("Iterate over keys:")
for product in products:
    print(f"  {product}: {products[product]}€")

print("\nIterate over values:")
for price in products.values():
    print(f"  Price: {price}€")

print("\nIterate over items:")
for product, price in products.items():
    print(f"  {product} costs {price}€")

# ========================================
# Dictionary Comprehensions
# ========================================
print("\n" + "=" * 50)
print("DICTIONARY COMPREHENSIONS")
print("=" * 50)

# Simple comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Square numbers: {squares}")

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even square numbers: {even_squares}")

# Reverse a dictionary
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(f"\nOriginal: {original}")
print(f"Reversed: {reversed_dict}")

# Filtering
prices = {"Apple": 0.5, "Banana": 0.3, "Mango": 1.2, "Orange": 0.6}
cheap = {k: v for k, v in prices.items() if v < 0.6}
print(f"\nCheap products: {cheap}")

# ========================================
# Nested Dictionaries
# ========================================
print("\n" + "=" * 50)
print("NESTED DICTIONARIES")
print("=" * 50)

company = {
    "employees": {
        "alice": {"age": 30, "position": "Developer"},
        "bob": {"age": 25, "position": "Designer"},
        "charlie": {"age": 35, "position": "Manager"}
    },
    "location": "Berlin",
    "founded": 2020
}

print(f"Company: {company['location']}")
print(f"Alice's position: {company['employees']['alice']['position']}")

# Iterate over nested structure
print("\nAll employees:")
for name, info in company["employees"].items():
    print(f"  {name.capitalize()}: {info['position']} ({info['age']} years)")

# ========================================
# defaultdict and OrderedDict
# ========================================
print("\n" + "=" * 50)
print("DEFAULTDICT AND ORDEREDDICT")
print("=" * 50)

from collections import defaultdict, OrderedDict

# defaultdict - automatic defaults
dd = defaultdict(list)
dd["fruits"].append("Apple")
dd["fruits"].append("Banana")
dd["vegetables"].append("Carrot")
print(f"defaultdict: {dict(dd)}")

# Count words with defaultdict
text = "python is great python is fun"
word_count = defaultdict(int)
for word in text.split():
    word_count[word] += 1
print(f"\nWord count: {dict(word_count)}")

# OrderedDict (important for order before Python 3.7)
od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3
print(f"\nOrderedDict: {od}")

# ========================================
# Dictionary Merging
# ========================================
print("\n" + "=" * 50)
print("DICTIONARY MERGING")
print("=" * 50)

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {"b": 99, "e": 5}

# With update() (modifies d1)
copy = d1.copy()
copy.update(d2)
print(f"update(): {copy}")

# With ** unpacking (Python 3.5+)
merged = {**d1, **d2}
print(f"Unpacking: {merged}")

# With | operator (Python 3.9+)
merged_new = d1 | d2
print(f"Union operator: {merged_new}")

# Overwrite on conflicts
merged_conflict = {**d1, **d3}
print(f"With conflict: {merged_conflict}")  # b gets overwritten

# ========================================
# Practical Examples
# ========================================
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Grouping
students = [
    {"name": "Alice", "course": "Python", "grade": 1.3},
    {"name": "Bob", "course": "Java", "grade": 2.0},
    {"name": "Charlie", "course": "Python", "grade": 1.7},
    {"name": "Diana", "course": "Java", "grade": 1.5}
]

courses = {}
for student in students:
    course = student["course"]
    if course not in courses:
        courses[course] = []
    courses[course].append(student["name"])

print("Students by course:")
for course, names in courses.items():
    print(f"  {course}: {', '.join(names)}")

# Cache/Memoization
cache = {}
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result

print(f"\nFibonacci(10): {fibonacci(10)}")
print(f"Cache: {cache}")

# Configuration
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "admin"
    },
    "api": {
        "key": "secret123",
        "timeout": 30
    }
}

db_host = config["database"]["host"]
api_timeout = config["api"]["timeout"]
print(f"\nDB Host: {db_host}, API Timeout: {api_timeout}s")

# ========================================
# Performance and Tips
# ========================================
print("\n" + "=" * 50)
print("PERFORMANCE AND TIPS")
print("=" * 50)

import time

# Dictionary vs. list for search
large_list = list(range(100000))
large_dict = {i: i for i in range(100000)}

# Search in list
start = time.time()
_ = 99999 in large_list
list_time = time.time() - start

# Search in dictionary
start = time.time()
_ = 99999 in large_dict
dict_time = time.time() - start

print(f"Search in list: {list_time:.6f}s")
print(f"Search in dict: {dict_time:.6f}s")
print(f"Dict is {list_time/dict_time:.0f}x faster")

# ========================================
# Dictionary as Switch Statement
# ========================================
print("\n" + "=" * 50)
print("DICTIONARY AS SWITCH")
print("=" * 50)

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication
}

a, b = 10, 5
for op, func in operations.items():
    result = func(a, b)
    print(f"{a} {op} {b} = {result}")