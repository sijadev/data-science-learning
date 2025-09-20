# Modul 3: Kontrollstrukturen

## 3.1 Bedingte Anweisungen

### Lernziele
- if, elif, else Statements verstehen und anwenden
- Verschachtelte Bedingungen strukturieren
- Ternären Operator verwenden
- match-case (Pattern Matching) beherrschen

### Kernkonzepte

#### if-elif-else Struktur
```python
if bedingung1:
    # Code wenn bedingung1 True
    pass
elif bedingung2:
    # Code wenn bedingung1 False und bedingung2 True
    pass
else:
    # Code wenn alle Bedingungen False
    pass
```

#### Verschachtelte Bedingungen
```python
# Verschachtelt
if outer_condition:
    if inner_condition:
        do_something()

# Besser mit logischen Operatoren
if outer_condition and inner_condition:
    do_something()
```

#### Ternärer Operator (Conditional Expression)
```python
# Syntax: value_if_true if condition else value_if_false
status = "aktiv" if is_active else "inaktiv"

# Äquivalent zu:
if is_active:
    status = "aktiv"
else:
    status = "inaktiv"
```

#### match-case (Python 3.10+)
Pattern Matching für komplexe Bedingungen:
```python
match value:
    case pattern1:
        action1()
    case pattern2 | pattern3:  # Multiple Patterns
        action2()
    case pattern4 if condition:  # Guard
        action3()
    case _:  # Default
        default_action()
```

**Pattern Types**:
- Literal Patterns: `case 42:`, `case "hello":`
- Capture Patterns: `case x:` (bindet Wert an Variable)
- Sequence Patterns: `case [x, y, z]:`
- Mapping Patterns: `case {"key": value}:`
- Class Patterns: `case Point(x=0, y=0):`

#### Truthy und Falsy Werte
**Falsy** (als False interpretiert):
- `None`
- `False`
- `0`, `0.0`, `0j`
- `""`, `[]`, `()`, `{}`, `set()`

**Truthy**: Alle anderen Werte

### Best Practices
1. **Flache Strukturen bevorzugen**: Zu viele Verschachtelungen vermeiden
2. **Guard Clauses**: Früh returnen statt tief verschachteln
3. **Explizite Vergleiche**: `if x is None:` statt `if not x:`
4. **match-case für komplexe Logik**: Bei vielen elif-Zweigen

### Häufige Fehler

#### Fehler: = statt ==
```python
# Fehler
if x = 5:  # SyntaxError!
    pass

# Richtig
if x == 5:
    pass
```

#### Fehler: Mutable Default-Werte
```python
# Gefährlich
def add_item(item, liste=[]):
    liste.append(item)
    return liste

# Sicher
def add_item(item, liste=None):
    if liste is None:
        liste = []
    liste.append(item)
    return liste
```

---

## 3.2 Schleifen

### Lernziele
- for und while Schleifen beherrschen
- range(), enumerate(), zip() verwenden
- break, continue und else in Schleifen
- List Comprehensions verstehen

### Kernkonzepte

#### for-Schleife
Iteriert über Sequenzen:
```python
for element in sequence:
    process(element)

# Mit Index
for i, element in enumerate(sequence):
    print(f"{i}: {element}")

# Parallel iterieren
for a, b in zip(list1, list2):
    process(a, b)
```

#### while-Schleife
Läuft solange Bedingung True:
```python
while condition:
    do_something()
    update_condition()

# Unendliche Schleife mit break
while True:
    if exit_condition:
        break
    process()
```

#### range() Funktion
Erzeugt Zahlensequenzen:
```python
range(stop)           # 0 bis stop-1
range(start, stop)    # start bis stop-1
range(start, stop, step)  # mit Schrittweite
```

**Beispiele**:
```python
range(5)        # 0, 1, 2, 3, 4
range(2, 8)     # 2, 3, 4, 5, 6, 7
range(10, 0, -2)  # 10, 8, 6, 4, 2
```

#### enumerate() Funktion
Fügt Index zu Iterables hinzu:
```python
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

#### zip() Funktion
Kombiniert mehrere Iterables:
```python
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

#### break und continue
- **break**: Beendet Schleife komplett
- **continue**: Springt zur nächsten Iteration

```python
for i in range(10):
    if i == 5:
        break  # Stoppt bei 5
    if i % 2 == 0:
        continue  # Überspringt gerade Zahlen
    print(i)  # Nur 1, 3
```

#### else in Schleifen
Wird ausgeführt wenn Schleife **nicht** durch break beendet wurde:
```python
for item in items:
    if condition(item):
        break
else:
    print("Kein Item erfüllte die Bedingung")
```

#### List Comprehensions
Kompakte Syntax für Listen-Erzeugung:
```python
# Traditional
squares = []
for x in range(5):
    squares.append(x**2)

# Comprehension
squares = [x**2 for x in range(5)]

# Mit Bedingung
evens = [x for x in range(10) if x % 2 == 0]

# Verschachtelt
matrix = [[i*j for j in range(3)] for i in range(3)]
```

### Schleifen-Patterns

#### Zähler-Pattern
```python
counter = 0
for item in items:
    if condition(item):
        counter += 1
```

#### Akkumulator-Pattern
```python
total = 0
for number in numbers:
    total += number
```

#### Flag-Pattern
```python
found = False
for item in items:
    if condition(item):
        found = True
        break
```

#### Sentinel-Pattern
```python
while True:
    data = get_input()
    if data == SENTINEL:
        break
    process(data)
```

### Performance-Tipps
1. **List Comprehensions**: Schneller als append in Schleife
2. **Generator Expressions**: Bei großen Datenmengen speicherschonend
3. **join() statt +=**: Für String-Konkatenation
4. **enumerate() statt range(len())**: Pythonischer und lesbarer

### Praktische Beispiele

#### Primzahlen finden
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(100) if is_prime(n)]
```

#### Fibonacci-Sequenz
```python
def fibonacci(n):
    a, b = 0, 1
    result = []
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result
```

#### Verschachtelte Iteration
```python
# Multiplikationstabelle
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()
```

### Häufige Fehler und Lösungen

#### Unendliche Schleifen
```python
# Fehler
i = 0
while i < 10:
    print(i)
    # i wird nie erhöht!

# Lösung
i = 0
while i < 10:
    print(i)
    i += 1
```

#### Modifikation während Iteration
```python
# Gefährlich
liste = [1, 2, 3, 4, 5]
for item in liste:
    if item % 2 == 0:
        liste.remove(item)  # Fehler!

# Sicher
liste = [1, 2, 3, 4, 5]
liste = [item for item in liste if item % 2 != 0]
```

### Weiterführende Ressourcen
- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python - Conditionals](https://realpython.com/python-conditional-statements/)
- [Python Loops Tutorial](https://realpython.com/python-for-loop/)
- [List Comprehensions Guide](https://realpython.com/list-comprehension-python/)