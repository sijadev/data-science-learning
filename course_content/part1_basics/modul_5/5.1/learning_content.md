# ⚙️ Funktionen definieren und aufrufen

## Was sind Funktionen?

Funktionen sind wiederverwendbare Code-Blöcke, die eine bestimmte Aufgabe erfüllen.

```python
def begrüßung():
    print("Hallo Welt!")

begrüßung()  # Funktionsaufruf
```

## Parameter und Argumente

### Einfache Parameter

```python
def begrüße_person(name):
    print(f"Hallo {name}!")

begrüße_person("Alice")
```

### Mehrere Parameter

```python
def addieren(a, b):
    return a + b

result = addieren(5, 3)  # 8
```

### Standardwerte

```python
def begrüßung(name, tageszeit="Tag"):
    print(f"Guten {tageszeit}, {name}!")

begrüßung("Alice")           # Guten Tag, Alice!
begrüßung("Bob", "Morgen")   # Guten Morgen, Bob!
```

## Rückgabewerte

```python
def quadrat(x):
    return x ** 2

ergebnis = quadrat(5)  # 25
```

## Variable Argumente

### *args - Variable Anzahl Argumente

```python
def summe(*zahlen):
    return sum(zahlen)

print(summe(1, 2, 3))        # 6
print(summe(1, 2, 3, 4, 5))  # 15
```

### **kwargs - Variable Keyword-Argumente

```python
def person_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

person_info(name="Alice", alter=30, beruf="Entwicklerin")
```

## Lokale vs. Globale Variablen

```python
globale_variable = "Ich bin global"

def test_funktion():
    lokale_variable = "Ich bin lokal"
    print(globale_variable)  # Zugriff auf globale Variable
    print(lokale_variable)   # Zugriff auf lokale Variable

test_funktion()
# print(lokale_variable)  # Fehler! Nicht außerhalb verfügbar
```

## Lambda-Funktionen

Kurze, anonyme Funktionen für einfache Operationen:

```python
quadrat = lambda x: x ** 2
print(quadrat(5))  # 25

# Mit Listen
zahlen = [1, 2, 3, 4, 5]
quadrate = list(map(lambda x: x**2, zahlen))
print(quadrate)  # [1, 4, 9, 16, 25]
```

## Best Practices

- Verwende aussagekräftige Funktionsnamen
- Eine Funktion sollte nur eine Aufgabe erfüllen
- Verwende Docstrings zur Dokumentation
- Vermeide zu viele Parameter
- Nutze Type Hints (moderne Python-Praxis)