# Dictionaries (Wörterbücher)

# Dictionary erstellen
print("=== Dictionary erstellen ===")
person = {
    "name": "Alice",
    "alter": 30,
    "beruf": "Entwicklerin",
    "stadt": "Berlin"
}

noten = {"Deutsch": 2, "Mathe": 1, "Englisch": 2, "Sport": 3}
leeres_dict = {}

print(f"Person: {person}")
print(f"Noten: {noten}")
print(f"Leeres Dict: {leeres_dict}")

# Dictionary-Zugriff
print("\n=== Dictionary-Zugriff ===")
print(f"Name: {person['name']}")
print(f"Alter: {person['alter']}")

# Sicherer Zugriff mit get()
print(f"Beruf: {person.get('beruf', 'Unbekannt')}")
print(f"Gehalt: {person.get('gehalt', 'Nicht angegeben')}")

# Elemente hinzufügen und ändern
print("\n=== Elemente hinzufügen/ändern ===")
print(f"Vor Änderung: {person}")

person["gehalt"] = 75000
person["alter"] = 31
print(f"Nach Änderung: {person}")

# Dictionary-Methoden
print("\n=== Dictionary-Methoden ===")
auto = {"marke": "BMW", "modell": "X3", "jahr": 2020, "farbe": "blau"}

print(f"Keys: {list(auto.keys())}")
print(f"Values: {list(auto.values())}")
print(f"Items: {list(auto.items())}")

# Iterieren über Dictionary
print("\n=== Dictionary-Iteration ===")
for key in auto:
    print(f"{key}: {auto[key]}")

print("\nMit items():")
for key, value in auto.items():
    print(f"{key} → {value}")

# Dictionary Comprehensions
print("\n=== Dictionary Comprehensions ===")
quadrate = {x: x**2 for x in range(1, 6)}
print(f"Quadrate: {quadrate}")

gerade_quadrate = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Gerade Quadrate: {gerade_quadrate}")

# Wörter und ihre Längen
wörter = ["Python", "ist", "fantastisch", "und", "mächtig"]
wort_längen = {wort: len(wort) for wort in wörter}
print(f"Wort-Längen: {wort_längen}")

# Verschachtelte Dictionaries
print("\n=== Verschachtelte Dictionaries ===")
studenten = {
    "alice": {
        "noten": {"Mathe": 1, "Physik": 2},
        "semester": 3,
        "studiengang": "Informatik"
    },
    "bob": {
        "noten": {"Mathe": 2, "Physik": 1},
        "semester": 2,
        "studiengang": "Physik"
    }
}

print("Studenten-Daten:")
for name, daten in studenten.items():
    print(f"  {name.capitalize()}:")
    print(f"    Studiengang: {daten['studiengang']}")
    print(f"    Semester: {daten['semester']}")
    print(f"    Noten: {daten['noten']}")

# Dictionary-Operationen
print("\n=== Dictionary-Operationen ===")
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 4}

# Zusammenführen (Python 3.9+)
zusammengeführt = dict1 | dict2
print(f"Dict1: {dict1}")
print(f"Dict2: {dict2}")
print(f"Zusammengeführt: {zusammengeführt}")

# Update
dict1_kopie = dict1.copy()
dict1_kopie.update(dict2)
print(f"Nach Update: {dict1_kopie}")

# Elemente entfernen
print("\n=== Elemente entfernen ===")
test_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
print(f"Start: {test_dict}")

# pop() - entfernt und gibt Wert zurück
wert = test_dict.pop("b")
print(f"Pop 'b': {wert}, Dict: {test_dict}")

# popitem() - entfernt letztes Element
letztes = test_dict.popitem()
print(f"Popitem: {letztes}, Dict: {test_dict}")

# del - entfernt Element
del test_dict["a"]
print(f"Nach del 'a': {test_dict}")

# Praktisches Beispiel: Wörter zählen
print("\n=== Wörter zählen ===")
text = "Python ist toll Python macht Spaß toll ist Python sehr toll"
wort_häufigkeit = {}

for wort in text.split():
    wort_häufigkeit[wort] = wort_häufigkeit.get(wort, 0) + 1

print("Wort-Häufigkeiten:")
for wort, anzahl in wort_häufigkeit.items():
    print(f"  {wort}: {anzahl}")

# Default Dictionary Alternative
print("\n=== Mit setdefault() ===")
text2 = "Python ist eine tolle Sprache Python ist einfach"
häufigkeit2 = {}

for wort in text2.split():
    häufigkeit2.setdefault(wort, 0)
    häufigkeit2[wort] += 1

print(f"Häufigkeiten: {häufigkeit2}")