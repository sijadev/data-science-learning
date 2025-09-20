# 3.2 Loops - Code Examples

# ========================================
# For Loop
# ========================================
print("=" * 50)
print("FOR LOOP")
print("=" * 50)

# Iterate over list
fruits = ["Apple", "Banana", "Orange"]
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# Iterate over string
word = "Python"
print(f"\nLetters in '{word}':")
for letter in word:
    print(f"  {letter}", end=" ")
print()

# Iterate over dictionary
person = {"name": "Alice", "age": 30, "city": "Berlin"}
print("\nDictionary iteration:")

print("Keys:")
for key in person:
    print(f"  {key}")

print("Values:")
for value in person.values():
    print(f"  {value}")

print("Key-Value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")

# ========================================
# range() Function
# ========================================
print("\n" + "=" * 50)
print("RANGE() FUNCTION")
print("=" * 50)

# range(stop)
print("range(5):", list(range(5)))

# range(start, stop)
print("range(2, 8):", list(range(2, 8)))

# range(start, stop, step)
print("range(0, 10, 2):", list(range(0, 10, 2)))
print("range(10, 0, -1):", list(range(10, 0, -1)))

# With for loop
print("\nSquare numbers:")
for i in range(1, 6):
    print(f"{i}² = {i**2}")

# ========================================
# enumerate() Function
# ========================================
print("\n" + "=" * 50)
print("ENUMERATE() FUNCTION")
print("=" * 50)

fruits = ["Apple", "Banana", "Orange", "Mango"]

# With index
print("With index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# With start index
print("\nWith start index 1:")
for number, fruit in enumerate(fruits, start=1):
    print(f"{number}. {fruit}")

# ========================================
# While Loop
# ========================================
print("\n" + "=" * 50)
print("WHILE LOOP")
print("=" * 50)

# Simple while loop
count = 0
print("Countdown:")
while count < 5:
    print(f"  {count}")
    count += 1

# With condition
print("\nSum up to 100:")
sum_val = 0
number = 1
while sum_val < 100:
    sum_val += number
    number += 1
print(f"Sum: {sum_val}, last number: {number-1}")

# Infinite loop with break
print("\nWith user input (simulated):")
inputs = ["yes", "yes", "no"]  # Simulated inputs
index = 0
while True:
    if index < len(inputs):
        answer = inputs[index]
        print(f"Continue? {answer}")
        if answer.lower() == "no":
            break
        index += 1
    else:
        break
print("Loop ended")

# ========================================
# break and continue
# ========================================
print("\n" + "=" * 50)
print("BREAK AND CONTINUE")
print("=" * 50)

# break - completely exit loop
print("Break example - find first even number:")
numbers = [1, 3, 5, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        print(f"First even number found: {number}")
        break
    print(f"  {number} is odd")

# continue - next iteration
print("\nContinue example - only even numbers:")
for i in range(10):
    if i % 2 != 0:
        continue  # Skip odd numbers
    print(f"  {i}")

# Combined in nested loops
print("\nNested with break:")
for i in range(3):
    print(f"Outer loop: {i}")
    for j in range(3):
        if j == 2:
            break
        print(f"  Inner loop: {j}")

# ========================================
# else in Loops
# ========================================
print("\n" + "=" * 50)
print("ELSE IN LOOPS")
print("=" * 50)

# for-else (executed when no break)
print("Prime check with for-else:")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"  {n} is divisible by {i}")
            break
    else:
        print(f"  {n} is a prime number")
        return True
    return False

for number in [7, 8, 11, 15]:
    print(f"Testing {number}:")
    is_prime(number)

# while-else
print("\nWhile-else example:")
attempts = 3
password = "secret"
inputs = ["wrong", "again", "secret"]  # Simulated
index = 0

while attempts > 0:
    if index < len(inputs):
        input_val = inputs[index]
        print(f"Attempt {4-attempts}: {input_val}")
        if input_val == password:
            print("Access granted!")
            break
        attempts -= 1
        index += 1
    else:
        break
else:
    print("No attempts left - access denied!")

# ========================================
# zip() Function
# ========================================
print("\n" + "=" * 50)
print("ZIP() FUNCTION")
print("=" * 50)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Berlin", "Munich", "Hamburg"]

print("Parallel iteration:")
for name, age, city in zip(names, ages, cities):
    print(f"{name} ({age}) from {city}")

# Different lengths
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30]
print("\nDifferent lengths (stops at shortest):")
for a, b in zip(numbers1, numbers2):
    print(f"{a} + {b} = {a + b}")

# ========================================
# List Comprehensions (Preview)
# ========================================
print("\n" + "=" * 50)
print("LIST COMPREHENSIONS")
print("=" * 50)

# Traditional loop
squares = []
for x in range(5):
    squares.append(x ** 2)
print(f"With loop: {squares}")

# List comprehension
squares = [x ** 2 for x in range(5)]
print(f"With comprehension: {squares}")

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers: {evens}")

# ========================================
# Nested Loops
# ========================================
print("\n" + "=" * 50)
print("NESTED LOOPS")
print("=" * 50)

# Multiplication table
print("Small multiplication table (excerpt):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j:2}", end="  ")
    print()

# Traverse matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nTraverse matrix:")
for row in matrix:
    for element in row:
        print(f"{element:2}", end=" ")
    print()

# ========================================
# Practical Examples
# ========================================
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Fibonacci sequence
def fibonacci(n):
    fib = []
    a, b = 0, 1
    while len(fib) < n:
        fib.append(a)
        a, b = b, a + b
    return fib

print(f"Fibonacci (10): {fibonacci(10)}")

# Count words
text = "Python is great Python is fun Python is powerful"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

print(f"\nWord count:")
for word, count in word_count.items():
    if count > 1:
        print(f"  '{word}': {count}x")

# Draw pyramid
print("\nPyramid:")
height = 5
for i in range(height):
    print(" " * (height - i - 1) + "*" * (2 * i + 1))

# ========================================
# Performance Tips
# ========================================
print("\n" + "=" * 50)
print("PERFORMANCE TIPS")
print("=" * 50)

import time

# Bad: String concatenation in loop
start = time.time()
result = ""
for i in range(1000):
    result += str(i)
time1 = time.time() - start

# Better: Use join
start = time.time()
result = "".join(str(i) for i in range(1000))
time2 = time.time() - start

print(f"String concatenation: {time1:.6f}s")
print(f"Join method: {time2:.6f}s")
print(f"Join is {time1/time2:.1f}x faster")

# ========================================
# Advanced Iteration
# ========================================
print("\n" + "=" * 50)
print("ADVANCED ITERATION")
print("=" * 50)

# reversed() - iterate backwards
print("Backwards:")
for i in reversed(range(5)):
    print(f"  {i}")

# sorted() - iterate sorted
words = ["Zebra", "Ape", "Elephant", "Bear"]
print("\nSorted:")
for word in sorted(words):
    print(f"  {word}")

# itertools (Preview)
import itertools

print("\nItertools cycle (first 10):")
counter = 0
for item in itertools.cycle(['A', 'B', 'C']):
    if counter >= 10:
        break
    print(item, end=" ")
    counter += 1
print()