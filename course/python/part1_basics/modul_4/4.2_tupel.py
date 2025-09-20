# 4.2 Tupel - Code Examples

# ========================================
# Tupel erstellen
# ========================================
print("=" * 50)
print("TUPEL ERSTELLEN")
print("=" * 50)

# Verschiedene Arten Tupel zu erstellen
leer = ()
einzeln = (42,)  # Komma wichtig bei einzelnem Element!
zahlen = (1, 2, 3, 4, 5)
gemischt = (1, "Text", 3.14, True, None)
verschachtelt = ((1, 2), (3, 4), (5, 6))

print(f"Leeres Tupel: {leer}")
print(f"Einzelnes Element: {einzeln}")
print(f"Zahlen: {zahlen}")
print(f"Gemischt: {gemischt}")
print(f"Verschachtelt: {verschachtelt}")

# Ohne Klammern (Tuple Packing)
coordinates = 10, 20, 30
print(f"\nTuple Packing: {coordinates}")

# Mit tuple() Konstruktor
aus_liste = tuple([1, 2, 3])
aus_string = tuple("Python")
aus_range = tuple(range(5))

print(f"\nAus Liste: {aus_liste}")
print(f"Aus String: {aus_string}")
print(f"Aus Range: {aus_range}")

# ========================================
# Unveränderlichkeit (Immutability)
# ========================================
print("\n" + "=" * 50)
print("UNVERÄNDERLICHKEIT")
print("=" * 50)

t = (1, 2, 3)
print(f"Original Tupel: {t}")

# Dies würde einen Fehler verursachen:
try:
    t[0] = 99
except TypeError as e:
    print(f"Fehler beim Ändern: {e}")

# ABER: Mutable Objekte im Tupel können geändert werden
t_mit_liste = (1, [2, 3], 4)
print(f"\nTupel mit Liste: {t_mit_liste}")
t_mit_liste[1].append(99)
print(f"Nach Änderung der Liste: {t_mit_liste}")

# ========================================
# Indizierung und Slicing
# ========================================
print("\n" + "=" * 50)
print("INDIZIERUNG UND SLICING")
print("=" * 50)

t = ('a', 'b', 'c', 'd', 'e')
print(f"Tupel: {t}")

# Einzelne Elemente
print(f"Erstes Element [0]: {t[0]}")
print(f"Letztes Element [-1]: {t[-1]}")
print(f"Mittleres Element [2]: {t[2]}")

# Slicing
print(f"[1:4]: {t[1:4]}")
print(f"[:3]: {t[:3]}")
print(f"[2:]: {t[2:]}")
print(f"[::2]: {t[::2]}")
print(f"[::-1]: {t[::-1]}")  # Reverse

# ========================================
# Tuple Unpacking
# ========================================
print("\n" + "=" * 50)
print("TUPLE UNPACKING")
print("=" * 50)

# Einfaches Unpacking
punkt = (10, 20)
x, y = punkt
print(f"x = {x}, y = {y}")

# Multiple Assignment
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# Mit *-Operator (Extended Unpacking)
zahlen = (1, 2, 3, 4, 5)
erste, *mitte, letzte = zahlen
print(f"Erste: {erste}, Mitte: {mitte}, Letzte: {letzte}")

# Ignorieren von Werten mit _
daten = ("Alice", 25, "Berlin", "Engineer")
name, _, stadt, _ = daten
print(f"Name: {name}, Stadt: {stadt}")

# Funktionen mit mehreren Rückgabewerten
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"\nMin: {minimum}, Max: {maximum}")

# ========================================
# Tupel-Methoden
# ========================================
print("\n" + "=" * 50)
print("TUPEL-METHODEN")
print("=" * 50)

t = (1, 2, 3, 2, 4, 2, 5)
print(f"Tupel: {t}")

# count() - Vorkommen zählen
anzahl = t.count(2)
print(f"Die Zahl 2 kommt {anzahl}x vor")

# index() - Position finden
position = t.index(4)
print(f"Position von 4: {position}")

# Weitere Operationen
print(f"Länge: {len(t)}")
print(f"Maximum: {max(t)}")
print(f"Minimum: {min(t)}")
print(f"Summe: {sum(t)}")

# ========================================
# Named Tuples
# ========================================
print("\n" + "=" * 50)
print("NAMED TUPLES")
print("=" * 50)

from collections import namedtuple

# Named Tuple definieren
Person = namedtuple('Person', ['name', 'alter', 'stadt'])

# Instanz erstellen
alice = Person('Alice', 30, 'Berlin')
print(f"Person: {alice}")

