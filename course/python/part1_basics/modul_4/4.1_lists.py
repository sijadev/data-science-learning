# 4.1 Lists - Code Examples

# ========================================
# Creating Lists
# ========================================
print("=" * 50)
print("CREATING LISTS")
print("=" * 50)

# Different ways to create lists
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Text", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

print(f"Empty list: {empty}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Nested: {nested}")

# With list() constructor
from_string = list("Python")
from_range = list(range(5))
from_tuple = list((1, 2, 3))

print(f"\nFrom string: {from_string}")
print(f"From range: {from_range}")
print(f"From tuple: {from_tuple}")

# ========================================
# Indexing and Slicing
# ========================================
print("\n" + "=" * 50)
print("INDEXING AND SLICING")
print("=" * 50)

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f"List: {lista}")

# Individual elements
print(f"\nFirst element [0]: {lista[0]}")
print(f"Last element [-1]: {lista[-1]}")
print(f"Third element [2]: {lista[2]}")
print(f"Second last [-2]: {lista[-2]}")

# Slicing [start:stop:step]
print(f"\n[1:4]: {lista[1:4]}")
print(f"[:3]: {lista[:3]}")
print(f"[3:]: {lista[3:]}")
print(f"[::2]: {lista[::2]}")
print(f"[::-1]: {lista[::-1]}")  # Reverse

# Slice assignment
copy = lista.copy()
copy[1:3] = ['X', 'Y']
print(f"\nAfter copy[1:3] = ['X', 'Y']: {copy}")

# ========================================
# List Methods
# ========================================
print("\n" + "=" * 50)
print("LIST METHODS")
print("=" * 50)

# append() - add element at end
lista = [1, 2, 3]
lista.append(4)
print(f"After append(4): {lista}")

# extend() - add multiple elements
lista.extend([5, 6, 7])
print(f"After extend([5,6,7]): {lista}")

# insert() - insert at specific position
lista.insert(0, 0)
print(f"After insert(0, 0): {lista}")

# remove() - remove first occurrence
lista.remove(3)
print(f"After remove(3): {lista}")

# pop() - remove and return element
last = lista.pop()
print(f"After pop(): {lista}, removed: {last}")
first = lista.pop(0)
print(f"After pop(0): {lista}, removed: {first}")

# clear() - empty list
copy = lista.copy()
copy.clear()
print(f"After clear(): {copy}")

# ========================================
# Sorting and Reversing
# ========================================
print("\n" + "=" * 50)
print("SORTING")
print("=" * 50)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

# sort() - in-place sorting
numbers.sort()
print(f"After sort(): {numbers}")

numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# sorted() - new sorted list
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(f"\nOriginal: {original}")
print(f"sorted(): {sorted_list}")

# With key function
words = ["Python", "is", "a", "great", "language"]
by_length = sorted(words, key=len)
print(f"\nSorted by length: {by_length}")

# reverse() - reverse in place
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(f"\nAfter reverse(): {lista}")

# ========================================
# List Comprehensions
# ========================================
print("\n" + "=" * 50)
print("LIST COMPREHENSIONS")
print("=" * 50)

# Simple comprehension
squares = [x**2 for x in range(10)]
print(f"Square numbers: {squares}")

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {evens}")

# With if-else
result = [x if x % 2 == 0 else -x for x in range(10)]
print(f"Even positive, odd negative: {result}")

# Nested comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Multiplication table: {matrix}")

# String processing
words = ["Python", "is", "GREAT"]
lowercase = [w.lower() for w in words]
print(f"Lowercase: {lowercase}")

# ========================================
# List Operations
# ========================================
print("\n" + "=" * 50)
print("LIST OPERATIONS")
print("=" * 50)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"{list1} + {list2} = {combined}")

# Repetition
repeated = list1 * 3
print(f"{list1} * 3 = {repeated}")

# Membership
print(f"2 in {list1}: {2 in list1}")
print(f"10 not in {list1}: {10 not in list1}")

# count() - count occurrences
numbers = [1, 2, 3, 2, 2, 4]
print(f"\n2 appears {numbers.count(2)}x in {numbers}")

# index() - find position
position = numbers.index(2)
print(f"First position of 2: {position}")

# ========================================
# Practical Examples
# ========================================
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Stack (LIFO) with list
stack = []
stack.append("A")  # Push
stack.append("B")
stack.append("C")
print(f"Stack: {stack}")
top = stack.pop()  # Pop
print(f"Removed: {top}, Stack: {stack}")

# Queue (FIFO) - inefficient with list!
from collections import deque
queue = deque(["A", "B", "C"])
queue.append("D")  # Add at back
first = queue.popleft()  # Remove from front
print(f"\nQueue after popleft: {list(queue)}")

# Matrix operations
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"\nTransposed matrix: {transposed}")

# Flatten (2D to 1D)
flat = [element for row in matrix for element in row]
print(f"Flat list: {flat}")

# ========================================
# Copying Lists
# ========================================
print("\n" + "=" * 50)
print("COPYING LISTS")
print("=" * 50)

original = [1, [2, 3], 4]

# Shallow copy
shallow = original.copy()
shallow[0] = 99
shallow[1][0] = 88
print(f"Original after shallow copy: {original}")
print(f"Shallow copy: {shallow}")

# Deep copy
import copy
original = [1, [2, 3], 4]
deep = copy.deepcopy(original)
deep[1][0] = 77
print(f"\nOriginal after deep copy: {original}")
print(f"Deep copy: {deep}")

# ========================================
# Performance Tips
# ========================================
print("\n" + "=" * 50)
print("PERFORMANCE TIPS")
print("=" * 50)

import time

# List comprehension vs. loop
start = time.time()
result1 = []
for i in range(10000):
    result1.append(i**2)
time1 = time.time() - start

start = time.time()
result2 = [i**2 for i in range(10000)]
time2 = time.time() - start

print(f"Loop: {time1:.6f}s")
print(f"Comprehension: {time2:.6f}s")
print(f"Comprehension is {time1/time2:.2f}x faster")

# ========================================
# Advanced Techniques
# ========================================
print("\n" + "=" * 50)
print("ADVANCED TECHNIQUES")
print("=" * 50)

# Filter with comprehension
numbers = range(-5, 6)
positive = [x for x in numbers if x > 0]
print(f"Positive numbers: {positive}")

# Map with comprehension
words = ["python", "java", "javascript"]
uppercase = [w.upper() for w in words]
print(f"Uppercase: {uppercase}")

# Enumerate in comprehension
indexed = [(i, val) for i, val in enumerate(['a', 'b', 'c'])]
print(f"With index: {indexed}")

# Zip in comprehension
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = [(x, y) for x, y in zip(list1, list2)]
print(f"Zipped: {combined}")