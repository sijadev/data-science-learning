# 🔄 Schleifen

## for-Schleife

Die for-Schleife wird verwendet, um über Sequenzen zu iterieren.

### Mit range()

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

### Mit Listen

```python
früchte = ["Apfel", "Banane", "Kirsche"]
for frucht in früchte:
    print(frucht)
```

### Mit enumerate()

Um sowohl Index als auch Wert zu erhalten:

```python
for index, frucht in enumerate(früchte):
    print(f"{index}: {frucht}")
```

## while-Schleife

Die while-Schleife läuft solange eine Bedingung wahr ist:

```python
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
```

## Schleifenkontrolle

- `break` - Beendet die Schleife sofort
- `continue` - Springt zum nächsten Durchlauf

## List Comprehensions

Elegante Methode zur Listenerstellung:

```python
quadrate = [x**2 for x in range(10)]
gerade_zahlen = [x for x in range(20) if x % 2 == 0]
```