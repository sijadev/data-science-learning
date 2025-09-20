# 4.1 Listen - Code Examples

# ========================================
# Listen erstellen
# ========================================
print("=" * 50)
print("LISTEN ERSTELLEN")
print("=" * 50)

# Verschiedene Arten Listen zu erstellen
leer = []
zahlen = [1, 2, 3, 4, 5]
gemischt = [1, "Text", 3.14, True, None]
verschachtelt = [[1, 2], [3, 4], [5, 6]]

print(f"Leere Liste: {leer}")
print(f"Zahlen: {zahlen}")
print(f"Gemischt: {gemischt}")
print(f"Verschachtelt: {verschachtelt}")

# Mit list() Konstruktor
aus_string = list("Python")
aus_range = list(range(5))
aus_tuple = list((1, 2, 3))

print(f"\nAus String: {aus_string}")
print(f"Aus Range: {aus_range}")
print(f"Aus Tuple: {aus_tuple}")

# ========================================
# Indizierung und Slicing
# ========================================
print("\n" + "=" * 50)
print("INDIZIERUNG UND SLICING")
print("=" * 50)

liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f"Liste: {liste}")

# Einzelne Elemente
print(f"\nErstes Element [0]: {liste[0]}")
print(f"Letztes Element [-1]: {liste[-1]}")
print(f"Drittes Element [2]: {liste[2]}")
print(f"Vorletztes [-2]: {liste[-2]}")

# Slicing [start:stop:step]
print(f"\n[1:4]: {liste[1:4]}")
print(f"[:3]: {liste[:3]}")
print(f"[3:]: {liste[3:]}")
print(f"[::2]: {liste[::2]}")
print(f"[::-1]: {liste[::-1]}")  # Reverse

# Slice-Zuweisung
kopie = liste.copy()
kopie[1:3] = ['X', 'Y']
print(f"\nNach kopie[1:3] = ['X', 'Y']: {kopie}")

# ========================================
# Listen-Methoden
# ========================================
print("\n" + "=" * 50)
print("LISTEN-METHODEN")
print("=" * 50)

# append() - Element am Ende hinzufügen
liste = [1, 2, 3]
liste.append(4)
print(f"Nach append(4): {liste}")

# extend() - Mehrere Elemente hinzufügen
liste.extend([5, 6, 7])
print(f"Nach extend([5,6,7]): {liste}")

# insert() - An bestimmter Position einfügen
liste.insert(0, 0)
print(f"Nach insert(0, 0): {liste}")

# remove() - Erstes Vorkommen entfernen
liste.remove(3)
print(f"Nach remove(3): {liste}")

# pop() - Element entfernen und zurückgeben
letztes = liste.pop()
print(f"Nach pop(): {liste}, entfernt: {letztes}")
erstes = liste.pop(0)
print(f"Nach pop(0): {liste}, entfernt: {erstes}")

# clear() - Liste leeren
kopie = liste.copy()
kopie.clear()
print(f"Nach clear(): {kopie}")

# ========================================
# Sortierung und Umkehrung
# ========================================
print("\n" + "=" * 50)
print("SORTIERUNG")
print("=" * 50)

zahlen = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {zahlen}")

# sort() - In-place Sortierung
zahlen.sort()
print(f"Nach sort(): {zahlen}")

zahlen.sort(reverse=True)
print(f"Nach sort(reverse=True): {zahlen}")

# sorted() - Neue sortierte Liste
original = [3, 1, 4, 1, 5]
sortiert = sorted(original)
print(f"\nOriginal: {original}")
print(f"sorted(): {sortiert}")

# Mit key-Funktion
wörter = ["Python", "ist", "eine", "tolle", "Sprache"]
nach_länge = sorted(wörter, key=len)
print(f"\nNach Länge sortiert: {nach_länge}")

# reverse() - Umkehren
liste = [1, 2, 3, 4, 5]
liste.reverse()
print(f"\nNach reverse(): {liste}")

# ========================================
# List Comprehensions
# ========================================
print("\n" + "=" * 50)
print("LIST COMPREHENSIONS")
print("=" * 50)

# Einfache Comprehension
quadrate = [x**2 for x in range(10)]
print(f"Quadratzahlen: {quadrate}")

# Mit Bedingung
gerade = [x for x in range(20) if x % 2 == 0]
print(f"Gerade Zahlen: {gerade}")

