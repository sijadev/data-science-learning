# 🎯 Sets (Mengen)

## Was sind Sets?

Sets sind ungeordnete Sammlungen eindeutiger Elemente - keine Duplikate erlaubt.

```python
zahlen = {1, 2, 3, 4, 5}
gemischt = {1, "Text", 3.14}
```

## Set-Eigenschaften

- **Eindeutig:** Jedes Element nur einmal
- **Ungeordnet:** Keine feste Reihenfolge
- **Veränderlich:** Elemente können hinzugefügt/entfernt werden
- **Hashbar:** Nur unveränderliche Elemente

## Duplikat-Entfernung

```python
liste_mit_duplikaten = [1, 2, 2, 3, 3, 4]
eindeutige_werte = set(liste_mit_duplikaten)
# {1, 2, 3, 4}
```

## Set-Operationen

### Mathematische Operationen

- **Vereinigung (Union):** `set_a | set_b`
- **Schnittmenge (Intersection):** `set_a & set_b`
- **Differenz:** `set_a - set_b`
- **Symmetrische Differenz:** `set_a ^ set_b`

### Vergleiche

- **Teilmenge:** `set_a.issubset(set_b)`
- **Obermenge:** `set_a.issuperset(set_b)`
- **Disjunkt:** `set_a.isdisjoint(set_b)`

## Set-Methoden

- `add()` - Element hinzufügen
- `update()` - Mehrere Elemente hinzufügen
- `remove()` - Element entfernen (Fehler wenn nicht vorhanden)
- `discard()` - Element entfernen (kein Fehler)
- `pop()` - Zufälliges Element entfernen und zurückgeben

## Frozenset

Unveränderliche Version von Sets:

```python
frozen = frozenset([1, 2, 3, 4])
# Kann als Dictionary-Key verwendet werden
```

## Praktische Anwendungen

- Eindeutige Werte finden
- Schnelle Mitgliedschaftstests
- Mathematische Mengenlehre
- Datenbereinigung