# 4.2 Tuples - Code Examples

# ========================================
# Creating Tuples
# ========================================
print("=" * 50)
print("CREATING TUPLES")
print("=" * 50)

# Different ways to create tuples
empty = ()
single = (42,)  # Comma important for single element!
numbers = (1, 2, 3, 4, 5)
mixed = (1, "Text", 3.14, True, None)
nested = ((1, 2), (3, 4), (5, 6))

print(f"Empty tuple: {empty}")
print(f"Single element: {single}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Nested: {nested}")

# Without parentheses (Tuple packing)
coordinates = 10, 20, 30
print(f"\nTuple packing: {coordinates}")

# With tuple() constructor
from_list = tuple([1, 2, 3])
from_string = tuple("Python")
from_range = tuple(range(5))

print(f"\nFrom list: {from_list}")
print(f"From string: {from_string}")
print(f"From range: {from_range}")

# ========================================
# Immutability
# ========================================
print("\n" + "=" * 50)
print("IMMUTABILITY")
print("=" * 50)

t = (1, 2, 3)
print(f"Original tuple: {t}")

# This would cause an error:
try:
    t[0] = 99
except TypeError as e:
    print(f"Error when changing: {e}")

# BUT: Mutable objects inside tuple can be changed
t_with_list = (1, [2, 3], 4)
print(f"\nTuple with list: {t_with_list}")
t_with_list[1].append(99)
print(f"After changing the list: {t_with_list}")

# ========================================
# Indexing and Slicing
# ========================================
print("\n" + "=" * 50)
print("INDEXING AND SLICING")
print("=" * 50)

t = ('a', 'b', 'c', 'd', 'e')
print(f"Tuple: {t}")

# Individual elements
print(f"First element [0]: {t[0]}")
print(f"Last element [-1]: {t[-1]}")
print(f"Middle element [2]: {t[2]}")

# Slicing
print(f"[1:4]: {t[1:4]}")
print(f"[:3]: {t[:3]}")
print(f"[2:]: {t[2:]}")
print(f"[::2]: {t[::2]}")
print(f"[::-1]: {t[::-1]}")  # Reverse

# ========================================
# Tuple Unpacking
# ========================================
print("\n" + "=" * 50)
print("TUPLE UNPACKING")
print("=" * 50)

# Simple unpacking
point = (10, 20)
x, y = point
print(f"x = {x}, y = {y}")

# Multiple assignment
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# With *-operator (Extended unpacking)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Ignoring values with _
data = ("Alice", 25, "Berlin", "Engineer")
name, _, city, _ = data
print(f"Name: {name}, City: {city}")

# Functions with multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"\nMin: {minimum}, Max: {maximum}")

# ========================================
# Tuple Methods
# ========================================
print("\n" + "=" * 50)
print("TUPLE METHODS")
print("=" * 50)

t = (1, 2, 3, 2, 4, 2, 5)
print(f"Tuple: {t}")

# count() - count occurrences
count = t.count(2)
print(f"Number 2 appears {count}x")

# index() - find position
position = t.index(4)
print(f"Position of 4: {position}")

# Other operations
print(f"Length: {len(t)}")
print(f"Maximum: {max(t)}")
print(f"Minimum: {min(t)}")
print(f"Sum: {sum(t)}")

# ========================================
# Named Tuples
# ========================================
print("\n" + "=" * 50)
print("NAMED TUPLES")
print("=" * 50)

from collections import namedtuple

# Define named tuple
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instance
alice = Person('Alice', 30, 'Berlin')
print(f"Person: {alice}")

# Access fields
print(f"Name: {alice.name}")
print(f"Age: {alice.age}")
print(f"City: {alice.city}")

# Index access still possible
print(f"Index [0]: {alice[0]}")

# Unpacking works
name, age, city = alice
print(f"Unpacked: {name}, {age}, {city}")

# _asdict() method
person_dict = alice._asdict()
print(f"As dictionary: {person_dict}")

# _replace() method
bob = alice._replace(name='Bob', age=25)
print(f"New person: {bob}")

# ========================================
# Tuples vs. Lists
# ========================================
print("\n" + "=" * 50)
print("TUPLES VS. LISTS")
print("=" * 50)

import sys
import time

# Memory usage
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(lista)} bytes")
print(f"Tuple size: {sys.getsizeof(tupla)} bytes")

# Performance during iteration
large_list = list(range(100000))
large_tuple = tuple(range(100000))

start = time.time()
for _ in large_list:
    pass
list_time = time.time() - start

start = time.time()
for _ in large_tuple:
    pass
tuple_time = time.time() - start

print(f"\nList iteration: {list_time:.6f}s")
print(f"Tuple iteration: {tuple_time:.6f}s")

# ========================================
# Practical Applications
# ========================================
print("\n" + "=" * 50)
print("PRACTICAL APPLICATIONS")
print("=" * 50)

# As dictionary keys
coordinates = {
    (0, 0): "Origin",
    (1, 0): "Right",
    (0, 1): "Up",
    (1, 1): "Diagonal"
}
print(f"Point (0,0): {coordinates[(0, 0)]}")

# Multiple return values
def statistics(numbers):
    return (
        min(numbers),
        max(numbers),
        sum(numbers) / len(numbers),
        len(numbers)
    )

stats = statistics([1, 2, 3, 4, 5])
min_val, max_val, avg_val, count = stats
print(f"\nStatistics: Min={min_val}, Max={max_val}, Avg={avg_val:.2f}, Count={count}")

# Store datasets
students = [
    ("Alice", 25, 1.3),
    ("Bob", 23, 2.0),
    ("Charlie", 24, 1.7)
]

for name, age, grade in students:
    print(f"{name} ({age} years): Grade {grade}")

# ========================================
# Tuple Operations
# ========================================
print("\n" + "=" * 50)
print("TUPLE OPERATIONS")
print("=" * 50)

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
combined = t1 + t2
print(f"{t1} + {t2} = {combined}")

# Repetition
repeated = t1 * 3
print(f"{t1} * 3 = {repeated}")

# Membership
print(f"2 in {t1}: {2 in t1}")
print(f"10 not in {t1}: {10 not in t1}")

# Comparisons (lexicographic)
t3 = (1, 2, 3)
t4 = (1, 2, 4)
print(f"\n{t3} < {t4}: {t3 < t4}")
print(f"{t3} == {t1}: {t3 == t1}")

# ========================================
# Advanced Techniques
# ========================================
print("\n" + "=" * 50)
print("ADVANCED TECHNIQUES")
print("=" * 50)

# Tuple as function arguments
def print_info(*args):
    """Any number of arguments"""
    for i, arg in enumerate(args, 1):
        print(f"  Argument {i}: {arg}")

print("Variable arguments:")
print_info("Python", 3.12, True)

# Zip with tuples
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)
cities = ("Berlin", "Munich", "Hamburg")

people = list(zip(names, ages, cities))
print(f"\nZipped people: {people}")

# Enumerate with tuples
for index, (name, age, city) in enumerate(people):
    print(f"{index}: {name} ({age}) from {city}")

# Sort tuples
points = [(3, 2), (1, 4), (2, 1), (3, 1)]
sorted_x = sorted(points)  # By first element
sorted_y = sorted(points, key=lambda p: p[1])  # By second element

print(f"\nSorted by x: {sorted_x}")
print(f"Sorted by y: {sorted_y}")