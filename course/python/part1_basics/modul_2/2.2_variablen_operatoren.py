# 2.2 Variablen und Operatoren - Code Examples

# ========================================
# Variablenzuweisung
# ========================================
print("=" * 50)
print("VARIABLENZUWEISUNG")
print("=" * 50)

# Einfache Zuweisung
name = "Python"
age = 30
pi = 3.14159
is_active = True

print(f"name = {name}")
print(f"age = {age}")
print(f"pi = {pi}")
print(f"is_active = {is_active}")

# Mehrfachzuweisung
x, y, z = 1, 2, 3
print(f"\nx, y, z = 1, 2, 3")
print(f"x={x}, y={y}, z={z}")

# Gleiche Werte
a = b = c = 100
print(f"\na = b = c = 100")
print(f"a={a}, b={b}, c={c}")

# Tuple Unpacking
coordinates = (10, 20)
x, y = coordinates
print(f"\nTuple Unpacking: x={x}, y={y}")

# Variablen tauschen
x, y = y, x
print(f"Nach Tausch: x={x}, y={y}")

# ========================================
# Arithmetische Operatoren
# ========================================
print("\n" + "=" * 50)
print("ARITHMETISCHE OPERATOREN")
print("=" * 50)

a, b = 10, 3
print(f"a = {a}, b = {b}")
print("-" * 30)

print(f"Addition:       a + b = {a + b}")
print(f"Subtraktion:    a - b = {a - b}")
print(f"Multiplikation: a * b = {a * b}")
print(f"Division:       a / b = {a / b:.2f}")
print(f"Ganzzahldiv:    a // b = {a // b}")
print(f"Modulo:         a % b = {a % b}")
print(f"Potenz:         a ** b = {a ** b}")
print(f"Negative:       -a = {-a}")
print(f"Positive:       +a = {+a}")

# Komplexe Ausdrücke
result = (a + b) * 2 - a ** 2 / b
print(f"\n(a + b) * 2 - a² / b = {result:.2f}")

# Mit verschiedenen Typen
print("\nMit verschiedenen Typen:")
print(f"10 + 3.5 = {10 + 3.5}")
print(f"'Py' + 'thon' = {'Py' + 'thon'}")
print(f"'Ha' * 3 = {'Ha' * 3}")
print(f"[1, 2] + [3, 4] = {[1, 2] + [3, 4]}")

# ========================================
# Vergleichsoperatoren
# ========================================
print("\n" + "=" * 50)
print("VERGLEICHSOPERATOREN")
print("=" * 50)

x, y = 5, 10
print(f"x = {x}, y = {y}")
print("-" * 30)

print(f"Gleich:          x == y  → {x == y}")
print(f"Ungleich:        x != y  → {x != y}")
print(f"Größer:          x > y   → {x > y}")
print(f"Kleiner:         x < y   → {x < y}")
print(f"Größer gleich:   x >= y  → {x >= y}")
print(f"Kleiner gleich:  x <= y  → {x <= y}")

# String-Vergleiche
print("\nString-Vergleiche (lexikographisch):")
print(f"'apple' < 'banana' → {'apple' < 'banana'}")
print(f"'Python' == 'python' → {'Python' == 'python'}")
print(f"'10' < '2' → {'10' < '2'}  (String-Vergleich!)")

# Verkettete Vergleiche
a, b, c = 5, 10, 15
print(f"\nVerkettete Vergleiche:")
print(f"a < b < c → {a < b < c}")
print(f"a < b > 0 → {a < b > 0}")

# ========================================
# Logische Operatoren
# ========================================
print("\n" + "=" * 50)
print("LOGISCHE OPERATOREN")
print("=" * 50)

a, b = True, False
print(f"a = {a}, b = {b}")
print("-" * 30)

print(f"a and b  → {a and b}")
print(f"a or b   → {a or b}")
print(f"not a    → {not a}")
print(f"not b    → {not b}")

# Mit Zahlen
x, y = 5, 0
print(f"\nMit Zahlen (x={x}, y={y}):")
print(f"x and y  → {x and y}")
print(f"x or y   → {x or y}")
print(f"not x    → {not x}")
print(f"not y    → {not y}")

# Short-circuit Evaluation
print("\nShort-circuit Evaluation:")
print(f"False and (10/0) → False (Division wird nicht ausgeführt)")
print(f"True or (10/0) → True (Division wird nicht ausgeführt)")

# Praktisches Beispiel
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"\nKann fahren (age={age}, has_license={has_license}): {can_drive}")

# ========================================
# Bitweise Operatoren
# ========================================
print("\n" + "=" * 50)
print("BITWEISE OPERATOREN")
print("=" * 50)

a, b = 12, 5  # 12 = 1100, 5 = 0101 in Binär
print(f"a = {a} (0b{a:04b}), b = {b} (0b{b:04b})")
print("-" * 30)

