# 4.4 Sets - Code Examples

# ========================================
# Creating Sets
# ========================================
print("=" * 50)
print("CREATING SETS")
print("=" * 50)

# Different ways to create sets
empty = set()  # Not {} - that would be an empty dictionary!
numbers = {1, 2, 3, 4, 5}
letters = {'a', 'b', 'c'}
mixed = {1, "Text", 3.14, (1, 2)}  # Only immutable types!

print(f"Empty set: {empty}")
print(f"Numbers: {numbers}")
print(f"Letters: {letters}")
print(f"Mixed: {mixed}")

# With set() constructor
from_list = set([1, 2, 3, 2, 1])  # Duplicates are removed
from_string = set("Python")
from_range = set(range(5))

print(f"\nFrom list (with duplicates): {from_list}")
print(f"From string: {from_string}")
print(f"From range: {from_range}")

# Set comprehension
squares = {x**2 for x in range(-3, 4)}
print(f"\nSquare numbers: {squares}")

# ========================================
# Set Properties
# ========================================
print("\n" + "=" * 50)
print("SET PROPERTIES")
print("=" * 50)

# No duplicates
with_duplicates = [1, 2, 2, 3, 3, 3, 4]
without_duplicates = set(with_duplicates)
print(f"List: {with_duplicates}")
print(f"Set: {without_duplicates}")

# No order (unordered)
s1 = {3, 1, 2}
s2 = {1, 2, 3}
print(f"\n{s1} == {s2}: {s1 == s2}")  # True, order doesn't matter

# Only hashable (immutable) elements
try:
    invalid = {[1, 2], [3, 4]}  # Lists are not hashable
except TypeError as e:
    print(f"\nError with lists: {e}")

# ========================================
# Set Methods
# ========================================
print("\n" + "=" * 50)
print("SET METHODS")
print("=" * 50)

s = {1, 2, 3}
print(f"Start set: {s}")

# add() - add one element
s.add(4)
print(f"After add(4): {s}")
s.add(2)  # No effect, 2 already exists
print(f"After add(2): {s}")

# update() - add multiple elements
s.update([5, 6, 7])
print(f"After update([5,6,7]): {s}")

# remove() - remove element (error if not present)
s.remove(3)
print(f"After remove(3): {s}")

# discard() - remove element (no error if not present)
s.discard(10)  # No error
print(f"After discard(10): {s}")

# pop() - remove random element
element = s.pop()
print(f"After pop(): {s}, removed: {element}")

# clear() - remove all elements
copy = s.copy()
copy.clear()
print(f"After clear(): {copy}")

# ========================================
# Set Operations
# ========================================
print("\n" + "=" * 50)
print("SET OPERATIONS")
print("=" * 50)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"Set A: {a}")
print(f"Set B: {b}")

# Union
union = a | b  # or a.union(b)
print(f"\nA ∪ B: {union}")

# Intersection
intersection = a & b  # or a.intersection(b)
print(f"A ∩ B: {intersection}")

# Difference
diff_a = a - b  # or a.difference(b)
diff_b = b - a
print(f"A - B: {diff_a}")
print(f"B - A: {diff_b}")

# Symmetric difference
sym_diff = a ^ b  # or a.symmetric_difference(b)
print(f"A △ B: {sym_diff}")

# ========================================
# Set Comparisons
# ========================================
print("\n" + "=" * 50)
print("SET COMPARISONS")
print("=" * 50)

s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
s3 = {2, 3}
s4 = {6, 7, 8}

# Subset
print(f"{s1} ⊆ {s2}: {s1.issubset(s2)}")  # True
print(f"{s1} ⊆ {s3}: {s1.issubset(s3)}")  # False

# Superset
print(f"\n{s2} ⊇ {s1}: {s2.issuperset(s1)}")  # True
print(f"{s1} ⊇ {s3}: {s1.issuperset(s3)}")  # True

# Disjoint (no common elements)
print(f"\n{s1} disjoint {s4}: {s1.isdisjoint(s4)}")  # True
print(f"{s1} disjoint {s3}: {s1.isdisjoint(s3)}")  # False

