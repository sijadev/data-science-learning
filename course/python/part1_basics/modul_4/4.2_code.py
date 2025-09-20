# Tupel

# Tupel erstellen
print("=== Tupel erstellen ===")
koordinaten = (10, 20)
einzelnes_tupel = (42,)  # Komma wichtig für einzelnes Element!
person = ("Alice", 30, "Berlin")
farben = ("rot", "grün", "blau")

print(f"Koordinaten: {koordinaten}")
print(f"Einzelnes Tupel: {einzelnes_tupel}")
print(f"Person: {person}")
print(f"Farben: {farben}")

# Tupel-Zugriff
print("\n=== Tupel-Zugriff ===")
print(f"X-Koordinate: {koordinaten[0]}")
print(f"Y-Koordinate: {koordinaten[1]}")
print(f"Erste Farbe: {farben[0]}")
print(f"Letzte Farbe: {farben[-1]}")

# Tupel Unpacking
print("\n=== Tupel Unpacking ===")
x, y = koordinaten
print(f"x = {x}, y = {y}")

name, alter, stadt = person
print(f"Name: {name}, Alter: {alter}, Stadt: {stadt}")

# Extended Unpacking
print("\n=== Extended Unpacking ===")
zahlen = (1, 2, 3, 4, 5, 6, 7)
erste, zweite, *mittlere, vorletzte, letzte = zahlen
print(f"Erste: {erste}")
print(f"Zweite: {zweite}")
print(f"Mittlere: {mittlere}")
print(f"Vorletzte: {vorletzte}")
print(f"Letzte: {letzte}")

# Named Tuples
print("\n=== Named Tuples ===")
from collections import namedtuple

# Punkt definieren
Punkt = namedtuple('Punkt', ['x', 'y'])
p1 = Punkt(10, 20)
p2 = Punkt(x=5, y=15)

print(f"Punkt 1: {p1}")
print(f"P1.x: {p1.x}, P1.y: {p1.y}")
print(f"Punkt 2: {p2}")

# Person definieren
Person = namedtuple('Person', 'name alter beruf')
alice = Person("Alice", 30, "Entwicklerin")
bob = Person("Bob", 25, "Designer")

print(f"Alice: {alice}")
print(f"Alice Beruf: {alice.beruf}")
print(f"Bob Alter: {bob.alter}")

# Tupel als Dictionary Keys
print("\n=== Tupel als Dictionary Keys ===")
positionen = {
    (0, 0): "Start",
    (10, 10): "Ziel",
    (5, 5): "Checkpoint",
    (3, 7): "Hindernis"
}

print("Positionen auf der Karte:")
for position, beschreibung in positionen.items():
    print(f"  {position}: {beschreibung}")

# Tupel-Methoden
print("\n=== Tupel-Methoden ===")
test_tupel = (1, 2, 3, 2, 4, 2, 5)
print(f"Tupel: {test_tupel}")
print(f"Länge: {len(test_tupel)}")
print(f"Anzahl von 2: {test_tupel.count(2)}")
print(f"Index von 4: {test_tupel.index(4)}")

# Tupel vs. Listen
print("\n=== Tupel vs. Listen ===")
liste = [1, 2, 3]
tupel = (1, 2, 3)

print(f"Liste: {liste} (veränderbar)")
print(f"Tupel: {tupel} (unveränderbar)")

liste[0] = 999
print(f"Liste nach Änderung: {liste}")
# tupel[0] = 999  # Das würde einen Fehler verursachen!

# Tupel in Listen umwandeln und zurück
print("\n=== Konvertierung ===")
original_tupel = (1, 2, 3, 4, 5)
als_liste = list(original_tupel)
print(f"Tupel zu Liste: {als_liste}")

als_liste.append(6)
zurück_zu_tupel = tuple(als_liste)
print(f"Modifiziert zurück zu Tupel: {zurück_zu_tupel}")
