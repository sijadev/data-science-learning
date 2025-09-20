# Modul 4: Datenstrukturen

## 4.1 Listen (bereits erstellt)

### Lernziele
- Listen erstellen, manipulieren und durchlaufen
- List Comprehensions verstehen und anwenden
- Wichtige Listen-Methoden beherrschen
- Slicing und Indizierung verwenden

---

## 4.2 Tupel

### Lernziele
- Unveränderlichkeit von Tupeln verstehen
- Tuple Unpacking beherrschen
- Named Tuples verwenden
- Wann Tupel statt Listen verwenden

### Kernkonzepte

#### Tupel-Eigenschaften
- **Unveränderlich (Immutable)**: Können nach Erstellung nicht geändert werden
- **Geordnet**: Elemente haben eine feste Reihenfolge
- **Duplikate erlaubt**: Gleiche Werte können mehrfach vorkommen
- **Hashbar**: Können als Dictionary-Schlüssel verwendet werden

#### Tupel-Erstellung
```python
# Verschiedene Syntaxen
leer = ()
einzeln = (42,)  # Komma wichtig!
koordinaten = (10, 20)
ohne_klammern = 1, 2, 3  # Tuple Packing

# Aus anderen Typen
aus_liste = tuple([1, 2, 3])
aus_string = tuple("ABC")  # ('A', 'B', 'C')
```

#### Tuple Unpacking
```python
punkt = (10, 20)
x, y = punkt

# Extended Unpacking
zahlen = (1, 2, 3, 4, 5)
erste, *mitte, letzte = zahlen
# erste=1, mitte=[2,3,4], letzte=5

# Ignorieren von Werten
name, _, alter = ("Alice", "unwichtig", 30)
```

#### Named Tuples
```python
from collections import namedtuple

Person = namedtuple('Person', ['name', 'alter', 'stadt'])
alice = Person('Alice', 30, 'Berlin')

print(alice.name)  # Zugriff über Attribut
print(alice[0])    # Zugriff über Index
```

### Wann Tupel verwenden?
- **Koordinaten**: `(x, y, z)`
- **Datensätze**: `(name, alter, email)`
- **Dictionary-Schlüssel**: Unveränderliche Zusammenstellungen
- **Funktions-Rückgaben**: Mehrere zusammengehörige Werte
- **Performance**: Etwas schneller als Listen bei Iteration

---

## 4.3 Dictionaries

### Lernziele
- Key-Value Paare verstehen und verwenden
- Dictionary-Methoden beherrschen
- Dictionary Comprehensions anwenden
- Verschachtelte Dictionaries verwalten

### Kernkonzepte

#### Dictionary-Eigenschaften
- **Key-Value Struktur**: Zuordnung von Schlüsseln zu Werten
- **Keine Duplikate**: Jeder Schlüssel ist eindeutig
- **Veränderbar (Mutable)**: Können nach Erstellung geändert werden
- **Ungeordnet** (Python < 3.7) / **Geordnet** (Python ≥ 3.7)

#### Dictionary-Erstellung
```python
# Verschiedene Syntaxen
person = {"name": "Alice", "alter": 30}
zahlen = dict(eins=1, zwei=2, drei=3)
aus_liste = dict([("a", 1), ("b", 2)])

# Dictionary Comprehension
quadrate = {x: x**2 for x in range(5)}
```

#### Zugriff und Manipulation
```python
# Sicherer Zugriff
wert = dict.get("schlüssel", "default")

# Hinzufügen/Ändern
dict["neuer_key"] = "neuer_wert"
dict.update({"key1": "wert1", "key2": "wert2"})

# Entfernen
wert = dict.pop("key")
del dict["key"]
```

#### Iteration
```python
for key in dict:                    # Über Schlüssel
for value in dict.values():         # Über Werte
for key, value in dict.items():     # Über Paare
```

### Praktische Anwendungen
- **Konfiguration**: Einstellungen speichern
- **Caching**: Berechnete Werte zwischenspeichern
- **Gruppierung**: Daten nach Kategorien ordnen
- **Zählen**: Häufigkeiten ermitteln
- **Mapping**: Zuordnungen definieren

