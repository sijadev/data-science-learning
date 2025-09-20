# Listen
# Übung: Listen erstellen und manipulieren

# TODO: Listen erstellen
meine_liste = [1, 2, 3, 4, 5]
gemischte_liste = [1, "Text", 3.14, True]

# TODO: Elemente hinzufügen
meine_liste.append(6)
meine_liste.extend([7, 8, 9])
meine_liste.insert(0, 0)
print(f"Nach Hinzufügungen: {meine_liste}")

# TODO: Elemente entfernen
meine_liste.remove(0)  # Entfernt ersten Wert 0
letztes = meine_liste.pop()  # Entfernt und gibt letztes Element zurück
print(f"Entferntes Element: {letztes}")
print(f"Nach Entfernungen: {meine_liste}")

# TODO: Listen durchsuchen und sortieren
zahlen = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Index von 4: {zahlen.index(4)}")
print(f"Anzahl von 1: {zahlen.count(1)}")

zahlen.sort()
print(f"Sortiert: {zahlen}")

# TODO: Slicing
print(f"Erste 3 Elemente: {zahlen[:3]}")
print(f"Letzte 3 Elemente: {zahlen[-3:]}")
print(f"Jedes zweite Element: {zahlen[::2]}")