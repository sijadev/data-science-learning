# 3.2 Schleifen - Code Examples

# ========================================
# For-Schleife
# ========================================
print("=" * 50)
print("FOR-SCHLEIFE")
print("=" * 50)

# Über Liste iterieren
früchte = ["Apfel", "Banane", "Orange"]
print("Früchte:")
for frucht in früchte:
    print(f"  - {frucht}")

# Über String iterieren
wort = "Python"
print(f"\nBuchstaben in '{wort}':")
for buchstabe in wort:
    print(f"  {buchstabe}", end=" ")
print()

# Über Dictionary iterieren
person = {"name": "Alice", "alter": 30, "stadt": "Berlin"}
print("\nDictionary Iteration:")

print("Keys:")
for key in person:
    print(f"  {key}")

print("Values:")
for value in person.values():
    print(f"  {value}")

print("Key-Value Paare:")
for key, value in person.items():
    print(f"  {key}: {value}")

# ========================================
# range() Funktion
# ========================================
print("\n" + "=" * 50)
print("RANGE() FUNKTION")
print("=" * 50)

# range(stop)
print("range(5):", list(range(5)))

# range(start, stop)
print("range(2, 8):", list(range(2, 8)))

# range(start, stop, step)
print("range(0, 10, 2):", list(range(0, 10, 2)))
print("range(10, 0, -1):", list(range(10, 0, -1)))

# Mit for-Schleife
print("\nQuadratzahlen:")
for i in range(1, 6):
    print(f"{i}² = {i**2}")

# ========================================
# enumerate() Funktion
# ========================================
print("\n" + "=" * 50)
print("ENUMERATE() FUNKTION")
print("=" * 50)

früchte = ["Apfel", "Banane", "Orange", "Mango"]

# Mit Index
print("Mit Index:")
for index, frucht in enumerate(früchte):
    print(f"{index}: {frucht}")

# Mit Start-Index
print("\nMit Start-Index 1:")
for nummer, frucht in enumerate(früchte, start=1):
    print(f"{nummer}. {frucht}")

# ========================================
# While-Schleife
# ========================================
print("\n" + "=" * 50)
print("WHILE-SCHLEIFE")
print("=" * 50)

# Einfache while-Schleife
count = 0
print("Countdown:")
while count < 5:
    print(f"  {count}")
    count += 1

# Mit Bedingung
print("\nSumme bis 100:")
summe = 0
zahl = 1
while summe < 100:
    summe += zahl
    zahl += 1
print(f"Summe: {summe}, letzte Zahl: {zahl-1}")

# Unendliche Schleife mit break
print("\nMit Benutzer-Input (simuliert):")
inputs = ["ja", "ja", "nein"]  # Simulierte Eingaben
index = 0
while True:
    if index < len(inputs):
        antwort = inputs[index]
        print(f"Weitermachen? {antwort}")
        if antwort.lower() == "nein":
            break
        index += 1
    else:
        break
print("Schleife beendet")

# ========================================
# break und continue
# ========================================
print("\n" + "=" * 50)
print("BREAK UND CONTINUE")
print("=" * 50)

# break - Schleife komplett beenden
print("Break Beispiel - Suche erste gerade Zahl:")
zahlen = [1, 3, 5, 8, 9, 10]
for zahl in zahlen:
    if zahl % 2 == 0:
        print(f"Erste gerade Zahl gefunden: {zahl}")
        break
    print(f"  {zahl} ist ungerade")

# continue - Nächste Iteration
print("\nContinue Beispiel - Nur gerade Zahlen:")
for i in range(10):
    if i % 2 != 0:
        continue  # Ungerade überspringen
    print(f"  {i}")

# Kombiniert in verschachtelten Schleifen
print("\nVerschachtelt mit break:")
for i in range(3):
    print(f"Äußere Schleife: {i}")
    for j in range(3):
        if j == 2:
            break
        print(f"  Innere Schleife: {j}")

# ========================================
# else in Schleifen
# ========================================
print("\n" + "=" * 50)
print("ELSE IN SCHLEIFEN")
print("=" * 50)

# for-else (wird ausgeführt wenn kein break)
print("Primzahl-Check mit for-else:")
def ist_primzahl(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"  {n} ist durch {i} teilbar")
            break
    else:
        print(f"  {n} ist eine Primzahl")
        return True
    return False

for zahl in [7, 8, 11, 15]:
    print(f"Teste {zahl}:")
    ist_primzahl(zahl)

# while-else
print("\nWhile-else Beispiel:")
versuche = 3
passwort = "geheim"
eingaben = ["falsch", "nochmal", "geheim"]  # Simuliert
index = 0

