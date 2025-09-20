# Modul 5: Funktionen Grundlagen

## 5.1 Funktionsdefinition

### Lernziele
- Funktionen definieren und aufrufen
- Parameter und Argumente verstehen
- Return-Werte verwenden
- Docstrings schreiben
- Type Hints anwenden

### Kernkonzepte

#### Grundlegende Funktionsstruktur
```python
def function_name(parameters):
    """Docstring - Beschreibung der Funktion"""
    # Funktionskörper
    return value  # Optional
```

#### Parameter-Arten

##### Positionale Parameter
```python
def greet(name, age):
    return f"Hallo {name}, du bist {age} Jahre alt"

greet("Alice", 30)  # Reihenfolge wichtig
```

##### Keyword Arguments
```python
greet(age=30, name="Alice")  # Reihenfolge egal
```

##### Default-Parameter
```python
def greet(name, title="Herr/Frau"):
    return f"Guten Tag, {title} {name}"

greet("Schmidt")           # Verwendet Default
greet("Weber", "Dr.")      # Überschreibt Default
```

##### Variable Parameter (*args)
```python
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4, 5)  # Beliebig viele Argumente
```

##### Keyword Parameter (**kwargs)
```python
def create_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(name="Alice", age=30, city="Berlin")
```

##### Kombination aller Parameter-Arten
```python
def flexible_func(pos1, pos2, *args, default="value", **kwargs):
    # Reihenfolge: positional, *args, default, **kwargs
    pass
```

#### Return-Werte

##### Kein Return (None)
```python
def print_message(msg):
    print(msg)
    # Implizites return None
```

##### Einzelner Wert
```python
def square(x):
    return x ** 2
```

##### Mehrere Werte (Tupel)
```python
def get_name_age():
    return "Alice", 30

name, age = get_name_age()  # Tuple Unpacking
```

##### Bedingtes Return
```python
def check_positive(number):
    if number > 0:
        return True
    return False
```

#### Docstrings
```python
def calculate_area(width, height):
    """
    Berechnet die Fläche eines Rechtecks.

    Args:
        width (float): Breite des Rechtecks
        height (float): Höhe des Rechtecks

    Returns:
        float: Die Fläche des Rechtecks

    Raises:
        ValueError: Wenn width oder height negativ

    Example:
        >>> calculate_area(5, 3)
        15
    """
    if width < 0 or height < 0:
        raise ValueError("Negative Werte nicht erlaubt")
    return width * height
```

#### Type Hints (Python 3.5+)
```python
from typing import List, Dict, Optional, Union

def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

def flexible_input(value: Union[int, str]) -> str:
    return str(value)
```

#### Funktionen als First-Class Objects
```python
# Funktionen können Variablen zugewiesen werden
my_func = len

# Als Parameter übergeben werden
def apply_to_list(lst, func):
    return [func(x) for x in lst]

# In Datenstrukturen gespeichert werden
operations = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y
}
```

### Best Practices

#### Funktionsdesign
1. **Single Responsibility**: Eine Funktion, eine Aufgabe
2. **Aussagekräftige Namen**: `calculate_tax()` statt `calc()`
3. **Kurze Funktionen**: Maximal 20-30 Zeilen
4. **Keine Seiteneffekte**: Vermeiden globaler Änderungen

#### Parameter
1. **Wenige Parameter**: Maximal 4-5 Parameter
2. **Defaults für optionale Werte**
3. **Immutable Defaults**: Nie `[]` oder `{}` als Default

```python
# Falsch
def add_item(item, lst=[]):
    lst.append(item)
    return lst

# Richtig
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

#### Documentation
1. **Immer Docstrings** für public Functions
2. **Type Hints** für bessere IDE-Unterstützung
3. **Beispiele** in Docstrings

---

## 5.2 Scope und Namespaces

### Lernziele
- LEGB-Regel verstehen und anwenden
- global und nonlocal Keywords verwenden
- Closures erstellen und nutzen
- Namespace-Konzepte beherrschen

### Kernkonzepte

#### LEGB-Regel
Python sucht Variablen in folgender Reihenfolge:

1. **Local**: Innerhalb der aktuellen Funktion
2. **Enclosing**: In umschließenden Funktionen
3. **Global**: Auf Modul-Ebene
4. **Built-in**: Eingebaute Namen (len, print, etc.)

```python
x = "Global"  # Global

