# 📋 Listen

## Was sind Listen?

Listen sind veränderbare Sequenzen, die verschiedene Datentypen speichern können.

```python
zahlen = [1, 2, 3, 4, 5]
gemischt = [1, "Text", 3.14, True]
```

## Listen-Operationen

### Zugriff auf Elemente

- Index-Zugriff: `liste[0]`
- Negativer Index: `liste[-1]` (letztes Element)
- Slicing: `liste[1:4]`

### Elemente hinzufügen

- `append()` - Fügt ein Element am Ende hinzu
- `extend()` - Fügt mehrere Elemente hinzu
- `insert()` - Fügt Element an bestimmter Position ein

### Elemente entfernen

- `remove()` - Entfernt erstes Vorkommen
- `pop()` - Entfernt und gibt Element zurück
- `del` - Löscht Element an Index

## Nützliche Methoden

- `len()` - Länge der Liste
- `sort()` - Sortiert die Liste
- `reverse()` - Kehrt die Reihenfolge um
- `count()` - Zählt Vorkommen eines Elements
- `index()` - Findet Index eines Elements

## List Comprehensions

Elegante Methode zur Listenerstellung:

```python
quadrate = [x**2 for x in range(10)]
gerade_zahlen = [x for x in range(20) if x % 2 == 0]
```