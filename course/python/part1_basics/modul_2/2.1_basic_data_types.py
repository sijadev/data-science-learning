# 2.1 Basic Data Types - Code Examples

# ========================================
# Integer (Whole Numbers)
# ========================================
print("=" * 50)
print("INTEGER")
print("=" * 50)

# Decimal
age = 25
year = 2024
negative = -42

# Other number systems
binary = 0b1010      # Binary (10 in decimal)
octal = 0o12         # Octal (10 in decimal)
hexadecimal = 0xA    # Hexadecimal (10 in decimal)

print(f"Decimal: {age}")
print(f"Binary 0b1010: {binary}")
print(f"Octal 0o12: {octal}")
print(f"Hex 0xA: {hexadecimal}")

# Large numbers with underscores (for better readability)
million = 1_000_000
print(f"One million: {million:,}")

# ========================================
# Float (Floating Point Numbers)
# ========================================
print("\n" + "=" * 50)
print("FLOAT")
print("=" * 50)

pi = 3.14159
temperature = -17.5
scientific = 2.5e-3  # Scientific notation (0.0025)

print(f"Pi: {pi}")
print(f"Temperature: {temperature}°C")
print(f"Scientific 2.5e-3: {scientific}")

# Float precision
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # Warning: Floating-Point Arithmetic!
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")

# Infinity and NaN
import math
infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan')

print(f"Infinity: {infinity}")
print(f"Is infinite? {math.isinf(infinity)}")
print(f"Is NaN? {math.isnan(not_a_number)}")

# ========================================
# Complex (Complex Numbers)
# ========================================
print("\n" + "=" * 50)
print("COMPLEX")
print("=" * 50)

z1 = 3 + 4j
z2 = complex(2, -1)

print(f"Complex number z1: {z1}")
print(f"Real part: {z1.real}, Imaginary part: {z1.imag}")
print(f"Conjugate: {z1.conjugate()}")
print(f"Magnitude: {abs(z1)}")

# ========================================
# String (Text Strings)
# ========================================
print("\n" + "=" * 50)
print("STRING")
print("=" * 50)

# String creation
single_quote = 'Hello'
double_quote = "World"
triple_quote = """Multi-line
string"""
raw_string = r"Raw String: \n is not interpreted"

print(f"Single Quote: {single_quote}")
print(f"Double Quote: {double_quote}")
print(f"Triple Quote: {triple_quote}")
print(f"Raw String: {raw_string}")

# String operations
name = "Python"
print(f"\nString '{name}':")
print(f"Length: {len(name)}")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")
print(f"First character: {name[0]}")
print(f"Last character: {name[-1]}")
print(f"Slice [1:4]: {name[1:4]}")

# String methods
text = "  Python Programming  "
print(f"\nOriginal: '{text}'")
print(f"Strip: '{text.strip()}'")
print(f"Replace: '{text.replace('Python', 'Java')}'")
print(f"Split: {text.split()}")
print(f"Contains 'Python': {'Python' in text}")

# String formatting
age = 25
height = 1.75
formatted = f"I am {age} years old and {height:.2f}m tall"
print(f"F-String: {formatted}")

# Escape sequences
escaped = "Line 1\nLine 2\tTab\r\nWindows line"
print(f"\nEscape sequences:\n{escaped}")

# ========================================
# Boolean (Truth Values)
# ========================================
print("\n" + "=" * 50)
print("BOOLEAN")
print("=" * 50)

is_active = True
is_deleted = False

print(f"is_active: {is_active}")
print(f"is_deleted: {is_deleted}")

# Boolean from comparisons
x, y = 10, 20
print(f"\n{x} > {y}: {x > y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")

# Truthy and Falsy values
print("\nFalsy values:")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')}")
print(f"bool([]): {bool([])}")
print(f"bool(None): {bool(None)}")

print("\nTruthy values:")
print(f"bool(1): {bool(1)}")
print(f"bool('Text'): {bool('Text')}")
print(f"bool([1, 2]): {bool([1, 2])}")

# ========================================
# None (Null Value)
# ========================================
print("\n" + "=" * 50)
print("NONE")
print("=" * 50)

result = None
print(f"result: {result}")
print(f"result is None: {result is None}")
print(f"type(None): {type(None)}")

# None as default value
def greet(name=None):
    if name is None:
        return "Hello, stranger!"
    return f"Hello, {name}!"

print(greet())
print(greet("Python"))

# ========================================
# Type Casting (Type Conversion)
# ========================================
print("\n" + "=" * 50)
print("TYPE CASTING")
print("=" * 50)

# String to number
str_number = "42"
int_number = int(str_number)
float_number = float(str_number)

print(f"String '{str_number}' to Int: {int_number}")
print(f"String '{str_number}' to Float: {float_number}")

# Number to string
number = 123
str_from_number = str(number)
print(f"Number {number} to String: '{str_from_number}'")

# Float to Int (truncation)
pi = 3.14159
int_pi = int(pi)
print(f"Float {pi} to Int: {int_pi}")

# Bool conversions
print(f"\nint(True): {int(True)}")
print(f"int(False): {int(False)}")
print(f"str(True): '{str(True)}'")

# Error handling with casting
try:
    invalid = int("abc")
except ValueError as e:
    print(f"\nCasting error: {e}")

# ========================================
# Type Checking
# ========================================
print("\n" + "=" * 50)
print("TYPE CHECKING")
print("=" * 50)

examples = [42, 3.14, "Text", True, None, [1, 2], {'a': 1}]

for value in examples:
    print(f"{str(value):10} -> {type(value).__name__:10} | isinstance(int): {isinstance(value, int)}")

# Multiple type check
number = 42
print(f"\n{number} is int or float: {isinstance(number, (int, float))}")

# ========================================
# Dynamic Typing
# ========================================
print("\n" + "=" * 50)
print("DYNAMIC TYPING")
print("=" * 50)

# Variable can change type
variable = 42
print(f"variable = 42, Type: {type(variable)}")

variable = "Now a string"
print(f"variable = 'Now a string', Type: {type(variable)}")

variable = [1, 2, 3]
print(f"variable = [1, 2, 3], Type: {type(variable)}")