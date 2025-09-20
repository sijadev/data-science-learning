# 5.1 Function Definition - Code Examples

# ========================================
# Simple Functions
# ========================================
print("=" * 50)
print("SIMPLE FUNCTIONS")
print("=" * 50)

# Function without parameters and return
def greet():
    print("Hello World!")

greet()

# Function with parameter
def greet_person(name):
    print(f"Hello {name}!")

greet_person("Alice")

# Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Function with multiple parameters and return
def calculate_rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter  # Returns tuple

area, perimeter = calculate_rectangle(5, 3)
print(f"Rectangle: Area={area}, Perimeter={perimeter}")

# ========================================
# Parameters and Arguments
# ========================================
print("\n" + "=" * 50)
print("PARAMETERS AND ARGUMENTS")
print("=" * 50)

# Positional parameters
def divide(dividend, divisor):
    if divisor == 0:
        return "Division by zero not possible"
    return dividend / divisor

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")

# Keyword arguments
def create_user(name, age, city):
    return f"User: {name}, {age} years, from {city}"

# Different call methods
user1 = create_user("Alice", 30, "Berlin")
user2 = create_user(age=25, name="Bob", city="Munich")
user3 = create_user("Charlie", city="Hamburg", age=35)

print(user1)
print(user2)
print(user3)

# ========================================
# Default Parameters
# ========================================
print("\n" + "=" * 50)
print("DEFAULT PARAMETERS")
print("=" * 50)

def greet_with_title(name, title="Mr./Ms."):
    return f"Good day, {title} {name}!"

print(greet_with_title("Schmidt"))
print(greet_with_title("Mueller", "Dr."))
print(greet_with_title("Weber", title="Prof."))

# Multiple default parameters
def configure_server(host="localhost", port=8000, debug=False):
    config = {
        "host": host,
        "port": port,
        "debug": debug
    }
    return config

print("\nServer configurations:")
print(configure_server())  # All defaults
print(configure_server("192.168.1.1"))  # Only host changed
print(configure_server(port=9000, debug=True))  # port and debug changed

