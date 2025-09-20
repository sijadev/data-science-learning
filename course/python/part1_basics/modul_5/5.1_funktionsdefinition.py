# 5.1 Funktionsdefinition - Code Examples

# ========================================
# Einfache Funktionen
# ========================================
print("=" * 50)
print("EINFACHE FUNKTIONEN")
print("=" * 50)

# Funktion ohne Parameter und Rückgabe
def greet():
    print("Hallo Welt!")

greet()

# Funktion mit Parameter
def greet_person(name):
    print(f"Hallo {name}!")

greet_person("Alice")

# Funktion mit Rückgabewert
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Funktion mit mehreren Parametern und Rückgabe
def calculate_rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter  # Gibt Tupel zurück

area, perimeter = calculate_rectangle(5, 3)
print(f"Rechteck: Fläche={area}, Umfang={perimeter}")

# ========================================
# Parameter und Argumente
# ========================================
print("\n" + "=" * 50)
print("PARAMETER UND ARGUMENTE")
print("=" * 50)

# Positionale Parameter
def divide(dividend, divisor):
    if divisor == 0:
        return "Division durch Null nicht möglich"
    return dividend / divisor

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")

# Keyword Arguments
def create_user(name, age, city):
    return f"Benutzer: {name}, {age} Jahre, aus {city}"

# Verschiedene Aufrufarten
user1 = create_user("Alice", 30, "Berlin")
user2 = create_user(age=25, name="Bob", city="München")
user3 = create_user("Charlie", city="Hamburg", age=35)

print(user1)
print(user2)
print(user3)

# ========================================
# Default-Parameter
# ========================================
print("\n" + "=" * 50)
print("DEFAULT-PARAMETER")
print("=" * 50)

def greet_with_title(name, title="Herr/Frau"):
    return f"Guten Tag, {title} {name}!"

print(greet_with_title("Schmidt"))
print(greet_with_title("Müller", "Dr."))
print(greet_with_title("Weber", title="Prof."))

# Mehrere Default-Parameter
def configure_server(host="localhost", port=8000, debug=False):
    config = {
        "host": host,
        "port": port,
        "debug": debug
    }
    return config

print("\nServer-Konfigurationen:")
print(configure_server())  # Alle Defaults
print(configure_server("192.168.1.1"))  # Nur host geändert
print(configure_server(port=9000, debug=True))  # port und debug geändert

# ========================================
# Variable Parameter (*args)
# ========================================
print("\n" + "=" * 50)
print("VARIABLE PARAMETER (*args)")
print("=" * 50)

def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"Summe von 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Summe von 1 bis 10: {sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")
print(f"Summe ohne Argumente: {sum_all()}")

# Mit normalen Parametern kombiniert
def describe_person(name, *hobbies):
    if hobbies:
        hobby_list = ", ".join(hobbies)
        return f"{name} mag: {hobby_list}"
    else:
        return f"{name} hat keine angegebenen Hobbies"

print(f"\n{describe_person('Alice')}")
print(f"{describe_person('Bob', 'Lesen')}")
print(f"{describe_person('Charlie', 'Lesen', 'Sport', 'Musik')}")

# ========================================
# Keyword-Parameter (**kwargs)
# ========================================
print("\n" + "=" * 50)
print("KEYWORD-PARAMETER (**kwargs)")
print("=" * 50)

def create_profile(**info):
    profile = "Profil:\n"
    for key, value in info.items():
        profile += f"  {key}: {value}\n"
    return profile

print(create_profile(name="Alice", age=30, city="Berlin"))
print(create_profile(name="Bob", job="Developer", experience="5 Jahre"))

# Kombination von *args und **kwargs
def flexible_function(*args, **kwargs):
    print(f"Positionale Argumente: {args}")
    print(f"Keyword Argumente: {kwargs}")

print("Flexibler Aufruf:")
flexible_function(1, 2, 3, name="Alice", age=30)

# ========================================
# Docstrings
# ========================================
print("\n" + "=" * 50)
print("DOCSTRINGS")
print("=" * 50)

def calculate_bmi(weight, height):
    """
    Berechnet den Body Mass Index (BMI).

    Args:
        weight (float): Gewicht in Kilogramm
        height (float): Größe in Metern

    Returns:
        float: BMI-Wert

    Example:
        >>> calculate_bmi(70, 1.75)
        22.857142857142858
    """
    return weight / (height ** 2)

bmi = calculate_bmi(70, 1.75)
print(f"BMI: {bmi:.2f}")

# Docstring anzeigen
print(f"\nDocstring:\n{calculate_bmi.__doc__}")

# Mit help() funktion
# help(calculate_bmi)  # Würde detaillierte Hilfe anzeigen

