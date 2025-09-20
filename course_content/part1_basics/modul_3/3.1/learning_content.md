# 🔀 Bedingte Anweisungen

## if-Anweisung

Die if-Anweisung ermöglicht es, Code nur unter bestimmten Bedingungen auszuführen.

```python
if alter >= 18:
    print("Volljährig")
else:
    print("Minderjährig")
```

## if-elif-else Kette

Für mehrere Bedingungen verwenden wir elif (else if):

```python
if note >= 90:
    bewertung = "Ausgezeichnet"
elif note >= 80:
    bewertung = "Sehr gut"
elif note >= 70:
    bewertung = "Gut"
else:
    bewertung = "Verbesserung nötig"
```

## Vergleichsoperatoren

- `==` Gleich
- `!=` Ungleich
- `<` Kleiner als
- `>` Größer als
- `<=` Kleiner oder gleich
- `>=` Größer oder gleich

## Logische Operatoren

- `and` Und-Verknüpfung
- `or` Oder-Verknüpfung
- `not` Negation

## Ternärer Operator

Kurze Schreibweise für einfache if-else Anweisungen:

```python
status = "aktiv" if alter >= 18 else "inaktiv"
```