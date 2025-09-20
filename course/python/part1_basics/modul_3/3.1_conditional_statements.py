# 3.1 Conditional Statements - Code Examples

# ========================================
# If-Statement
# ========================================
print("=" * 50)
print("IF-STATEMENT")
print("=" * 50)

# Simple if
age = 18
if age >= 18:
    print("You are of legal age")

# if-else
temperature = 25
if temperature > 30:
    print("It's hot")
else:
    print("It's pleasant")

# if-elif-else
grade = 85
if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# ========================================
# Nested Conditions
# ========================================
print("\n" + "=" * 50)
print("NESTED CONDITIONS")
print("=" * 50)

age = 25
has_license = True
sober = True

if age >= 18:
    if has_license:
        if sober:
            print("You may drive")
        else:
            print("You may not drive - not sober!")
    else:
        print("You may not drive - no license!")
else:
    print("You may not drive - too young!")

# Better with logical operators
if age >= 18 and has_license and sober:
    print("\nAlternative: You may drive")
else:
    print("\nAlternative: You may not drive")

# ========================================
# Ternary Operator (Conditional Expression)
# ========================================
print("\n" + "=" * 50)
print("TERNARY OPERATOR")
print("=" * 50)

# Syntax: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# With calculation
x = 10
y = 20
maximum = x if x > y else y
print(f"Maximum of {x} and {y}: {maximum}")

# Nested (not recommended - hard to read!)
grade = 75
evaluation = "good" if grade >= 80 else ("satisfactory" if grade >= 60 else "insufficient")
print(f"Evaluation: {evaluation}")

# ========================================
# Match-Case (Python 3.10+)
# ========================================
print("\n" + "=" * 50)
print("MATCH-CASE (Pattern Matching)")
print("=" * 50)

# Simple match
day = "Monday"
match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Almost weekend!")
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:
        print("Regular weekday")

# With values
def http_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

print(f"\nHTTP 200: {http_status(200)}")
print(f"HTTP 404: {http_status(404)}")

# With patterns and guards
def categorize_number(x):
    match x:
        case 0:
            return "Zero"
        case n if n > 0:
            return "Positive"
        case n if n < 0:
            return "Negative"

print(f"\nCategorize 42: {categorize_number(42)}")
print(f"Categorize -5: {categorize_number(-5)}")
print(f"Categorize 0: {categorize_number(0)}")

# With structures
def process_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"On Y-axis at y={y}"
        case (x, 0):
            return f"On X-axis at x={x}"
        case (x, y):
            return f"Point at ({x}, {y})"

print(f"\n(0, 0): {process_point((0, 0))}")
print(f"(0, 5): {process_point((0, 5))}")
print(f"(3, 4): {process_point((3, 4))}")

# With classes/types
def process_data(data):
    match data:
        case str(s):
            return f"String with {len(s)} characters"
        case int(n) if n > 0:
            return f"Positive number: {n}"
        case list(l):
            return f"List with {len(l)} elements"
        case dict(d):
            return f"Dictionary with {len(d)} keys"
        case _:
            return "Unknown type"

print(f"\n'Hello': {process_data('Hello')}")
print(f"42: {process_data(42)}")
print(f"[1,2,3]: {process_data([1,2,3])}")
print(f"dict: {process_data({'a': 1})}")

# ========================================
# Truthy and Falsy in Conditions
# ========================================
print("\n" + "=" * 50)
print("TRUTHY AND FALSY")
print("=" * 50)

# Falsy values
falsy_values = [0, 0.0, "", [], (), {}, None, False]
for value in falsy_values:
    if not value:
        print(f"{repr(value):10} is Falsy")

# Truthy values
print("\nTruthy examples:")
if 42:
    print("42 is Truthy")
if "Text":
    print("'Text' is Truthy")
if [1, 2, 3]:
    print("[1, 2, 3] is Truthy")

# ========================================
# Practical Examples
# ========================================
print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# User authentication
def login(username, password):
    users = {"admin": "secret123", "user": "pass456"}

    if not username or not password:
        return "Please enter username and password"

    if username not in users:
        return "User not found"

    if users[username] != password:
        return "Wrong password"

    return f"Welcome {username}!"

print(login("admin", "secret123"))
print(login("admin", "wrong"))
print(login("", ""))

# Leap year check
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

years = [1900, 2000, 2020, 2021, 2024]
print("\nLeap year test:")
for year in years:
    print(f"{year}: {'Leap year' if is_leap_year(year) else 'Not a leap year'}")

# Discount calculation
def calculate_discount(amount, customer_type):
    if customer_type == "premium":
        if amount > 100:
            return amount * 0.8  # 20% discount
        else:
            return amount * 0.9  # 10% discount
    elif customer_type == "regular":
        if amount > 200:
            return amount * 0.95  # 5% discount
        else:
            return amount
    else:
        return amount

print("\nDiscount calculation:")
print(f"Premium, 150€: {calculate_discount(150, 'premium'):.2f}€")
print(f"Regular, 250€: {calculate_discount(250, 'regular'):.2f}€")

# ========================================
# Advanced Techniques
# ========================================
print("\n" + "=" * 50)
print("ADVANCED TECHNIQUES")
print("=" * 50)

# Chained comparisons
age = 25
if 18 <= age < 65:
    print("Working age")

# Multiple conditions with any() and all()
conditions = [age >= 18, has_license, sober]
if all(conditions):
    print("All conditions met")

values = [0, 1, 2, 3]
if any(values):
    print("At least one truthy value")

# Dictionary as switch replacement (before Python 3.10)
def operation(op, a, b):
    operations = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b if b != 0 else "Division by zero!"
    }
    return operations.get(op, "Unknown operation")

print(f"\n5 + 3 = {operation('+', 5, 3)}")
print(f"5 / 0 = {operation('/', 5, 0)}")