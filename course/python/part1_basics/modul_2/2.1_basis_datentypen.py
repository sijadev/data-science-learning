# 2.1 Basis-Datentypen - Code Examples

# ========================================
# Integer (Ganze Zahlen)
# ========================================
print("=" * 50)
print("INTEGER")
print("=" * 50)

# Dezimal
age = 25
year = 2024
negative = -42

# Andere Zahlensysteme
binary = 0b1010      # Binär (10 in Dezimal)
octal = 0o12         # Oktal (10 in Dezimal)
hexadecimal = 0xA    # Hexadezimal (10 in Dezimal)

print(f"Dezimal: {age}")
print(f"Binär 0b1010: {binary}")
print(f"Oktal 0o12: {octal}")
print(f"Hex 0xA: {hexadecimal}")

# Große Zahlen mit Unterstrichen (für bessere Lesbarkeit)
million = 1_000_000
print(f"Eine Million: {million:,}")

# ========================================
# Float (Gleitkommazahlen)
# ========================================
print("\n" + "=" * 50)
print("FLOAT")
print("=" * 50)

pi = 3.14159
temperature = -17.5
scientific = 2.5e-3  # Wissenschaftliche Notation (0.0025)

print(f"Pi: {pi}")
print(f"Temperatur: {temperature}°C")
print(f"Wissenschaftlich 2.5e-3: {scientific}")

# Float Genauigkeit
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # Achtung: Floating-Point Arithmetik!
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")

# Unendlichkeit und NaN
import math
infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan')

print(f"Unendlich: {infinity}")
print(f"Ist unendlich? {math.isinf(infinity)}")
print(f"Ist NaN? {math.isnan(not_a_number)}")

# ========================================
# Complex (Komplexe Zahlen)
# ========================================
print("\n" + "=" * 50)
print("COMPLEX")
print("=" * 50)

z1 = 3 + 4j
z2 = complex(2, -1)

print(f"Komplexe Zahl z1: {z1}")
print(f"Realteil: {z1.real}, Imaginärteil: {z1.imag}")
print(f"Konjugiert: {z1.conjugate()}")
print(f"Betrag: {abs(z1)}")

# ========================================
# String (Zeichenketten)
# ========================================
print("\n" + "=" * 50)
print("STRING")
print("=" * 50)

# String-Erstellung
single_quote = 'Hallo'
double_quote = "Welt"
triple_quote = """Mehrzeilige
Zeichenkette"""
raw_string = r"Raw String: \n wird nicht interpretiert"

print(f"Single Quote: {single_quote}")
print(f"Double Quote: {double_quote}")
print(f"Triple Quote: {triple_quote}")
print(f"Raw String: {raw_string}")

# String-Operationen
name = "Python"
print(f"\nString '{name}':")
print(f"Länge: {len(name)}")
print(f"Großbuchstaben: {name.upper()}")
print(f"Kleinbuchstaben: {name.lower()}")
print(f"Erster Buchstabe: {name[0]}")
print(f"Letzter Buchstabe: {name[-1]}")
print(f"Slice [1:4]: {name[1:4]}")

# String-Methoden
text = "  Python Programming  "
print(f"\nOriginal: '{text}'")
print(f"Strip: '{text.strip()}'")
print(f"Replace: '{text.replace('Python', 'Java')}'")
print(f"Split: {text.split()}")
print(f"Enthält 'Python': {'Python' in text}")

# String-Formatierung
age = 25
height = 1.75
formatted = f"Ich bin {age} Jahre alt und {height:.2f}m groß"
print(f"F-String: {formatted}")

# Escape-Sequenzen
escaped = "Zeile 1\nZeile 2\tTabulator\r\nWindows-Zeile"
print(f"\nEscape-Sequenzen:\n{escaped}")

# ========================================
# Boolean (Wahrheitswerte)
# ========================================
print("\n" + "=" * 50)
print("BOOLEAN")
print("=" * 50)

is_active = True
is_deleted = False

print(f"is_active: {is_active}")
print(f"is_deleted: {is_deleted}")

# Boolean aus Vergleichen
x, y = 10, 20
print(f"\n{x} > {y}: {x > y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")

# Truthy und Falsy Werte
print("\nFalsy Werte:")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')}")
print(f"bool([]): {bool([])}")
print(f"bool(None): {bool(None)}")

print("\nTruthy Werte:")
print(f"bool(1): {bool(1)}")
print(f"bool('Text'): {bool('Text')}")
print(f"bool([1, 2]): {bool([1, 2])}")

# ========================================
# None (Null-Wert)
# ========================================
print("\n" + "=" * 50)
print("NONE")
print("=" * 50)

result = None
print(f"result: {result}")
print(f"result is None: {result is None}")
print(f"type(None): {type(None)}")

# None als Default-Wert
def greet(name=None):
    if name is None:
        return "Hallo, Fremder!"
    return f"Hallo, {name}!"

print(greet())
print(greet("Python"))

# ========================================
# Type Casting (Typumwandlung)
# ========================================
print("\n" + "=" * 50)
print("TYPE CASTING")
print("=" * 50)

# String zu Nummer
str_number = "42"
int_number = int(str_number)
float_number = float(str_number)

print(f"String '{str_number}' zu Int: {int_number}")
print(f"String '{str_number}' zu Float: {float_number}")

# Nummer zu String
number = 123
str_from_number = str(number)
print(f"Nummer {number} zu String: '{str_from_number}'")

# Float zu Int (Abschneiden)
pi = 3.14159
int_pi = int(pi)
print(f"Float {pi} zu Int: {int_pi}")

# Bool Konvertierungen
print(f"\nint(True): {int(True)}")
print(f"int(False): {int(False)}")
print(f"str(True): '{str(True)}'")

# Fehlerbehandlung bei Casting
try:
    invalid = int("abc")
except ValueError as e:
    print(f"\nFehler beim Casting: {e}")

# ========================================
# Type Checking
# ========================================
print("\n" + "=" * 50)
print("TYPE CHECKING")
print("=" * 50)

examples = [42, 3.14, "Text", True, None, [1, 2], {'a': 1}]

for value in examples:
    print(f"{str(value):10} -> {type(value).__name__:10} | isinstance(int): {isinstance(value, int)}")

# Multiple Type Check
number = 42
print(f"\n{number} ist int oder float: {isinstance(number, (int, float))}")

# ========================================
# Dynamische Typisierung
# ========================================
print("\n" + "=" * 50)
print("DYNAMISCHE TYPISIERUNG")
print("=" * 50)

# Variable kann Typ ändern
variable = 42
print(f"variable = 42, Typ: {type(variable)}")

variable = "Jetzt ein String"
print(f"variable = 'Jetzt ein String', Typ: {type(variable)}")

variable = [1, 2, 3]
print(f"variable = [1, 2, 3], Typ: {type(variable)}")