# 📚 Dictionaries (Wörterbücher)

## Was sind Dictionaries?

Dictionaries speichern Schlüssel-Wert-Paare und ermöglichen schnellen Zugriff über Schlüssel.

```python
person = {
    "name": "Alice",
    "alter": 30,
    "beruf": "Entwicklerin"
}
```

## Dictionary-Operationen

### Zugriff auf Werte

```python
# Direkter Zugriff
name = person["name"]

# Sicherer Zugriff
beruf = person.get("beruf", "Unbekannt")
```

### Hinzufügen und Ändern

```python
person["gehalt"] = 75000  # Neuer Schlüssel
person["alter"] = 31      # Wert ändern
```

### Elemente entfernen

- `pop()` - Entfernt und gibt Wert zurück
- `popitem()` - Entfernt letztes Element
- `del` - Löscht Schlüssel-Wert-Paar

## Dictionary-Methoden

- `keys()` - Alle Schlüssel
- `values()` - Alle Werte
- `items()` - Alle Schlüssel-Wert-Paare
- `update()` - Fügt anderes Dictionary hinzu
- `clear()` - Leert das Dictionary

## Iteration

```python
# Über Schlüssel
for key in person:
    print(key, person[key])

# Über Schlüssel-Wert-Paare
for key, value in person.items():
    print(f"{key}: {value}")
```

## Dictionary Comprehensions

```python
quadrate = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

wort_längen = {wort: len(wort) for wort in ["Python", "ist", "toll"]}
```

## Verschachtelte Dictionaries

```python
studenten = {
    "alice": {
        "noten": {"Mathe": 1, "Physik": 2},
        "semester": 3
    },
    "bob": {
        "noten": {"Mathe": 2, "Physik": 1},
        "semester": 2
    }
}
```

## Praktische Anwendungen

- Konfigurationsdaten
- Datenbankergebnisse
- Zuordnungstabellen
- Zähler und Statistiken
- API-Responses