# Mit if-else
ergebnis = [x if x % 2 == 0 else -x for x in range(10)]
print(f"Gerade positiv, ungerade negativ: {ergebnis}")

# Verschachtelte Comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Multiplikationstabelle: {matrix}")

# String-Verarbeitung
wörter = ["Python", "ist", "TOLL"]
klein = [w.lower() for w in wörter]
print(f"Kleinbuchstaben: {klein}")

# ========================================
# Listen-Operationen
# ========================================
print("\n" + "=" * 50)
print("LISTEN-OPERATIONEN")
print("=" * 50)

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

# Konkatenation
kombiniert = liste1 + liste2
print(f"{liste1} + {liste2} = {kombiniert}")

# Wiederholung
wiederholt = liste1 * 3
print(f"{liste1} * 3 = {wiederholt}")

# Mitgliedschaft
print(f"2 in {liste1}: {2 in liste1}")
print(f"10 not in {liste1}: {10 not in liste1}")

# count() - Vorkommen zählen
zahlen = [1, 2, 3, 2, 2, 4]
print(f"\n2 kommt {zahlen.count(2)}x vor in {zahlen}")

# index() - Position finden
position = zahlen.index(2)
print(f"Erste Position von 2: {position}")

# ========================================
# Praktische Beispiele
# ========================================
print("\n" + "=" * 50)
print("PRAKTISCHE BEISPIELE")
print("=" * 50)

# Stack (LIFO) mit Liste
stack = []
stack.append("A")  # Push
stack.append("B")
stack.append("C")
print(f"Stack: {stack}")
top = stack.pop()  # Pop
print(f"Entfernt: {top}, Stack: {stack}")

# Queue (FIFO) - Ineffizient mit Liste!
from collections import deque
queue = deque(["A", "B", "C"])
queue.append("D")  # Hinten anfügen
first = queue.popleft()  # Vorne entfernen
print(f"\nQueue nach popleft: {list(queue)}")

# Matrix-Operationen
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transponieren
transponiert = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"\nTransponierte Matrix: {transponiert}")

# Flatten (2D zu 1D)
flach = [element for row in matrix for element in row]
print(f"Flache Liste: {flach}")

# ========================================
# Kopieren von Listen
# ========================================
print("\n" + "=" * 50)
print("KOPIEREN VON LISTEN")
print("=" * 50)

original = [1, [2, 3], 4]

# Shallow Copy
shallow = original.copy()
shallow[0] = 99
shallow[1][0] = 88
print(f"Original nach Shallow Copy: {original}")
print(f"Shallow Copy: {shallow}")

# Deep Copy
import copy
original = [1, [2, 3], 4]
deep = copy.deepcopy(original)
deep[1][0] = 77
print(f"\nOriginal nach Deep Copy: {original}")
print(f"Deep Copy: {deep}")

# ========================================
# Performance-Tipps
# ========================================
print("\n" + "=" * 50)
print("PERFORMANCE-TIPPS")
print("=" * 50)

import time

# List Comprehension vs. Loop
start = time.time()
result1 = []
for i in range(10000):
    result1.append(i**2)
zeit1 = time.time() - start

start = time.time()
result2 = [i**2 for i in range(10000)]
zeit2 = time.time() - start

print(f"Loop: {zeit1:.6f}s")
print(f"Comprehension: {zeit2:.6f}s")
print(f"Comprehension ist {zeit1/zeit2:.2f}x schneller")

# ========================================
# Erweiterte Techniken
# ========================================
print("\n" + "=" * 50)
print("ERWEITERTE TECHNIKEN")
print("=" * 50)

# Filter mit Comprehension
zahlen = range(-5, 6)
positiv = [x for x in zahlen if x > 0]
print(f"Positive Zahlen: {positiv}")

# Map mit Comprehension
wörter = ["python", "java", "javascript"]
großbuchstaben = [w.upper() for w in wörter]
print(f"Großbuchstaben: {großbuchstaben}")

# Enumerate in Comprehension
indexed = [(i, val) for i, val in enumerate(['a', 'b', 'c'])]
print(f"Mit Index: {indexed}")

# Zip in Comprehension
liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']
kombiniert = [(x, y) for x, y in zip(liste1, liste2)]
print(f"Gezippt: {kombiniert}")