# ========================================
# Variable Parameters (*args)
# ========================================
print("\n" + "=" * 50)
print("VARIABLE PARAMETERS (*args)")
print("=" * 50)

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 1 to 10: {sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")
print(f"Sum without arguments: {sum_all()}")

# Combined with normal parameters
def describe_person(name, *hobbies):
    if hobbies:
        hobby_list = ", ".join(hobbies)
        return f"{name} likes: {hobby_list}"
    else:
        return f"{name} has no specified hobbies"

print(f"\n{describe_person('Alice')}")
print(f"{describe_person('Bob', 'Reading')}")
print(f"{describe_person('Charlie', 'Reading', 'Sports', 'Music')}")

# ========================================
# Keyword Parameters (**kwargs)
# ========================================
print("\n" + "=" * 50)
print("KEYWORD PARAMETERS (**kwargs)")
print("=" * 50)

def create_profile(**info):
    profile = "Profile:\n"
    for key, value in info.items():
        profile += f"  {key}: {value}\n"
    return profile

print(create_profile(name="Alice", age=30, city="Berlin"))
print(create_profile(name="Bob", job="Developer", experience="5 years"))

# Combination of *args and **kwargs
def flexible_function(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print("Flexible call:")
flexible_function(1, 2, 3, name="Alice", age=30)

# ========================================
# Docstrings
# ========================================
print("\n" + "=" * 50)
print("DOCSTRINGS")
print("=" * 50)

def calculate_bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI).

    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters

    Returns:
        float: BMI value

    Example:
        >>> calculate_bmi(70, 1.75)
        22.857142857142858
    """
    return weight / (height ** 2)

bmi = calculate_bmi(70, 1.75)
print(f"BMI: {bmi:.2f}")

# Show docstring
print(f"\nDocstring:\n{calculate_bmi.__doc__}")

# With help() function
# help(calculate_bmi)  # Would show detailed help

# ========================================
# Return Values
# ========================================
print("\n" + "=" * 50)
print("RETURN VALUES")
print("=" * 50)

# No explicit return (returns None)
def print_message(message):
    print(f"Message: {message}")

result = print_message("Hello")
print(f"Return value: {result}")

# Early return
def check_age(age):
    if age < 0:
        return "Invalid age"
    if age < 18:
        return "Minor"
    if age < 65:
        return "Adult"
    return "Senior"

ages = [5, 16, 25, 70, -5]
for age in ages:
    print(f"Age {age}: {check_age(age)}")

# Multiple return values
def analyze_text(text):
    words = text.split()
    return len(text), len(words), text.upper(), text.lower()

text = "Python is great"
char_count, word_count, upper, lower = analyze_text(text)
print(f"\nText analysis of '{text}':")
print(f"Characters: {char_count}, Words: {word_count}")
print(f"Upper: {upper}")
print(f"Lower: {lower}")

# ========================================
# Functions as First-Class Objects
# ========================================
print("\n" + "=" * 50)
print("FUNCTIONS AS OBJECTS")
print("=" * 50)

# Functions can be assigned to variables
def square(x):
    return x * x

my_function = square
print(f"square(5) = {square(5)}")
print(f"my_function(5) = {my_function(5)}")

# Functions can be passed as parameters
def apply_operation(numbers, operation):
    return [operation(num) for num in numbers]

numbers = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, square)
print(f"\nNumbers: {numbers}")
print(f"Squared: {squared}")

# Functions can be stored in lists
def cube(x):
    return x ** 3

def double(x):
    return x * 2

operations = [square, cube, double]
x = 3
for op in operations:
    print(f"{op.__name__}({x}) = {op(x)}")

# ========================================
# Nested Functions
# ========================================
print("\n" + "=" * 50)
print("NESTED FUNCTIONS")
print("=" * 50)

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Create closure
add_5 = outer_function(5)
print(f"add_5(3) = {add_5(3)}")

# Factory pattern
def create_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(f"\ndouble(4) = {double(4)}")
print(f"triple(4) = {triple(4)}")

# ========================================
# Recursion
# ========================================
print("\n" + "=" * 50)
print("RECURSION")
print("=" * 50)

def factorial(n):
    """Calculates factorial of n recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

for i in range(6):
    print(f"{i}! = {factorial(i)}")

# Fibonacci recursive
def fibonacci(n):
    """Calculates the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\nFibonacci sequence:")
for i in range(10):
    print(f"fib({i}) = {fibonacci(i)}")

# ========================================
# Lambda Functions (Preview)
# ========================================
print("\n" + "=" * 50)
print("LAMBDA FUNCTIONS")
print("=" * 50)

# Simple lambda
square_lambda = lambda x: x ** 2
print(f"Lambda square(4) = {square_lambda(4)}")

# Lambda with multiple parameters
add_lambda = lambda x, y: x + y
print(f"Lambda add(3, 5) = {add_lambda(3, 5)}")

# Lambda in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"\nOriginal: {numbers}")
print(f"Squared: {squared}")
print(f"Evens: {evens}")

# ========================================
# Type Hints (Modern Python)
# ========================================
print("\n" + "=" * 50)
print("TYPE HINTS")
print("=" * 50)

def add_with_types(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b

def greet_typed(name: str, age: int = 0) -> str:
    """Greets a person with optional age."""
    if age > 0:
        return f"Hello {name}, you are {age} years old!"
    return f"Hello {name}!"

print(add_with_types(5, 3))
print(greet_typed("Alice"))
print(greet_typed("Bob", 30))

# Complex type hints
from typing import List, Dict, Optional

def process_names(names: List[str]) -> Dict[str, int]:
    """Creates a dictionary with names and their lengths."""
    return {name: len(name) for name in names}

def find_user(user_id: int) -> Optional[str]:
    """Finds a user or returns None."""
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id)

names = ["Alice", "Bob", "Charlie"]
name_lengths = process_names(names)
print(f"\nName lengths: {name_lengths}")

user = find_user(2)
print(f"User 2: {user}")
user = find_user(99)
print(f"User 99: {user}")