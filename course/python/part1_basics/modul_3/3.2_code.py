# Schleifen

# for-Schleife mit range
print("=== for-Schleife mit range ===")
print("Zahlen von 1 bis 5:")
for i in range(1, 6):
    print(f"  {i}")

print("\nGerade Zahlen von 0 bis 10:")
for i in range(0, 11, 2):
    print(f"  {i}")

# for-Schleife mit Listen
print("\n=== for-Schleife mit Listen ===")
früchte = ["Apfel", "Banane", "Kirsche", "Dattel"]
for frucht in früchte:
    print(f"Ich mag {frucht}")

# enumerate für Index und Wert
print("\n=== enumerate() für Index ===")
for index, frucht in enumerate(früchte, 1):
    print(f"{index}. {frucht}")

# zip für parallele Listen
print("\n=== zip() für parallele Listen ===")
namen = ["Alice", "Bob", "Charlie"]
alter = [25, 30, 35]
for name, age in zip(namen, alter):
    print(f"{name} ist {age} Jahre alt")

# while-Schleife
print("\n=== while-Schleife ===")
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Start!")

# List Comprehensions
print("\n=== List Comprehensions ===")
quadrate = [x**2 for x in range(1, 6)]
print(f"Quadrate 1-5: {quadrate}")

gerade_zahlen = [x for x in range(20) if x % 2 == 0]
print(f"Gerade Zahlen 0-19: {gerade_zahlen}")

# break und continue
print("\n=== break und continue ===")
print("Zahlen 0-9, aber 3 überspringen und bei 7 stoppen:")
for i in range(10):
    if i == 3:
        print(f"  {i} übersprungen")
        continue
    if i == 7:
        print(f"  Bei {i} gestoppt")
        break
    print(f"  {i}")

# Verschachtelte Schleifen
print("\n=== Multiplikationstabelle ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()  # Neue Zeile nach jeder Reihe
