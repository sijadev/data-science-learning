# 2.2 Variables and Operators - Code Examples

# ========================================
# Variable Assignment
# ========================================
print("=" * 50)
print("VARIABLE ASSIGNMENT")
print("=" * 50)

# Simple assignment
name = "Python"
age = 30
pi = 3.14159
is_active = True

print(f"name = {name}")
print(f"age = {age}")
print(f"pi = {pi}")
print(f"is_active = {is_active}")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"\nx, y, z = 1, 2, 3")
print(f"x={x}, y={y}, z={z}")

# Same values
a = b = c = 100
print(f"\na = b = c = 100")
print(f"a={a}, b={b}, c={c}")

# Tuple unpacking
coordinates = (10, 20)
x, y = coordinates
print(f"\nTuple unpacking: x={x}, y={y}")

# Variable swapping
x, y = y, x
print(f"After swap: x={x}, y={y}")

# ========================================
# Arithmetic Operators
# ========================================
print("\n" + "=" * 50)
print("ARITHMETIC OPERATORS")
print("=" * 50)

a, b = 10, 3
print(f"a = {a}, b = {b}")
print("-" * 30)

print(f"Addition:       a + b = {a + b}")
print(f"Subtraction:    a - b = {a - b}")
print(f"Multiplication: a * b = {a * b}")
print(f"Division:       a / b = {a / b:.2f}")
print(f"Floor division: a // b = {a // b}")
print(f"Modulo:         a % b = {a % b}")
print(f"Exponentiation: a ** b = {a ** b}")
print(f"Negative:       -a = {-a}")
print(f"Positive:       +a = {+a}")

# Complex expressions
result = (a + b) * 2 - a ** 2 / b
print(f"\n(a + b) * 2 - a² / b = {result:.2f}")

# With different types
print("\nWith different types:")
print(f"10 + 3.5 = {10 + 3.5}")
print(f"'Py' + 'thon' = {'Py' + 'thon'}")
print(f"'Ha' * 3 = {'Ha' * 3}")
print(f"[1, 2] + [3, 4] = {[1, 2] + [3, 4]}")

# ========================================
# Comparison Operators
# ========================================
print("\n" + "=" * 50)
print("COMPARISON OPERATORS")
print("=" * 50)

x, y = 5, 10
print(f"x = {x}, y = {y}")
print("-" * 30)

print(f"Equal:           x == y  → {x == y}")
print(f"Not equal:       x != y  → {x != y}")
print(f"Greater:         x > y   → {x > y}")
print(f"Less:            x < y   → {x < y}")
print(f"Greater equal:   x >= y  → {x >= y}")
print(f"Less equal:      x <= y  → {x <= y}")

# String comparisons
print("\nString comparisons (lexicographic):")
print(f"'apple' < 'banana' → {'apple' < 'banana'}")
print(f"'Python' == 'python' → {'Python' == 'python'}")
print(f"'10' < '2' → {'10' < '2'}  (String comparison!)")

# Chained comparisons
a, b, c = 5, 10, 15
print(f"\nChained comparisons:")
print(f"a < b < c → {a < b < c}")
print(f"a < b > 0 → {a < b > 0}")

# ========================================
# Logical Operators
# ========================================
print("\n" + "=" * 50)
print("LOGICAL OPERATORS")
print("=" * 50)

a, b = True, False
print(f"a = {a}, b = {b}")
print("-" * 30)

print(f"a and b  → {a and b}")
print(f"a or b   → {a or b}")
print(f"not a    → {not a}")
print(f"not b    → {not b}")

# With numbers
x, y = 5, 0
print(f"\nWith numbers (x={x}, y={y}):")
print(f"x and y  → {x and y}")
print(f"x or y   → {x or y}")
print(f"not x    → {not x}")
print(f"not y    → {not y}")

# Short-circuit evaluation
print("\nShort-circuit evaluation:")
print(f"False and (10/0) → False (division not executed)")
print(f"True or (10/0) → True (division not executed)")

# Practical example
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"\nCan drive (age={age}, has_license={has_license}): {can_drive}")

# ========================================
# Bitwise Operators
# ========================================
print("\n" + "=" * 50)
print("BITWISE OPERATORS")
print("=" * 50)

a, b = 12, 5  # 12 = 1100, 5 = 0101 in binary
print(f"a = {a} (0b{a:04b}), b = {b} (0b{b:04b})")
print("-" * 30)