def outer():
    x = "Enclosing"  # Enclosing

    def inner():
        x = "Local"  # Local
        print(x)     # Findet "Local"

    inner()

outer()
```

#### Local Scope
```python
def my_function():
    local_var = "Nur hier verfügbar"
    print(local_var)  # OK

my_function()
# print(local_var)  # NameError!
```

#### Global Scope
```python
global_var = "Überall verfügbar"

def access_global():
    print(global_var)  # Lesen OK

def modify_global():
    global global_var  # Notwendig zum Ändern
    global_var = "Geändert"

access_global()
modify_global()
```

#### Enclosing Scope (Closures)
```python
def outer_function(x):
    def inner_function(y):
        return x + y  # x aus enclosing scope
    return inner_function

add_5 = outer_function(5)
result = add_5(3)  # 8
```

#### nonlocal Keyword
```python
def create_counter():
    count = 0

    def increment():
        nonlocal count  # Zugriff auf enclosing variable
        count += 1
        return count

    return increment

counter = create_counter()
print(counter())  # 1
print(counter())  # 2
```

### Closures

#### Was sind Closures?
Funktionen, die auf Variablen aus ihrem enclosing scope zugreifen:

```python
def multiplier_factory(factor):
    def multiplier(number):
        return number * factor  # factor wird "eingefangen"
    return multiplier

double = multiplier_factory(2)
triple = multiplier_factory(3)

print(double(5))  # 10
print(triple(5))  # 15
```

#### Praktische Anwendungen
```python
# Configuration
def create_api_client(base_url, api_key):
    def make_request(endpoint):
        return f"GET {base_url}/{endpoint} (key: {api_key})"
    return make_request

client = create_api_client("https://api.example.com", "secret123")

# State Management
def create_accumulator(start=0):
    total = start

    def add(value):
        nonlocal total
        total += value
        return total

    def get():
        return total

    return add, get

add_func, get_func = create_accumulator(10)
```

### Namespace-Debugging

#### globals() und locals()
```python
global_var = "Global value"

def debug_function():
    local_var = "Local value"

    print("Globals:", list(globals().keys())[:5])
    print("Locals:", locals())

debug_function()
```

#### vars() Funktion
```python
class Example:
    def __init__(self):
        self.attr = "value"

obj = Example()
print(vars(obj))  # {'attr': 'value'}
```

### Häufige Fehler und Lösungen

#### UnboundLocalError
```python
# Fehler
count = 0
def increment():
    count += 1  # UnboundLocalError!

# Lösung
count = 0
def increment():
    global count
    count += 1
```

#### Mutable Default Arguments
```python
# Gefährlich
def add_item(item, lst=[]):
    lst.append(item)
    return lst

# Sicher
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

#### Late Binding Closures
```python
# Unerwartetes Verhalten
functions = []
for i in range(3):
    functions.append(lambda: i)  # Alle referenzieren dasselbe i!

# Alle geben 2 zurück
for f in functions:
    print(f())  # 2, 2, 2

# Lösung: Default Parameter
functions = []
for i in range(3):
    functions.append(lambda x=i: x)  # x wird zur Definitionszeit gebunden

# Oder: Closure Factory
def make_closure(i):
    return lambda: i

functions = [make_closure(i) for i in range(3)]
```

### Best Practices

#### Scope Management
1. **Minimiere globale Variablen**
2. **Verwende Klassen** für Zustand statt globaler Variablen
3. **Explizite Parameter** statt globaler Zugriffe
4. **Closures für Konfiguration** und Zustand

#### Naming
1. **Eindeutige Namen** in verschiedenen Scopes
2. **`_private`** Convention für "private" Variablen
3. **CONSTANTS** in GROSSBUCHSTABEN

#### Code Organization
```python
# Gut strukturiert
class DatabaseConfig:
    HOST = "localhost"
    PORT = 5432

    @classmethod
    def get_connection_string(cls):
        return f"postgresql://{cls.HOST}:{cls.PORT}"

# Statt globaler Variablen
def create_processor(config):
    def process(data):
        # Nutzt config aus closure
        return f"Processing {data} with {config}"
    return process
```

### Weiterführende Ressourcen
- [Python Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [Real Python - Python Scope](https://realpython.com/python-scope-legb-rule/)
- [Closures in Python](https://realpython.com/python-closures/)
- [Function Documentation Guide](https://peps.python.org/pep-0257/)