# 1.2 Basic Syntax - Code Examples

# ========================================
# Python Philosophy and Zen
# ========================================
import this  # Shows "The Zen of Python"

# ========================================
# Comments
# ========================================
# This is a single-line comment

"""
This is a multi-line comment
or docstring. Often used for
documentation.
"""

# ========================================
# Indentation
# ========================================
# Python uses indentation instead of braces
if True:
    print("This line is indented (4 spaces)")
    if True:
        print("This line is double indented")
    print("Back to first indentation level")
print("No indentation - outside the if block")

# ========================================
# Variables and Assignments
# ========================================
# No type declaration needed
name = "Python"
age = 30
pi = 3.14159

# Multiple assignment
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Same value for multiple variables
a = b = c = 100
print(f"a={a}, b={b}, c={c}")

# ========================================
# Python Keywords
# ========================================
import keyword
print("\nPython Keywords:")
print(keyword.kwlist)

# ========================================
# Naming Conventions (PEP 8)
# ========================================
# snake_case for variables and functions
my_variable = "Snake Case"
def my_function():
    pass

# UPPER_CASE for constants
MAX_SIZE = 100
PI_VALUE = 3.14159

# PascalCase for classes
class MyClass:
    pass

# ========================================
# Code Structure
# ========================================
def example_function(parameter1, parameter2):
    """
    Docstring: Function description
    Args:
        parameter1: Description
        parameter2: Description
    Returns:
        Description of return value
    """
    # Function body
    result = parameter1 + parameter2
    return result

# ========================================
# Print and Formatting
# ========================================
print("Simple print")
print("Line 1", "Line 2", sep=" | ")  # Separator
print("With line break", end="\n\n")   # End character

# String formatting
name = "Python"
version = 3.12
print("Classic: %s Version %.2f" % (name, version))
print("Format: {} Version {:.2f}".format(name, version))
print(f"F-String: {name} Version {version:.2f}")  # Recommended!

# ========================================
# User Input
# ========================================
# name_input = input("What's your name? ")
# print(f"Hello {name_input}!")

# ========================================
# Line Continuation
# ========================================
# With backslash
long_calculation = 1 + 2 + 3 + \
                  4 + 5 + 6

# Implicit with parentheses
long_list = [
    "Element 1",
    "Element 2",
    "Element 3"
]

# ========================================
# Pass Statement
# ========================================
# Placeholder for empty code block
def not_implemented_yet():
    pass  # TODO: Implement later

# ========================================
# Assertions
# ========================================
x = 10
assert x > 0, "x must be positive"
# assert x < 0, "This would raise an AssertionError"

# ========================================
# Best Practices Demo
# ========================================
def calculate_area(width, height):
    """Calculates the area of a rectangle."""
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive")

    area = width * height
    return area

# Usage
try:
    result = calculate_area(5, 10)
    print(f"Area: {result}")
except ValueError as e:
    print(f"Error: {e}")

# ========================================
# REPL (Read-Eval-Print-Loop) Examples
# ========================================
print("\n📝 REPL commands to try:")
print(">>> 2 + 2")
print(">>> type(42)")
print(">>> help(print)")
print(">>> dir(str)")
print(">>> import math; math.pi")