---

## 4.4 Sets

### Lernziele
- Mengenoperationen verstehen und anwenden
- Duplikate effizient entfernen
- Set Comprehensions verwenden
- Frozen Sets kennenlernen

### Kernkonzepte

#### Set-Eigenschaften
- **Keine Duplikate**: Jeder Wert ist eindeutig
- **Ungeordnet**: Keine feste Reihenfolge
- **Veränderbar**: Können nach Erstellung geändert werden
- **Nur hashbare Elemente**: Unveränderliche Typen

#### Set-Erstellung
```python
# Verschiedene Syntaxen
zahlen = {1, 2, 3, 4, 5}
aus_liste = set([1, 2, 3, 2, 1])  # {1, 2, 3}
leer = set()  # Nicht {} - das ist Dictionary!

# Set Comprehension
gerade = {x for x in range(10) if x % 2 == 0}
```

#### Mengenoperationen
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Vereinigung
a | b  # oder a.union(b)

# Schnittmenge
a & b  # oder a.intersection(b)

# Differenz
a - b  # oder a.difference(b)

# Symmetrische Differenz
a ^ b  # oder a.symmetric_difference(b)
```

#### Vergleiche
```python
# Teilmenge
{1, 2}.issubset({1, 2, 3, 4})  # True

# Obermenge
{1, 2, 3}.issuperset({1, 2})   # True

# Disjunkt (keine gemeinsamen Elemente)
{1, 2}.isdisjoint({3, 4})      # True
```

#### Frozen Sets
```python
fs = frozenset([1, 2, 3])
# Unveränderlich, kann als Dict-Key verwendet werden
```

### Praktische Anwendungen
- **Duplikate entfernen**: `list(set(liste))`
- **Mitgliedschaftstests**: Sehr schnell bei großen Datenmengen
- **Mengenvergleiche**: Gemeinsame/unterschiedliche Elemente finden
- **Filtering**: Elemente basierend auf Mitgliedschaft filtern

---

## Vergleich der Datenstrukturen

| Eigenschaft | Liste | Tupel | Dictionary | Set |
|-------------|-------|--------|------------|-----|
| Veränderbar | ✅ | ❌ | ✅ | ✅ |
| Geordnet | ✅ | ✅ | ✅ (3.7+) | ❌ |
| Duplikate | ✅ | ✅ | ❌ (Keys) | ❌ |
| Indizierung | ✅ | ✅ | Key-basiert | ❌ |
| Slicing | ✅ | ✅ | ❌ | ❌ |
| Hashbar | ❌ | ✅ | ❌ | ❌ |

## Best Practices

### Listen
- Für Sequenzen veränderlicher Daten
- Wenn Reihenfolge wichtig ist
- Für Daten die häufig geändert werden

### Tupel
- Für unveränderliche Sequenzen
- Als Dictionary-Keys
- Für Koordinaten und Datensätze
- Return-Values von Funktionen

### Dictionaries
- Für Key-Value Zuordnungen
- Schnelle Lookups
- Strukturierte Daten
- Konfigurationen und Mappings

### Sets
- Für eindeutige Werte
- Mengenoperationen
- Schnelle Mitgliedschaftstests
- Duplikate entfernen

### Performance-Tipps
1. **Mitgliedschaftstest**: Set > Dict > Liste
2. **Sortierte Daten**: Nutze `bisect` für Listen
3. **Große Datenmengen**: Wähle richtige Datenstruktur
4. **Memory**: Tupel < Listen, Sets sind speicher-effizient

### Häufige Fehler
1. **Leeres Set**: `set()` nicht `{}`
2. **Dictionary vs. Set**: `{}` ist Dictionary
3. **Tupel mit einem Element**: `(42,)` nicht `(42)`
4. **Unveränderliche Schlüssel**: Nur hashbare Typen in Sets/Dict-Keys
5. **Liste als Dict-Key**: Nicht möglich, Tupel verwenden

### Weiterführende Ressource
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python - Python Data Structures](https://realpython.com/python-data-structures/)
- [Collections Module](https://docs.python.org/3/library/collections.html)