# 📦 Module und Pakete

## Was sind Module?

Module sind Python-Dateien, die Funktionen, Klassen und Variablen enthalten, die in anderen Programmen wiederverwendet werden können.

## Module importieren

### Komplettes Modul importieren

```python
import math
print(math.pi)        # 3.14159...
print(math.sqrt(16))  # 4.0
```

### Spezifische Funktionen importieren

```python
from math import pi, sqrt
print(pi)        # 3.14159...
print(sqrt(16))  # 4.0
```

### Import mit Alias

```python
import math as m
import datetime as dt

print(m.pi)
heute = dt.date.today()
```

## Wichtige Standard-Module

### math - Mathematische Funktionen

```python
import math

math.pi          # Pi-Konstante
math.sqrt(x)     # Quadratwurzel
math.ceil(x)     # Aufrunden
math.floor(x)    # Abrunden
math.pow(x, y)   # Potenz
```

### random - Zufallszahlen

```python
import random

random.random()           # Zufallszahl 0-1
random.randint(1, 10)     # Zufällige Ganzzahl
random.choice(liste)      # Zufälliges Element
random.shuffle(liste)     # Liste mischen
```

### datetime - Datum und Zeit

```python
import datetime

jetzt = datetime.datetime.now()
heute = datetime.date.today()
zeit = datetime.time(14, 30, 0)
```

### os - Betriebssystem

```python
import os

os.getcwd()              # Aktuelles Verzeichnis
os.listdir('.')          # Dateien im Verzeichnis
os.path.exists(pfad)     # Prüft ob Pfad existiert
```

### json - JSON-Datenverarbeitung

```python
import json

# Python zu JSON
data = {"name": "Alice", "alter": 30}
json_string = json.dumps(data)

# JSON zu Python
data_back = json.loads(json_string)
```

## Collections-Modul

Erweiterte Datenstrukturen:

```python
from collections import Counter, defaultdict, namedtuple

# Counter für Häufigkeiten
counter = Counter("hello world")
print(counter)  # Counter({'l': 3, 'o': 2, ...})

# defaultdict für automatische Standardwerte
dd = defaultdict(list)
dd['schlüssel'].append('wert')

# namedtuple für strukturierte Daten
Person = namedtuple('Person', 'name alter')
alice = Person('Alice', 30)
```

## Eigene Module erstellen

1. Erstelle eine .py-Datei (z.B. `mein_modul.py`)
2. Definiere Funktionen und Variablen
3. Importiere das Modul in anderen Dateien

```python
# mein_modul.py
def begrüßung(name):
    return f"Hallo {name}!"

PI = 3.14159

# hauptprogramm.py
import mein_modul
print(mein_modul.begrüßung("Welt"))
```

## Pakete

Pakete sind Ordner, die mehrere Module enthalten und mit einer `__init__.py`-Datei gekennzeichnet sind.

```
mein_paket/
    __init__.py
    modul1.py
    modul2.py
    unterpaket/
        __init__.py
        modul3.py
```

## Module-Suchpfad

Python sucht Module in:

1. Aktuelles Verzeichnis
2. PYTHONPATH-Umgebungsvariable
3. Standard-Bibliothek
4. Site-packages (installierte Pakete)

```python
import sys
print(sys.path)  # Zeigt Suchpfade an
```