# Zugriff auf Felder
print(f"Name: {alice.name}")
print(f"Alter: {alice.alter}")
print(f"Stadt: {alice.stadt}")

# Auch Index-Zugriff möglich
print(f"Index [0]: {alice[0]}")

# Unpacking funktioniert
name, alter, stadt = alice
print(f"Unpacked: {name}, {alter}, {stadt}")

# _asdict() Methode
person_dict = alice._asdict()
print(f"Als Dictionary: {person_dict}")

# _replace() Methode
bob = alice._replace(name='Bob', alter=25)
print(f"Neue Person: {bob}")

# ========================================
# Tupel vs. Listen
# ========================================
print("\n" + "=" * 50)
print("TUPEL VS. LISTEN")
print("=" * 50)

import sys
import time

# Speicherverbrauch
liste = [1, 2, 3, 4, 5]
tupel = (1, 2, 3, 4, 5)

print(f"Liste Größe: {sys.getsizeof(liste)} bytes")
print(f"Tupel Größe: {sys.getsizeof(tupel)} bytes")

# Performance bei Iteration
große_liste = list(range(100000))
großes_tupel = tuple(range(100000))

start = time.time()
for _ in große_liste:
    pass
liste_zeit = time.time() - start

start = time.time()
for _ in großes_tupel:
    pass
tupel_zeit = time.time() - start

print(f"\nIteration Liste: {liste_zeit:.6f}s")
print(f"Iteration Tupel: {tupel_zeit:.6f}s")

# ========================================
# Praktische Anwendungen
# ========================================
print("\n" + "=" * 50)
print("PRAKTISCHE ANWENDUNGEN")
print("=" * 50)

# Als Dictionary-Schlüssel
koordinaten = {
    (0, 0): "Ursprung",
    (1, 0): "Rechts",
    (0, 1): "Oben",
    (1, 1): "Diagonal"
}
print(f"Punkt (0,0): {koordinaten[(0, 0)]}")

# Mehrere Rückgabewerte
def statistiken(zahlen):
    return (
        min(zahlen),
        max(zahlen),
        sum(zahlen) / len(zahlen),
        len(zahlen)
    )

stats = statistiken([1, 2, 3, 4, 5])
min_val, max_val, avg_val, count = stats
print(f"\nStatistiken: Min={min_val}, Max={max_val}, Avg={avg_val:.2f}, Count={count}")

# Datensätze speichern
studenten = [
    ("Alice", 25, 1.3),
    ("Bob", 23, 2.0),
    ("Charlie", 24, 1.7)
]

for name, alter, note in studenten:
    print(f"{name} ({alter} Jahre): Note {note}")

# ========================================
# Tupel-Operationen
# ========================================
print("\n" + "=" * 50)
print("TUPEL-OPERATIONEN")
print("=" * 50)

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Konkatenation
kombiniert = t1 + t2
print(f"{t1} + {t2} = {kombiniert}")

# Wiederholung
wiederholt = t1 * 3
print(f"{t1} * 3 = {wiederholt}")

# Mitgliedschaft
print(f"2 in {t1}: {2 in t1}")
print(f"10 not in {t1}: {10 not in t1}")

# Vergleiche (lexikographisch)
t3 = (1, 2, 3)
t4 = (1, 2, 4)
print(f"\n{t3} < {t4}: {t3 < t4}")
print(f"{t3} == {t1}: {t3 == t1}")

# ========================================
# Fortgeschrittene Techniken
# ========================================
print("\n" + "=" * 50)
print("FORTGESCHRITTENE TECHNIKEN")
print("=" * 50)

# Tupel als Funktionsargumente
def print_info(*args):
    """Beliebige Anzahl von Argumenten"""
    for i, arg in enumerate(args, 1):
        print(f"  Argument {i}: {arg}")

print("Variable Argumente:")
print_info("Python", 3.12, True)

# Zip mit Tupeln
namen = ("Alice", "Bob", "Charlie")
alter = (25, 30, 35)
städte = ("Berlin", "München", "Hamburg")

personen = list(zip(namen, alter, städte))
print(f"\nGezippte Personen: {personen}")

# Enumerate mit Tupeln
for index, (name, age, city) in enumerate(personen):
    print(f"{index}: {name} ({age}) aus {city}")

# Sortieren von Tupeln
punkte = [(3, 2), (1, 4), (2, 1), (3, 1)]
sortiert_x = sorted(punkte)  # Nach erstem Element
sortiert_y = sorted(punkte, key=lambda p: p[1])  # Nach zweitem Element

print(f"\nNach x sortiert: {sortiert_x}")
print(f"Nach y sortiert: {sortiert_y}")