# ========================================
# Frozen Sets
# ========================================
print("\n" + "=" * 50)
print("FROZEN SETS")
print("=" * 50)

# Immutable set
fs = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {fs}")

# Cannot be modified
try:
    fs.add(6)
except AttributeError as e:
    print(f"Error with add(): {e}")

# Can be used as dictionary key
set_dict = {
    frozenset([1, 2]): "Set A",
    frozenset([3, 4]): "Set B"
}
print(f"\nDictionary with frozen sets: {set_dict}")

# Can be contained in other sets
set_of_sets = {
    frozenset([1, 2]),
    frozenset([3, 4]),
    frozenset([5, 6])
}
print(f"Set of sets: {set_of_sets}")

# ========================================
# Practical Examples
# ========================================
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Remove duplicates
names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "David"]
unique = list(set(names))
print(f"Original: {names}")
print(f"Without duplicates: {unique}")

# Find common elements
python_users = {"Alice", "Bob", "Charlie", "David"}
java_users = {"Bob", "David", "Eve", "Frank"}
both = python_users & java_users
print(f"\nPython AND Java: {both}")

# Find differences
only_python = python_users - java_users
only_java = java_users - python_users
print(f"Only Python: {only_python}")
print(f"Only Java: {only_java}")

# Membership testing (fast!)
large_list = list(range(100000))
large_set = set(range(100000))

import time

# Search in list
start = time.time()
_ = 99999 in large_list
list_time = time.time() - start

# Search in set
start = time.time()
_ = 99999 in large_set
set_time = time.time() - start

print(f"\nSearch in list: {list_time:.6f}s")
print(f"Search in set: {set_time:.6f}s")
print(f"Set is {list_time/set_time:.0f}x faster")

# ========================================
# Set Updates (In-Place Operations)
# ========================================
print("\n" + "=" * 50)
print("SET UPDATES (IN-PLACE)")
print("=" * 50)

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(f"Original s1: {s1}")

# update() - union in-place
s1_copy = s1.copy()
s1_copy.update(s2)
print(f"After update(): {s1_copy}")

# intersection_update() - intersection in-place
s1_copy = s1.copy()
s1_copy.intersection_update(s2)
print(f"After intersection_update(): {s1_copy}")

# difference_update() - difference in-place
s1_copy = s1.copy()
s1_copy.difference_update(s2)
print(f"After difference_update(): {s1_copy}")

# symmetric_difference_update() - symmetric difference in-place
s1_copy = s1.copy()
s1_copy.symmetric_difference_update(s2)
print(f"After symmetric_difference_update(): {s1_copy}")

# ========================================
# Advanced Examples
# ========================================
print("\n" + "=" * 50)
print("ADVANCED EXAMPLES")
print("=" * 50)

# Prime numbers with set
def sieve_of_eratosthenes(n):
    """Find all prime numbers up to n"""
    numbers = set(range(2, n + 1))
    primes = set()

    while numbers:
        prime = min(numbers)
        primes.add(prime)
        numbers -= set(range(prime, n + 1, prime))

    return primes

primes = sieve_of_eratosthenes(30)
print(f"Primes up to 30: {sorted(primes)}")

# Compare words
text1 = "Python is a great programming language"
text2 = "Java is also a programming language"

words1 = set(text1.lower().split())
words2 = set(text2.lower().split())

common = words1 & words2
only_text1 = words1 - words2
only_text2 = words2 - words1

print(f"\nCommon words: {common}")
print(f"Only in text 1: {only_text1}")
print(f"Only in text 2: {only_text2}")

# ========================================
# Set Comprehensions with Conditions
# ========================================
print("\n" + "=" * 50)
print("SET COMPREHENSIONS")
print("=" * 50)

# Even square numbers
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even square numbers: {even_squares}")

# Letters from string (without duplicates)
text = "Hello World"
letters = {char.lower() for char in text if char.isalpha()}
print(f"Letters from '{text}': {letters}")

# Combinations
a = {1, 2, 3}
b = {'a', 'b'}
combinations = {(x, y) for x in a for y in b}
print(f"Combinations: {combinations}")