print(f"AND:    a & b  = {a & b:2} (0b{a & b:04b})")
print(f"OR:     a | b  = {a | b:2} (0b{a | b:04b})")
print(f"XOR:    a ^ b  = {a ^ b:2} (0b{a ^ b:04b})")
print(f"NOT:    ~a     = {~a:2} (Zweierkomplement)")
print(f"Left:   a << 1 = {a << 1:2} (0b{a << 1:04b})")
print(f"Right:  a >> 1 = {a >> 1:2} (0b{a >> 1:04b})")

# Praktische Anwendung
flags = 0b0000
FLAG_READ = 0b0001
FLAG_WRITE = 0b0010
FLAG_EXECUTE = 0b0100

# Flags setzen
flags = flags | FLAG_READ | FLAG_WRITE
print(f"\nFlags nach Setzen: 0b{flags:04b}")

# Flag prüfen
has_read = bool(flags & FLAG_READ)
has_execute = bool(flags & FLAG_EXECUTE)
print(f"Hat Leserecht: {has_read}")
print(f"Hat Ausführungsrecht: {has_execute}")

# ========================================
# Zuweisungsoperatoren
# ========================================
print("\n" + "=" * 50)
print("ZUWEISUNGSOPERATOREN")
print("=" * 50)

x = 10
print(f"Start: x = {x}")

x += 5
print(f"x += 5  → x = {x}")

x -= 3
print(f"x -= 3  → x = {x}")

x *= 2
print(f"x *= 2  → x = {x}")

x //= 4
print(f"x //= 4 → x = {x}")

x %= 5
print(f"x %= 5  → x = {x}")

x **= 2
print(f"x **= 2 → x = {x}")

# Mit Strings
text = "Py"
text += "thon"
print(f"\nString: 'Py' += 'thon' → '{text}'")

# Mit Listen
liste = [1, 2]
liste += [3, 4]
print(f"Liste: [1, 2] += [3, 4] → {liste}")

# ========================================
# Identitäts- und Mitgliedschaftsoperatoren
# ========================================
print("\n" + "=" * 50)
print("IDENTITÄTS- UND MITGLIEDSCHAFT")
print("=" * 50)

# Identitätsoperatoren (is, is not)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("Identität (is):")
print(f"a = {a}")
print(f"b = {b} (gleicher Inhalt)")
print(f"c = a (gleiche Referenz)")
print(f"a == b  → {a == b}  (gleicher Wert)")
print(f"a is b  → {a is b}  (nicht gleiche Objekte)")
print(f"a is c  → {a is c}  (gleiche Objekte)")

# None Vergleich
x = None
print(f"\nx is None → {x is None}  (Best Practice)")
print(f"x == None → {x == None}  (Funktioniert, aber nicht empfohlen)")

# Mitgliedschaftsoperatoren (in, not in)
print("\nMitgliedschaft (in):")
text = "Python Programming"
print(f"Text: '{text}'")
print(f"'Python' in text     → {'Python' in text}")
print(f"'Java' not in text   → {'Java' not in text}")

numbers = [1, 2, 3, 4, 5]
print(f"\nListe: {numbers}")
print(f"3 in numbers         → {3 in numbers}")
print(f"10 not in numbers    → {10 not in numbers}")

# ========================================
# Operator-Priorität
# ========================================
print("\n" + "=" * 50)
print("OPERATOR-PRIORITÄT")
print("=" * 50)

print("Reihenfolge (höchste zuerst):")
print("1. () Klammern")
print("2. ** Potenz")
print("3. +x, -x, ~x Unäre Operatoren")
print("4. *, /, //, % Multiplikation, Division")
print("5. +, - Addition, Subtraktion")
print("6. <<, >> Bitverschiebung")
print("7. & Bitweises AND")
print("8. ^ Bitweises XOR")
print("9. | Bitweises OR")
print("10. ==, !=, <, <=, >, >= Vergleiche")
print("11. is, is not, in, not in")
print("12. not Logisches NOT")
print("13. and Logisches AND")
print("14. or Logisches OR")

# Beispiele
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
print(f"\n2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")

result3 = True or False and False
result4 = (True or False) and False
print(f"\nTrue or False and False = {result3}")
print(f"(True or False) and False = {result4}")

# ========================================
# Walrus Operator := (Python 3.8+)
# ========================================
print("\n" + "=" * 50)
print("WALRUS OPERATOR :=")
print("=" * 50)

# Zuweisung in Ausdrücken
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"Liste hat {n} Elemente (mehr als 3)")

# In While-Schleifen nützlich
data = [1, 2, 3, 0, 4, 5]
print(f"\nDaten: {data}")
print("Verarbeite bis 0 gefunden wird:")
i = 0
while i < len(data) and (value := data[i]) != 0:
    print(f"  Verarbeite: {value}")
    i += 1