while versuche > 0:
    if index < len(eingaben):
        eingabe = eingaben[index]
        print(f"Versuch {4-versuche}: {eingabe}")
        if eingabe == passwort:
            print("Zugang gewährt!")
            break
        versuche -= 1
        index += 1
    else:
        break
else:
    print("Keine Versuche mehr - Zugang verweigert!")

# ========================================
# zip() Funktion
# ========================================
print("\n" + "=" * 50)
print("ZIP() FUNKTION")
print("=" * 50)

namen = ["Alice", "Bob", "Charlie"]
alter = [25, 30, 35]
städte = ["Berlin", "München", "Hamburg"]

print("Parallel iterieren:")
for name, age, stadt in zip(namen, alter, städte):
    print(f"{name} ({age}) aus {stadt}")

# Unterschiedliche Längen
zahlen1 = [1, 2, 3, 4, 5]
zahlen2 = [10, 20, 30]
print("\nUnterschiedliche Längen (stoppt bei kürzester):")
for a, b in zip(zahlen1, zahlen2):
    print(f"{a} + {b} = {a + b}")

# ========================================
# List Comprehensions (Preview)
# ========================================
print("\n" + "=" * 50)
print("LIST COMPREHENSIONS")
print("=" * 50)

# Traditionelle Schleife
quadrate = []
for x in range(5):
    quadrate.append(x ** 2)
print(f"Mit Schleife: {quadrate}")

# List Comprehension
quadrate = [x ** 2 for x in range(5)]
print(f"Mit Comprehension: {quadrate}")

# Mit Bedingung
gerade = [x for x in range(10) if x % 2 == 0]
print(f"Gerade Zahlen: {gerade}")

# ========================================
# Verschachtelte Schleifen
# ========================================
print("\n" + "=" * 50)
print("VERSCHACHTELTE SCHLEIFEN")
print("=" * 50)

# Multiplikationstabelle
print("Kleines Einmaleins (Ausschnitt):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j:2}", end="  ")
    print()

# Matrix durchlaufen
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nMatrix durchlaufen:")
for zeile in matrix:
    for element in zeile:
        print(f"{element:2}", end=" ")
    print()

# ========================================
# Praktische Beispiele
# ========================================
print("\n" + "=" * 50)
print("PRAKTISCHE BEISPIELE")
print("=" * 50)

# Fibonacci-Sequenz
def fibonacci(n):
    fib = []
    a, b = 0, 1
    while len(fib) < n:
        fib.append(a)
        a, b = b, a + b
    return fib

print(f"Fibonacci (10): {fibonacci(10)}")

# Wörter zählen
text = "Python ist toll Python macht Spaß Python ist mächtig"
wort_count = {}
for wort in text.split():
    wort_count[wort] = wort_count.get(wort, 0) + 1

print(f"\nWörter zählen:")
for wort, anzahl in wort_count.items():
    if anzahl > 1:
        print(f"  '{wort}': {anzahl}x")

# Pyramide zeichnen
print("\nPyramide:")
höhe = 5
for i in range(höhe):
    print(" " * (höhe - i - 1) + "*" * (2 * i + 1))

# ========================================
# Performance-Tipps
# ========================================
print("\n" + "=" * 50)
print("PERFORMANCE-TIPPS")
print("=" * 50)

import time

# Schlecht: String-Konkatenation in Schleife
start = time.time()
result = ""
for i in range(1000):
    result += str(i)
zeit1 = time.time() - start

# Besser: Join verwenden
start = time.time()
result = "".join(str(i) for i in range(1000))
zeit2 = time.time() - start

print(f"String-Konkatenation: {zeit1:.6f}s")
print(f"Join-Methode: {zeit2:.6f}s")
print(f"Join ist {zeit1/zeit2:.1f}x schneller")

# ========================================
# Fortgeschrittene Iteration
# ========================================
print("\n" + "=" * 50)
print("FORTGESCHRITTENE ITERATION")
print("=" * 50)

# reversed() - Rückwärts iterieren
print("Rückwärts:")
for i in reversed(range(5)):
    print(f"  {i}")

# sorted() - Sortiert iterieren
wörter = ["Zebra", "Affe", "Elefant", "Bär"]
print("\nSortiert:")
for wort in sorted(wörter):
    print(f"  {wort}")

# itertools (Preview)
import itertools

print("\nItertools cycle (erste 10):")
counter = 0
for item in itertools.cycle(['A', 'B', 'C']):
    if counter >= 10:
        break
    print(item, end=" ")
    counter += 1
print()