# Sets (Mengen)

# Sets erstellen
print("=== Sets erstellen ===")
zahlen_set = {1, 2, 3, 4, 5}
gemischtes_set = {1, "Text", 3.14, True}
leeres_set = set()  # Wichtig: {} ist ein leeres Dictionary!

print(f"Zahlen Set: {zahlen_set}")
print(f"Gemischtes Set: {gemischtes_set}")
print(f"Leeres Set: {leeres_set}")

# Automatische Duplikat-Entfernung
print("\n=== Duplikat-Entfernung ===")
mit_duplikaten = {1, 2, 2, 3, 3, 3, 4, 5}
print(f"Mit Duplikaten: {mit_duplikaten}")

aus_liste = set([1, 1, 2, 2, 3, 3, 4, 5])
print(f"Aus Liste: {aus_liste}")

# Set-Operationen
print("\n=== Set-Operationen ===")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Vereinigung (Union)
vereinigung = set_a | set_b
print(f"Vereinigung (A ∪ B): {vereinigung}")

# Schnittmenge (Intersection)
schnittmenge = set_a & set_b
print(f"Schnittmenge (A ∩ B): {schnittmenge}")

# Differenz
differenz = set_a - set_b
print(f"Differenz (A - B): {differenz}")

# Symmetrische Differenz
sym_differenz = set_a ^ set_b
print(f"Symmetrische Differenz (A ⊕ B): {sym_differenz}")

# Set-Methoden
print("\n=== Set-Methoden ===")
mein_set = {1, 2, 3}
print(f"Start: {mein_set}")

mein_set.add(4)
print(f"Nach add(4): {mein_set}")

mein_set.update([5, 6, 7])
print(f"Nach update([5,6,7]): {mein_set}")

mein_set.remove(2)
print(f"Nach remove(2): {mein_set}")

mein_set.discard(10)  # Kein Fehler wenn Element nicht existiert
print(f"Nach discard(10): {mein_set}")

# Set-Vergleiche
print("\n=== Set-Vergleiche ===")
kleine_zahlen = {1, 2, 3}
große_zahlen = {1, 2, 3, 4, 5, 6}
andere_zahlen = {7, 8, 9}

print(f"Kleine Zahlen: {kleine_zahlen}")
print(f"Große Zahlen: {große_zahlen}")
print(f"Andere Zahlen: {andere_zahlen}")

print(f"Kleine ⊆ Große: {kleine_zahlen.issubset(große_zahlen)}")
print(f"Große ⊇ Kleine: {große_zahlen.issuperset(kleine_zahlen)}")
print(f"Kleine ∩ Andere = ∅: {kleine_zahlen.isdisjoint(andere_zahlen)}")

# Frozenset (unveränderlich)
print("\n=== Frozenset ===")
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {frozen}")
print(f"Typ: {type(frozen)}")

# frozen.add(6)  # Das würde einen Fehler verursachen!

# Praktisches Beispiel: Eindeutige Wörter
print("\n=== Eindeutige Wörter ===")
text = "Python ist toll Python macht Spaß toll ist Python"
wörter = text.split()
eindeutige_wörter = set(wörter)

print(f"Alle Wörter: {wörter}")
print(f"Eindeutige Wörter: {eindeutige_wörter}")
print(f"Anzahl gesamt: {len(wörter)}")
print(f"Anzahl eindeutig: {len(eindeutige_wörter)}")

# Set Comprehensions
print("\n=== Set Comprehensions ===")
quadrate = {x**2 for x in range(1, 6)}
print(f"Quadrate: {quadrate}")

gerade_zahlen = {x for x in range(20) if x % 2 == 0}
print(f"Gerade Zahlen: {gerade_zahlen}")