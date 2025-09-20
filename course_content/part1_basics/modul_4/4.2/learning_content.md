# 🗂️ Tupel

## Was sind Tupel?

Tupel sind unveränderliche Sequenzen - einmal erstellt, können sie nicht mehr verändert werden.

```python
koordinaten = (10, 20)
person = ("Alice", 30, "Berlin")
```

## Tupel vs. Listen

| Eigenschaft | Tupel | Listen |
|-------------|-------|--------|
| Veränderbarkeit | Unveränderlich | Veränderlich |
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Performance | Schneller | Langsamer |
| Verwendung | Feste Daten | Variable Daten |

## Tupel-Operationen

### Zugriff

```python
punkt = (5, 10)
x = punkt[0]  # 5
y = punkt[1]  # 10
```

### Unpacking

```python
koordinaten = (10, 20)
x, y = koordinaten

# Extended Unpacking
zahlen = (1, 2, 3, 4, 5)
erste, *mittlere, letzte = zahlen
```

## Named Tuples

Tupel mit benannten Feldern für bessere Lesbarkeit:

```python
from collections import namedtuple

Person = namedtuple('Person', ['name', 'alter', 'beruf'])
alice = Person("Alice", 30, "Entwicklerin")
print(alice.name)  # Alice
```

## Verwendungszwecke

- Koordinaten (x, y)
- RGB-Farben (r, g, b)
- Datenbankeinträge
- Funktions-Rückgabewerte
- Dictionary-Keys