print(f"AND:    a & b  = {a & b:2} (0b{a & b:04b})")
print(f"OR:     a | b  = {a | b:2} (0b{a | b:04b})")
print(f"XOR:    a ^ b  = {a ^ b:2} (0b{a ^ b:04b})")
print(f"NOT:    ~a     = {~a:2} (Two's complement)")
print(f"Left:   a << 1 = {a << 1:2} (0b{a << 1:04b})")
print(f"Right:  a >> 1 = {a >> 1:2} (0b{a >> 1:04b})")

# Practical application
flags = 0b0000
FLAG_READ = 0b0001
FLAG_WRITE = 0b0010
FLAG_EXECUTE = 0b0100

# Set flags
flags = flags | FLAG_READ | FLAG_WRITE
print(f"\nFlags after setting: 0b{flags:04b}")

# Check flag
has_read = bool(flags & FLAG_READ)
has_execute = bool(flags & FLAG_EXECUTE)
print(f"Has read permission: {has_read}")
print(f"Has execute permission: {has_execute}")

# ========================================
# Assignment Operators
# ========================================
print("\n" + "=" * 50)
print("ASSIGNMENT OPERATORS")
print("=" * 50)

x = 10
print(f"Start: x = {x}")

x += 5
print(f"x += 5  → x = {x}")

x -= 3
print(f"x -= 3  → x = {x}")

x *= 2
print(f"x *= 2  → x = {x}")

x //= 4
print(f"x //= 4 → x = {x}")

x %= 5
print(f"x %= 5  → x = {x}")

x **= 2
print(f"x **= 2 → x = {x}")

# With strings
text = "Py"
text += "thon"
print(f"\nString: 'Py' += 'thon' → '{text}'")

# With lists
lista = [1, 2]
lista += [3, 4]
print(f"List: [1, 2] += [3, 4] → {lista}")

# ========================================
# Identity and Membership Operators
# ========================================
print("\n" + "=" * 50)
print("IDENTITY AND MEMBERSHIP")
print("=" * 50)

# Identity operators (is, is not)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("Identity (is):")
print(f"a = {a}")
print(f"b = {b} (same content)")
print(f"c = a (same reference)")
print(f"a == b  → {a == b}  (same value)")
print(f"a is b  → {a is b}  (not same objects)")
print(f"a is c  → {a is c}  (same objects)")

# None comparison
x = None
print(f"\nx is None → {x is None}  (Best practice)")
print(f"x == None → {x == None}  (Works, but not recommended)")

# Membership operators (in, not in)
print("\nMembership (in):")
text = "Python Programming"
print(f"Text: '{text}'")
print(f"'Python' in text     → {'Python' in text}")
print(f"'Java' not in text   → {'Java' not in text}")

numbers = [1, 2, 3, 4, 5]
print(f"\nList: {numbers}")
print(f"3 in numbers         → {3 in numbers}")
print(f"10 not in numbers    → {10 not in numbers}")

# ========================================
# Operator Precedence
# ========================================
print("\n" + "=" * 50)
print("OPERATOR PRECEDENCE")
print("=" * 50)

print("Order (highest first):")
print("1. () Parentheses")
print("2. ** Exponentiation")
print("3. +x, -x, ~x Unary operators")
print("4. *, /, //, % Multiplication, Division")
print("5. +, - Addition, Subtraction")
print("6. <<, >> Bit shifts")
print("7. & Bitwise AND")
print("8. ^ Bitwise XOR")
print("9. | Bitwise OR")
print("10. ==, !=, <, <=, >, >= Comparisons")
print("11. is, is not, in, not in")
print("12. not Logical NOT")
print("13. and Logical AND")
print("14. or Logical OR")

# Examples
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
print(f"\n2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")

result3 = True or False and False
result4 = (True or False) and False
print(f"\nTrue or False and False = {result3}")
print(f"(True or False) and False = {result4}")

# ========================================
# Walrus Operator := (Python 3.8+)
# ========================================
print("\n" + "=" * 50)
print("WALRUS OPERATOR :=")
print("=" * 50)

# Assignment in expressions
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List has {n} elements (more than 3)")

# Useful in while loops
data = [1, 2, 3, 0, 4, 5]
print(f"\nData: {data}")
print("Process until 0 is found:")
i = 0
while i < len(data) and (value := data[i]) != 0:
    print(f"  Processing: {value}")
    i += 1