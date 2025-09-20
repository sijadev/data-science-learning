# Tupel
# Übung: Unveränderliche Sequenzen

# TODO: Tupel erstellen
koordinaten = (10, 20)
einzelnes_tupel = (42,)  # Komma wichtig!
person = ("Alice", 30, "Berlin")

# TODO: Tupel unpacking
x, y = koordinaten
name, alter, stadt = person
print(f"Position: x={x}, y={y}")
print(f"Person: {name}, {alter} Jahre, aus {stadt}")

# TODO: Extended unpacking
zahlen = (1, 2, 3, 4, 5, 6)
erste, *mittlere, letzte = zahlen
print(f"Erste: {erste}, Mittlere: {mittlere}, Letzte: {letzte}")

# TODO: Named Tuples
from collections import namedtuple
Punkt = namedtuple('Punkt', ['x', 'y'])
p1 = Punkt(10, 20)
print(f"Punkt: x={p1.x}, y={p1.y}")

# TODO: Tupel als Dictionary Keys
positionen = {
    (0, 0): "Start",
    (10, 10): "Ziel",
    (5, 5): "Checkpoint"
}
print(f"Position (5,5): {positionen[(5, 5)]}")