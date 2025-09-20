# Listen

# Listen erstellen
print("=== Listen erstellen ===")
zahlen = [1, 2, 3, 4, 5]
gemischte_liste = [1, "Text", 3.14, True, None]
leere_liste = []

print(f"Zahlen: {zahlen}")
print(f"Gemischte Liste: {gemischte_liste}")
print(f"Leere Liste: {leere_liste}")

# Listen-Zugriff und Slicing
print("\n=== Listen-Zugriff ===")
früchte = ["Apfel", "Banane", "Kirsche", "Dattel", "Erdbeere"]
print(f"Erste Frucht: {früchte[0]}")
print(f"Letzte Frucht: {früchte[-1]}")
print(f"Erste 3: {früchte[:3]}")
print(f"Letzte 2: {früchte[-2:]}")
print(f"Jede zweite: {früchte[::2]}")

# Elemente hinzufügen
print("\n=== Elemente hinzufügen ===")
meine_liste = [1, 2, 3]
print(f"Start: {meine_liste}")

meine_liste.append(4)
print(f"Nach append(4): {meine_liste}")

meine_liste.extend([5, 6, 7])
print(f"Nach extend([5,6,7]): {meine_liste}")

meine_liste.insert(0, 0)
print(f"Nach insert(0, 0): {meine_liste}")

# Elemente entfernen
print("\n=== Elemente entfernen ===")
test_liste = [1, 2, 3, 2, 4, 2, 5]
print(f"Start: {test_liste}")

test_liste.remove(2)  # Entfernt erstes Vorkommen
print(f"Nach remove(2): {test_liste}")

letztes = test_liste.pop()
print(f"Pop entfernt: {letztes}, Liste: {test_liste}")

element = test_liste.pop(1)
print(f"Pop(1) entfernt: {element}, Liste: {test_liste}")

# Listen-Methoden
print("\n=== Listen-Methoden ===")
zahlen_liste = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {zahlen_liste}")
print(f"Länge: {len(zahlen_liste)}")
print(f"Index von 4: {zahlen_liste.index(4)}")
print(f"Anzahl von 1: {zahlen_liste.count(1)}")
print(f"Maximum: {max(zahlen_liste)}")
print(f"Minimum: {min(zahlen_liste)}")
print(f"Summe: {sum(zahlen_liste)}")

# Sortieren
zahlen_kopie = zahlen_liste.copy()
zahlen_kopie.sort()
print(f"Sortiert: {zahlen_kopie}")

zahlen_kopie.reverse()
print(f"Umgekehrt: {zahlen_kopie}")

# List Comprehensions
print("\n=== List Comprehensions ===")
quadrate = [x**2 for x in range(1, 6)]
print(f"Quadrate: {quadrate}")

gerade_quadrate = [x**2 for x in range(10) if x % 2 == 0]
print(f"Gerade Quadrate: {gerade_quadrate}")

wörter = ["Python", "ist", "fantastisch"]
groß = [wort.upper() for wort in wörter]
print(f"Großbuchstaben: {groß}")
