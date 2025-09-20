# Sets
# Übung: Eindeutige Sammlungen

# TODO: Sets erstellen
zahlen = {1, 2, 3, 4, 5}
duplikate = [1, 2, 2, 3, 3, 3, 4, 5]
eindeutig = set(duplikate)
print(f"Ohne Duplikate: {eindeutig}")

# TODO: Set Operationen
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"Vereinigung: {a | b}")
print(f"Schnittmenge: {a & b}")
print(f"Differenz: {a - b}")
print(f"Symmetrische Differenz: {a ^ b}")

# TODO: Set Methoden
farben = {"rot", "grün", "blau"}
farben.add("gelb")
farben.update(["orange", "lila"])
print(f"Farben: {farben}")

# TODO: Membership tests
print(f"'rot' in farben: {'rot' in farben}")
print(f"'schwarz' in farben: {'schwarz' in farben}")

# TODO: Set Comprehension
gerade_quadrate = {x**2 for x in range(10) if x % 2 == 0}
print(f"Gerade Quadrate: {gerade_quadrate}")