# ========================================
# Return-Werte
# ========================================
print("\n" + "=" * 50)
print("RETURN-WERTE")
print("=" * 50)

# Kein explizites return (gibt None zurück)
def print_message(message):
    print(f"Nachricht: {message}")

result = print_message("Hallo")
print(f"Rückgabe: {result}")

# Frühes return
def check_age(age):
    if age < 0:
        return "Ungültiges Alter"
    if age < 18:
        return "Minderjährig"
    if age < 65:
        return "Erwachsen"
    return "Senior"

ages = [5, 16, 25, 70, -5]
for age in ages:
    print(f"Alter {age}: {check_age(age)}")

# Mehrere Rückgabewerte
def analyze_text(text):
    words = text.split()
    return len(text), len(words), text.upper(), text.lower()

text = "Python ist toll"
char_count, word_count, upper, lower = analyze_text(text)
print(f"\nText-Analyse von '{text}':")
print(f"Zeichen: {char_count}, Wörter: {word_count}")
print(f"Groß: {upper}")
print(f"Klein: {lower}")

# ========================================
# Funktionen als First-Class Objects
# ========================================
print("\n" + "=" * 50)
print("FUNKTIONEN ALS OBJEKTE")
print("=" * 50)

# Funktionen können Variablen zugewiesen werden
def square(x):
    return x * x

my_function = square
print(f"square(5) = {square(5)}")
print(f"my_function(5) = {my_function(5)}")

# Funktionen können als Parameter übergeben werden
def apply_operation(numbers, operation):
    return [operation(num) for num in numbers]

numbers = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, square)
print(f"\nZahlen: {numbers}")
print(f"Quadriert: {squared}")

# Funktionen können in Listen gespeichert werden
def cube(x):
    return x ** 3

def double(x):
    return x * 2

operations = [square, cube, double]
x = 3
for op in operations:
    print(f"{op.__name__}({x}) = {op(x)}")

# ========================================
# Nested Functions (Verschachtelte Funktionen)
# ========================================
print("\n" + "=" * 50)
print("VERSCHACHTELTE FUNKTIONEN")
print("=" * 50)

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# Closure erstellen
add_5 = outer_function(5)
print(f"add_5(3) = {add_5(3)}")

# Factory Pattern
def create_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(f"\ndouble(4) = {double(4)}")
print(f"triple(4) = {triple(4)}")

# ========================================
# Rekursion
# ========================================
print("\n" + "=" * 50)
print("REKURSION")
print("=" * 50)

def factorial(n):
    """Berechnet die Fakultät von n rekursiv."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

for i in range(6):
    print(f"{i}! = {factorial(i)}")

# Fibonacci rekursiv
def fibonacci(n):
    """Berechnet die n-te Fibonacci-Zahl rekursiv."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\nFibonacci-Folge:")
for i in range(10):
    print(f"fib({i}) = {fibonacci(i)}")

# ========================================
# Lambda-Funktionen (Preview)
# ========================================
print("\n" + "=" * 50)
print("LAMBDA-FUNKTIONEN")
print("=" * 50)

# Einfache Lambda
square_lambda = lambda x: x ** 2
print(f"Lambda square(4) = {square_lambda(4)}")

# Lambda mit mehreren Parametern
add_lambda = lambda x, y: x + y
print(f"Lambda add(3, 5) = {add_lambda(3, 5)}")

# Lambda in Funktionen
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"\nOriginal: {numbers}")
print(f"Quadriert: {squared}")
print(f"Gerade: {evens}")

# ========================================
# Type Hints (Modern Python)
# ========================================
print("\n" + "=" * 50)
print("TYPE HINTS")
print("=" * 50)

def add_with_types(a: int, b: int) -> int:
    """Addiert zwei Ganzzahlen."""
    return a + b

def greet_typed(name: str, age: int = 0) -> str:
    """Begrüßt eine Person mit optionalem Alter."""
    if age > 0:
        return f"Hallo {name}, du bist {age} Jahre alt!"
    return f"Hallo {name}!"

print(add_with_types(5, 3))
print(greet_typed("Alice"))
print(greet_typed("Bob", 30))

# Komplexere Type Hints
from typing import List, Dict, Optional

def process_names(names: List[str]) -> Dict[str, int]:
    """Erstellt ein Dictionary mit Namen und deren Längen."""
    return {name: len(name) for name in names}

def find_user(user_id: int) -> Optional[str]:
    """Findet einen Benutzer oder gibt None zurück."""
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id)

names = ["Alice", "Bob", "Charlie"]
name_lengths = process_names(names)
print(f"\nNamen-Längen: {name_lengths}")

user = find_user(2)
print(f"Benutzer 2: {user}")
user = find_user(99)
print(f"Benutzer 99: {user}")