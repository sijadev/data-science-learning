# Module und Pakete

# Eingebaute Module importieren
print("=== Eingebaute Module ===")
import math
import random
import datetime

# Math-Modul verwenden
print(f"Pi: {math.pi}")
print(f"Quadratewurzel von 16: {math.sqrt(16)}")
print(f"2 hoch 3: {math.pow(2, 3)}")
print(f"Aufrunden 4.3: {math.ceil(4.3)}")
print(f"Abrunden 4.7: {math.floor(4.7)}")

# Random-Modul verwenden
print(f"\nZufallszahl: {random.random()}")
print(f"Zufallszahl 1-10: {random.randint(1, 10)}")

früchte = ["Apfel", "Banane", "Kirsche", "Dattel"]
print(f"Zufällige Frucht: {random.choice(früchte)}")

# Datetime-Modul verwenden
jetzt = datetime.datetime.now()
print(f"Aktuelles Datum: {jetzt}")
print(f"Nur Datum: {jetzt.date()}")
print(f"Nur Zeit: {jetzt.time()}")

# Spezifische Funktionen importieren
print("\n=== Spezifische Imports ===")
from math import sin, cos, pi
from random import shuffle

print(f"sin(π/2): {sin(pi/2)}")
print(f"cos(0): {cos(0)}")

zahlen = [1, 2, 3, 4, 5]
shuffle(zahlen)
print(f"Gemischte Zahlen: {zahlen}")

# Import mit Alias
print("\n=== Import mit Alias ===")
import datetime as dt
import math as m

heute = dt.date.today()
print(f"Heute: {heute}")
print(f"e: {m.e}")

# Eigenes Modul erstellen (Simulation)
print("\n=== Eigenes Modul (Simulation) ===")

# Dies würde normalerweise in einer separaten .py Datei stehen
# Beispiel: mein_modul.py
class Rechner:
    @staticmethod
    def addieren(a, b):
        return a + b

    @staticmethod
    def multiplizieren(a, b):
        return a * b

def begrüßung(name):
    return f"Hallo {name} aus meinem Modul!"

# Verwendung des "Moduls"
rechner = Rechner()
print(f"5 + 3 = {rechner.addieren(5, 3)}")
print(f"4 × 6 = {rechner.multiplizieren(4, 6)}")
print(begrüßung("Python-Lerner"))

# Standard-Bibliothek Module
print("\n=== Weitere nützliche Module ===")

# OS-Modul für Betriebssystem-Funktionen
import os
print(f"Aktuelles Verzeichnis: {os.getcwd()}")
print(f"Betriebssystem: {os.name}")

# JSON-Modul für Datenverarbeitung
import json

person_dict = {"name": "Alice", "alter": 30, "beruf": "Entwicklerin"}
json_string = json.dumps(person_dict, ensure_ascii=False)
print(f"Als JSON: {json_string}")

zurück_dict = json.loads(json_string)
print(f"Zurück zu Dict: {zurück_dict}")

# Collections-Modul
print("\n=== Collections-Modul ===")
from collections import Counter, defaultdict

# Counter für Häufigkeiten
text = "Python ist toll und Python macht Spaß"
wort_zähler = Counter(text.split())
print(f"Wort-Häufigkeiten: {wort_zähler}")
print(f"Häufigste Wörter: {wort_zähler.most_common(2)}")

# defaultdict für automatische Standardwerte
gruppen = defaultdict(list)
personen = [
    ("Alice", "Entwicklung"),
    ("Bob", "Design"),
    ("Charlie", "Entwicklung"),
    ("Diana", "Marketing")
]

for name, abteilung in personen:
    gruppen[abteilung].append(name)

print("Gruppen nach Abteilung:")
for abteilung, mitarbeiter in gruppen.items():
    print(f"  {abteilung}: {mitarbeiter}")

# Itertools-Modul
print("\n=== Itertools-Modul ===")
import itertools

# Permutationen
zahlen = [1, 2, 3]
perms = list(itertools.permutations(zahlen, 2))
print(f"Permutationen von {zahlen}: {perms}")

# Kombinationen
kombs = list(itertools.combinations(zahlen, 2))
print(f"Kombinationen von {zahlen}: {kombs}")

# Cycle (unendliche Wiederholung)
farben = itertools.cycle(['rot', 'grün', 'blau'])
print("Erste 6 Farben aus Cycle:")
for i, farbe in enumerate(farben):
    if i >= 6:
        break
    print(f"  {i+1}: {farbe}")

# Sys-Modul für System-Informationen
print("\n=== Sys-Modul ===")
import sys

print(f"Python-Version: {sys.version}")
print(f"Plattform: {sys.platform}")
print(f"Encoding: {sys.getdefaultencoding()}")

# Module-Pfad anzeigen
print(f"Modul-Suchpfade (erste 3): {sys.path[:3]}")

# __name__ Variable
print("\n=== __name__ Variable ===")
print(f"Aktueller __name__: {__name__}")

# In einem echten Modul würde man schreiben:
# if __name__ == "__main__":
#     # Code der nur ausgeführt wird, wenn das Modul direkt gestartet wird
#     print("Dieses Modul wurde direkt ausgeführt!")

# Verfügbare Attribute eines Moduls anzeigen
print("\n=== Modul-Attribute ===")
mathe_attribute = [attr for attr in dir(math) if not attr.startswith('_')]
print(f"Math-Modul Funktionen (erste 10): {mathe_attribute[:10]}")

# Help-System
print("\n=== Help-System ===")
print("Hilfe für math.sqrt:")
help(math.sqrt)