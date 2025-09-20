# Schleifen
# Übung: for und while Loops

# TODO: for-Schleife mit range
print("Zahlen von 1 bis 5:")
for i in range(1, 6):
    print(i)

# TODO: for-Schleife mit Liste
früchte = ["Apfel", "Banane", "Kirsche"]
for frucht in früchte:
    print(f"Ich mag {frucht}")

# TODO: enumerate für Index und Wert
for index, frucht in enumerate(früchte, 1):
    print(f"{index}. {frucht}")

# TODO: while-Schleife
zähler = 0
while zähler < 3:
    print(f"Zähler: {zähler}")
    zähler += 1

# TODO: List Comprehension
quadrate = [x**2 for x in range(5)]
print(f"Quadrate: {quadrate}")

gerade_zahlen = [x for x in range(10) if x % 2 == 0]
print(f"Gerade Zahlen: {gerade_zahlen}")

# TODO: break und continue
for i in range(10):
    if i == 3:
        continue  # Überspringe 3
    if i == 7:
        break     # Stoppe bei 7
    print(i)